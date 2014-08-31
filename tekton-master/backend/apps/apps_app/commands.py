# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from apps_app.model import apps

class appsPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = apps
    _include = [apps.link, 
                apps.nome]


class appsForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = apps
    _include = [apps.link, 
                apps.nome]


class appsDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = apps
    _include = [apps.creation, 
                apps.link, 
                apps.nome]


class appsShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = apps
    _include = [apps.creation, 
                apps.link, 
                apps.nome]


class SaveappsCommand(SaveCommand):
    _model_form_class = appsForm


class UpdateappsCommand(UpdateNode):
    _model_form_class = appsForm


class ListappsCommand(ModelSearchCommand):
    def __init__(self):
        super(ListappsCommand, self).__init__(apps.query_by_creation())

