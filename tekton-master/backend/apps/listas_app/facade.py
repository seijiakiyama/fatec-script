# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from listas_app.commands import ListlistasCommand, SavelistasCommand, UpdatelistasCommand, \
    listasPublicForm, listasDetailForm, listasShortForm


def save_listas_cmd(**listas_properties):
    """
    Command to save listas entity
    :param listas_properties: a dict of properties to save on model
    :return: a Command that save listas, validating and localizing properties received as strings
    """
    return SavelistasCommand(**listas_properties)


def update_listas_cmd(listas_id, **listas_properties):
    """
    Command to update listas entity with id equals 'listas_id'
    :param listas_properties: a dict of properties to update model
    :return: a Command that update listas, validating and localizing properties received as strings
    """
    return UpdatelistasCommand(listas_id, **listas_properties)


def list_listass_cmd():
    """
    Command to list listas entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListlistasCommand()


def listas_detail_form(**kwargs):
    """
    Function to get listas's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return listasDetailForm(**kwargs)


def listas_short_form(**kwargs):
    """
    Function to get listas's short form. just a subset of listas's properties
    :param kwargs: form properties
    :return: Form
    """
    return listasShortForm(**kwargs)

def listas_public_form(**kwargs):
    """
    Function to get listas'spublic form. just a subset of listas's properties
    :param kwargs: form properties
    :return: Form
    """
    return listasPublicForm(**kwargs)


def get_listas_cmd(listas_id):
    """
    Find listas by her id
    :param listas_id: the listas id
    :return: Command
    """
    return NodeSearch(listas_id)


def delete_listas_cmd(listas_id):
    """
    Construct a command to delete a listas
    :param listas_id: listas's id
    :return: Command
    """
    return DeleteNode(listas_id)

