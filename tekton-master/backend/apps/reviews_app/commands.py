# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from reviews_app.model import reviews

class reviewsPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = reviews
    _include = [reviews.link, 
                reviews.app, 
                reviews.nota, 
                reviews.descricao]


class reviewsForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = reviews
    _include = [reviews.link, 
                reviews.app, 
                reviews.nota, 
                reviews.descricao]


class reviewsDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = reviews
    _include = [reviews.nota, 
                reviews.app, 
                reviews.creation, 
                reviews.link, 
                reviews.descricao]


class reviewsShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = reviews
    _include = [reviews.nota, 
                reviews.app, 
                reviews.creation, 
                reviews.link, 
                reviews.descricao]


class SavereviewsCommand(SaveCommand):
    _model_form_class = reviewsForm


class UpdatereviewsCommand(UpdateNode):
    _model_form_class = reviewsForm


class ListreviewsCommand(ModelSearchCommand):
    def __init__(self):
        super(ListreviewsCommand, self).__init__(reviews.query_by_creation())

