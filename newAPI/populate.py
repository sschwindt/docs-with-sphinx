"""
.. module:: populate
   :synopsis: Populates database with Records

.. moduleauthor:: Sebastian Schwindt <github.com/sschwindt>


"""

from newAPI.models import Content
from newAPI.database import db_session


def populate():
    """
        **Populate Database**

        This populates the content table.

    """
    teacher_samp = Content(1, 'Acer Negundo', 'Floodplain')
    teacher_samp2 = Content(2, 'Salix', 'Banks')
    teacher_samp3 = Content(3, 'Alnus Rhombifolia', 'Gravel Bar')
    db_session.add(content_samp)
    db_session.add(content_samp2)
    db_session.add(content_samp3)
    db_session.commit()
