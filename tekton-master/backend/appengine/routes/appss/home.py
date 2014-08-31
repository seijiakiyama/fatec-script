# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from apps_app import facade
from routes.appss import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_appss_cmd()
    appss = cmd()
    public_form = facade.apps_public_form()
    apps_public_dcts = [public_form.fill_with_model(apps) for apps in appss]
    context = {'appss': apps_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

