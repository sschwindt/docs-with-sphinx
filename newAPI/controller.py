"""
.. module:: controller
   :synopsis: All endpoints of the new API (with Contents) are defined here

.. moduleauthor:: Sebastian Schwindt <github.com/sschwindt>


"""

from flask import request, jsonify, abort, make_response, Blueprint
from newAPI.database import db_session
from newAPI.models import Content
from sqlalchemy import exc
import os

new_api = Blueprint('new_api', __name__)


@new_api.route('/', methods=['GET'])
def index():
    """
        **Get List of Contents**

        This function allows users to get a list of contents and the locations they're teaching.

        :return: content's information in json and http status code

        - Example::

              curl -X GET http://localhost:5000/ -H 'cache-control: no-cache' -H 'content-type: application/json'

        - Expected Success Response::

            HTTP Status Code: 200

            {
                "Contents": [
                    {
                        "id": 1,
                        "name": "Populus Fremontii",
                        "location": "Floodplain"
                    },
                    {
                        "id": 2,
                        "name": "Salix",
                        "location": "Banks"
                    },
                    {
                        "id": 3,
                        "name": "Acer Negundo",
                        "location": "Floodplain"
                    }
                ]
            }

    """
    contents = Content.query.all()
    return make_response(jsonify(Contents=[Content.serialize() for Content in contents]), 200)


@new_api.route('/', methods=['POST'])
def create_content():
    """
        **Create Content Record**

        This function allows user to create(post) a content record.

        :return: content information added by the user in json and http status code

        - Example::

            curl -X POST http://localhost:5000/ -H 'cache-control: no-cache' -H 'content-type: application/json' \
            -d '{
                "name": "Alnus Rhombifolia",
                "location": "Gravel Bars"
            }'

        - Expected Success Response::

            HTTP Status Code: 201

            {
                "name": "Alnus Rhombifolia",
                "location": "Gravel Bars"
            }

        - Expected Fail Response::

            HTTP Status Code: 400
            {'error': 'Duplicate content name'}

    """
    if not request.json:
        abort(400)
    content = request.get_json()
    if type(content['name']) != str:
        return make_response(jsonify({'error':'Content name should be a string'}), 400)
    try:
        content_temp = Content(name=content['name'],
                               location=content['location'])
        db_session.add(content_temp)
        db_session.commit()
        return jsonify(content), 201
    except exc.IntegrityError as e:
        return make_response(jsonify({'error': 'Duplicate content name'}), 400)


@new_api.route('/<int:content_id>', methods=['GET'])
def get_content(content_id):
    """
        **Get information of a specific content**

        This function allows user to get a specific content information through their content_id.

        :param content_id: id of the content
        :type content_id: int
        :return: content information accessed by user in json and http status code

        - Example::

            curl -X GET http://127.0.0.1:5000/1 -H 'cache-control: no-cache' -H 'content-type: application/json'

        - Expected Success Response::

            HTTP Status Code: 200

            {
                "Content": {
                    "id": 1,
                    "name": "Populus Fremontii",
                    "location": "Floodplain"
                }
            }

        - Expected Fail Response::

            HTTP Status Code: 404

            {'error': 'Not found'}

    """
    contents = Content.query.all()
    content = [content for content in contents if content.id == content_id]
    if len(content) == 0:
        not_found()
    return make_response(jsonify(Content=Content.serialize(content[0])), 200)


@new_api.route('/<int:content_id>', methods=['PUT'])
def update_content(content_id):
    """
        **Update Information of a Specific Content Record**

        This function allows user to update a specific content information through their content_id.

        :param content_id: id of the content
        :type content_id: int
        :return: content information updated by user in json and http status code

        - Example::

            curl -X PUT http://localhost:5000/1 -H 'cache-control: no-cache' -H 'content-type: application/json' \
            -d '{
                "name": "Alnus Rhombifolia",
                "location": "Floodplain"
            }'

        - Expected Success Response::

            HTTP Status Code: 200

            {
                "name": "Alnus Rhombifolia",
                "location": "Floodplain"
            }

        - Expected Fail Response::

            HTTP Status Code: 404

            {'error': 'Not found'}

            or

            HTTP Status Code: 404

            {'error': 'Duplicate content name'}

    """
    contents = Content.query.all()
    content = [content for content in contents if content.id == content_id]
    if len(content) == 0:
        not_found()
    if 'name' in request.json and type(request.json['name']) != str:
        return make_response(jsonify({'error': 'Content name not a string'}), 400)
    if 'location' in request.json and type(request.json['location']) != str:
        return make_response(jsonify({'error': 'Location not a string'}), 400)
    content = request.get_json()
    # updating the requested content record
    try:
        queried_content = Content.query.get(content_id)
        queried_content.name = content['name']
        queried_content.location = content['location']
        db_session.commit()
        return make_response(jsonify(content), 200)
    except exc.IntegrityError as e:
        return make_response(jsonify({'error': 'Duplicate content name'}), 400)


@new_api.route('/<int:content_id>', methods=['DELETE'])
def delete_content(content_id):
    """
        **Delete Content Record**

        This function allows user to delete a content record.

        :param content_id: id of the content
        :type content_id: int
        :return: delete status in json and http status code

        - Example::

            curl -X DELETE http://127.0.0.1:5000/4 -H 'cache-control: no-cache' -H 'content-type: application/json'

        - Expected Success Response::

            HTTP Status Code: 200

            {
                "Delete": true
            }

        - Expected Fail Response::

            HTTP Status Code: 404

            {'error': 'Not found'}

    """
    contents = Content.query.all()
    content = [content for content in contents if content.id == content_id]
    if len(content) == 0:
        not_found()
    Content.query.filter_by(id=content_id).delete()
    db_session.commit()
    return make_response(jsonify({'Delete': True}), 200)


@new_api.route('/search', methods=['POST'])
def search():
    """
        **Search Content Records**

        This function allows user to search for content through substring search of content names.

        :return: searched contents in json and http status code

        - Example::

            curl -X POST  http://localhost:5000/search -H 'cache-control: no-cache' -H 'content-type: application/json' \
            -d '{
                "value": "J"
            }'

        - Expected Success Response::

            HTTP Status Code: 200

            {
                "Contents": [
                    {
                        "id": 1,
                        "name": "Alnus Rhombifolia",
                        "location": "Floodplain"
                    },
                    {
                        "id": 2,
                        "name": "Salix",
                        "location": "Banks"
                    },
                    {
                        "id": 3,
                        "name": "Acer Negundo",
                        "location": "Floodplain"
                    }
                ]
            }

    """
    if not request.json:
        abort(400)
    if 'value' in request.json and type(request.json['value']) is not str:
        abort(400)
    content = request.get_json()
    contents = Content.query.filter(Content.name.like('%' + content['value']+ '%'))
    return make_response(jsonify(Contents=[Content.serialize() for Content in contents]), 200)


# Act as an error handler when a page is not found
@new_api.errorhandler(404)
def not_found():
    """
        **Error handler**

        This function returns a not found error in json when called.

        :return: not found error in json

    """
    return make_response(jsonify({'error': 'Not found'}), 404)
