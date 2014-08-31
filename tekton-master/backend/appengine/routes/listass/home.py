# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from listas_app import facade
from routes.listass import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_listass_cmd()
    listass = cmd()
    public_form = facade.listas_public_form()
    listas_public_dcts = [public_form.fill_with_model(listas) for listas in listass]
    context = {'listass': listas_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

