# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from reviews_app import facade


def index():
    cmd = facade.list_reviewss_cmd()
    reviews_list = cmd()
    short_form=facade.reviews_short_form()
    reviews_short = [short_form.fill_with_model(m) for m in reviews_list]
    return JsonResponse(reviews_short)


def save(**reviews_properties):
    cmd = facade.save_reviews_cmd(**reviews_properties)
    return _save_or_update_json_response(cmd)


def update(reviews_id, **reviews_properties):
    cmd = facade.update_reviews_cmd(reviews_id, **reviews_properties)
    return _save_or_update_json_response(cmd)


def delete(reviews_id):
    facade.delete_reviews_cmd(reviews_id)()


def _save_or_update_json_response(cmd):
    try:
        reviews = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.reviews_short_form()
    return JsonResponse(short_form.fill_with_model(reviews))

