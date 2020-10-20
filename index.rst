.. Tutorial on Documentation using Sphinx documentation


Configuration of Project Environment
*************************************

This is an API that manages a list of contents using Python3, Flask, and SQLAlchemy.

Overview on How to Run this API
================================
1. Either install a Python IDE or create a Python virtual environment to install the packages required
2. Install packages required
3. Install MySQL 5.7
4. Install Postman extension in Chrome or install curl

Setup procedure
================
1. Configure project environment - either install PyCharm or create a virtual environment (B)
    A. Install PyCharm ([read more](https://hydro-informatics.github.io/hy_ide.html#pycharm))
        - Open the New API Directory (File -> Open)
        - Configure the Base Project Interpreter (File -> Settings -> Project Interpreter)
            * Base Project Interpreter: pyenv version 3.6+ ('path to .pyenv version 3.6+'/bin/python)
                (pyenv was installed before creating the new project through 'pyenv install 3.6.3')
            .. note:: If the PyCharm interpreter fails to install packages (packages do not appear in the package list) and modules imported from them do not get resolved, use (B) - pyenv.
        - Manually install packages to project interpreter (PyCharm -> Preferences -> Project -> Project Interpreter -> plus button on the lower left side of the package table) and apply changes OR type the command below on the activated virtual environment. ::

            pip install -r requirements.txt

    B. Create a Python Virtual Environment
        - Install virtualenv::

            sudo pip install virtualenv

        - Create virtialenv::

            virtualenv -p python3 <name of virtualenv>

        - Install requirements::

            pip install -r requirements.txt

2. Install MySQL
    A. Search on the web on how to install MySQL in your OS
    B. Create database through piping
            mysql -u root < <Path to file>/create_db.sql
         * NOTE: depending on your mysql config, you need to provide your password if you have one
3. Initialize and Populate Company Database
    A. Edit line 14 of NewAPI/database.py and use the correct url to your mysql
        * In my case, I'm using the root and has a password of 'password'
        'mysql://root:<password>@localhost/Content'
    B. Either run the line below
        $ sh database_populator.sh

        OR

    C. Use the python interactive shell and run the lines below::

        $ python
        >> from NewAPI.database import init_db;
        >> init_db();
        >> from NewAPI.populate import populate;
        >> populate()

4. Run app.py::

    python app.py

5. Refer to NewAPI controller on how to test the code through curl

Endpoints of the New API
============================
1. Insert a new content record
2. Update an existing content record
3. Delete content record
4. Get content record details
5. List all content records
6. Filter list of contents using wildcard search


Documentation for the Code
**************************
.. toctree::
   :maxdepth: 2
   :caption: Contents:

NewAPI main
===================
.. automodule:: app
   :members:

NewAPI controller
=====================
.. automodule:: NewAPI.controller
   :members:

NewAPI models
=================
.. automodule:: NewAPI.models
   :members:

NewAPI database
===================
.. automodule:: NewAPI.database
   :members:

NewAPI populate
===================
.. automodule:: NewAPI.populate
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
