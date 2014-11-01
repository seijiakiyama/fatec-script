# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from apps_app import facade
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.appss.form import AppForm, App, deletar


@no_csrf
@login_not_required
def index():
    query = App.query(App.deleted != 1)
    apps_list = query.fetch()
    short_form=AppForm()
    apps_short = [short_form.fill_with_model(m) for m in apps_list]
    return JsonUnsecureResponse(apps_short)

@login_not_required
@no_csrf
def save(_resp, **apps_properties):
    app_form = AppForm(**apps_properties)
    erros = app_form.validate()
    if erros:
        _resp.status_code = 500
        return JsonUnsecureResponse({'errors': erros})
    else:
        app = app_form.fill_model()
        app.put()
        short_form = AppForm()
        return JsonUnsecureResponse(short_form.fill_with_model(app))
    # cmd = facade.save_apps_cmd(**apps_properties)
    # return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def update(_resp, apps_id, **apps_properties):
    cmd = facade.update_apps_cmd(apps_id, **apps_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def delete(**properties):
    deletar(properties['app_id'])

def _save_or_update_json_response(_resp, cmd):
    try:
        apps = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonUnsecureResponse({'errors': cmd.errors})
    short_form=AppForm()
    return JsonUnsecureResponse(short_form.fill_with_model(apps))

