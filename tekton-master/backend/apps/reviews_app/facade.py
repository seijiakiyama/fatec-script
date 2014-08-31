# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from reviews_app.commands import ListreviewsCommand, SavereviewsCommand, UpdatereviewsCommand, \
    reviewsPublicForm, reviewsDetailForm, reviewsShortForm


def save_reviews_cmd(**reviews_properties):
    """
    Command to save reviews entity
    :param reviews_properties: a dict of properties to save on model
    :return: a Command that save reviews, validating and localizing properties received as strings
    """
    return SavereviewsCommand(**reviews_properties)


def update_reviews_cmd(reviews_id, **reviews_properties):
    """
    Command to update reviews entity with id equals 'reviews_id'
    :param reviews_properties: a dict of properties to update model
    :return: a Command that update reviews, validating and localizing properties received as strings
    """
    return UpdatereviewsCommand(reviews_id, **reviews_properties)


def list_reviewss_cmd():
    """
    Command to list reviews entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListreviewsCommand()


def reviews_detail_form(**kwargs):
    """
    Function to get reviews's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return reviewsDetailForm(**kwargs)


def reviews_short_form(**kwargs):
    """
    Function to get reviews's short form. just a subset of reviews's properties
    :param kwargs: form properties
    :return: Form
    """
    return reviewsShortForm(**kwargs)

def reviews_public_form(**kwargs):
    """
    Function to get reviews'spublic form. just a subset of reviews's properties
    :param kwargs: form properties
    :return: Form
    """
    return reviewsPublicForm(**kwargs)


def get_reviews_cmd(reviews_id):
    """
    Find reviews by her id
    :param reviews_id: the reviews id
    :return: Command
    """
    return NodeSearch(reviews_id)


def delete_reviews_cmd(reviews_id):
    """
    Construct a command to delete a reviews
    :param reviews_id: reviews's id
    :return: Command
    """
    return DeleteNode(reviews_id)

