# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from listas_app.model import listas

class listasPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = listas
    _include = [listas.lista, 
                listas.nome]


class listasForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = listas
    _include = [listas.lista, 
                listas.nome]


class listasDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = listas
    _include = [listas.creation, 
                listas.lista, 
                listas.nome]


class listasShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = listas
    _include = [listas.creation, 
                listas.lista, 
                listas.nome]


class SavelistasCommand(SaveCommand):
    _model_form_class = listasForm


class UpdatelistasCommand(UpdateNode):
    _model_form_class = listasForm


class ListlistasCommand(ModelSearchCommand):
    def __init__(self):
        super(ListlistasCommand, self).__init__(listas.query_by_creation())

