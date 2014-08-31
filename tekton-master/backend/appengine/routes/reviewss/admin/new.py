# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from reviews_app import facade
from routes.reviewss import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'reviewss/admin/form.html')


def save(_handler, reviews_id=None, **reviews_properties):
    cmd = facade.save_reviews_cmd(**reviews_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'reviews': cmd.form}

        return TemplateResponse(context, 'reviewss/admin/form.html')
    _handler.redirect(router.to_path(admin))

