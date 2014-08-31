# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from listas_app import facade
from routes.listass import admin


@no_csrf
def index(listas_id):
    listas = facade.get_listas_cmd(listas_id)()
    detail_form = facade.listas_detail_form()
    context = {'save_path': router.to_path(save, listas_id), 'listas': detail_form.fill_with_model(listas)}
    return TemplateResponse(context, 'listass/admin/form.html')


def save(_handler, listas_id, **listas_properties):
    cmd = facade.update_listas_cmd(listas_id, **listas_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'listas': cmd.form}

        return TemplateResponse(context, 'listass/admin/form.html')
    _handler.redirect(router.to_path(admin))

