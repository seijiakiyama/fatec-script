# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from apps_app.commands import ListappsCommand, SaveappsCommand, UpdateappsCommand, \
    appsPublicForm, appsDetailForm, appsShortForm


def save_apps_cmd(**apps_properties):
    """
    Command to save apps entity
    :param apps_properties: a dict of properties to save on model
    :return: a Command that save apps, validating and localizing properties received as strings
    """
    return SaveappsCommand(**apps_properties)


def update_apps_cmd(apps_id, **apps_properties):
    """
    Command to update apps entity with id equals 'apps_id'
    :param apps_properties: a dict of properties to update model
    :return: a Command that update apps, validating and localizing properties received as strings
    """
    return UpdateappsCommand(apps_id, **apps_properties)


def list_appss_cmd():
    """
    Command to list apps entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListappsCommand()


def apps_detail_form(**kwargs):
    """
    Function to get apps's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return appsDetailForm(**kwargs)


def apps_short_form(**kwargs):
    """
    Function to get apps's short form. just a subset of apps's properties
    :param kwargs: form properties
    :return: Form
    """
    return appsShortForm(**kwargs)

def apps_public_form(**kwargs):
    """
    Function to get apps'spublic form. just a subset of apps's properties
    :param kwargs: form properties
    :return: Form
    """
    return appsPublicForm(**kwargs)


def get_apps_cmd(apps_id):
    """
    Find apps by her id
    :param apps_id: the apps id
    :return: Command
    """
    return NodeSearch(apps_id)


def delete_apps_cmd(apps_id):
    """
    Construct a command to delete a apps
    :param apps_id: apps's id
    :return: Command
    """
    return DeleteNode(apps_id)

