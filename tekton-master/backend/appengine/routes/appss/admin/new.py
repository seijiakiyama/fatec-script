# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from apps_app import facade
from routes.appss import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'appss/admin/form.html')


def save(_handler, apps_id=None, **apps_properties):
    cmd = facade.save_apps_cmd(**apps_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'apps': cmd.form}

        return TemplateResponse(context, 'appss/admin/form.html')
    _handler.redirect(router.to_path(admin))

