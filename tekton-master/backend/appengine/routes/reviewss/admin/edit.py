# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from reviews_app import facade
from routes.reviewss import admin


@no_csrf
def index(reviews_id):
    reviews = facade.get_reviews_cmd(reviews_id)()
    detail_form = facade.reviews_detail_form()
    context = {'save_path': router.to_path(save, reviews_id), 'reviews': detail_form.fill_with_model(reviews)}
    return TemplateResponse(context, 'reviewss/admin/form.html')


def save(_handler, reviews_id, **reviews_properties):
    cmd = facade.update_reviews_cmd(reviews_id, **reviews_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'reviews': cmd.form}

        return TemplateResponse(context, 'reviewss/admin/form.html')
    _handler.redirect(router.to_path(admin))

