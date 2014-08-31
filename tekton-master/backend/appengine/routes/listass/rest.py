# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from listas_app import facade


def index():
    cmd = facade.list_listass_cmd()
    listas_list = cmd()
    short_form=facade.listas_short_form()
    listas_short = [short_form.fill_with_model(m) for m in listas_list]
    return JsonResponse(listas_short)


def save(**listas_properties):
    cmd = facade.save_listas_cmd(**listas_properties)
    return _save_or_update_json_response(cmd)


def update(listas_id, **listas_properties):
    cmd = facade.update_listas_cmd(listas_id, **listas_properties)
    return _save_or_update_json_response(cmd)


def delete(listas_id):
    facade.delete_listas_cmd(listas_id)()


def _save_or_update_json_response(cmd):
    try:
        listas = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.listas_short_form()
    return JsonResponse(short_form.fill_with_model(listas))

