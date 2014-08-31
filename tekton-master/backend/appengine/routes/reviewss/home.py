# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from reviews_app import facade
from routes.reviewss import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_reviewss_cmd()
    reviewss = cmd()
    public_form = facade.reviews_public_form()
    reviews_public_dcts = [public_form.fill_with_model(reviews) for reviews in reviewss]
    context = {'reviewss': reviews_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

