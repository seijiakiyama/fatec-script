# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from apps_app import facade


def index():
    cmd = facade.list_appss_cmd()
    apps_list = cmd()
    short_form=facade.apps_short_form()
    apps_short = [short_form.fill_with_model(m) for m in apps_list]
    return JsonResponse(apps_short)


def save(**apps_properties):
    cmd = facade.save_apps_cmd(**apps_properties)
    return _save_or_update_json_response(cmd)


def update(apps_id, **apps_properties):
    cmd = facade.update_apps_cmd(apps_id, **apps_properties)
    return _save_or_update_json_response(cmd)


def delete(apps_id):
    facade.delete_apps_cmd(apps_id)()


def _save_or_update_json_response(cmd):
    try:
        apps = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.apps_short_form()
    return JsonResponse(short_form.fill_with_model(apps))

