# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.appss import admin
from routes.appss.form import edit_form, AppForm, deletar, App
from routes.reviewss.home import show_review


@login_not_required
@no_csrf
def index():
    query = App.query(App.deleted != 1)
    # cmd = facade.list_appss_cmd()
    appss = query.fetch()
    public_form = AppForm()
    appss = [public_form.fill_with_model(apps) for apps in appss]
    editar_form_path = router.to_path(edit_form)
    deletar_form_path = router.to_path(deletar)
    ver_review_path = router.to_path(show_review) ##router.to_path(teleportToReview)
    for app in appss:
        app['edit_path'] = '%s/%s'%(editar_form_path, app['id'])
        app['delete_path'] = '%s/%s'%(deletar_form_path, app['id'])
        app['review_path'] = '%s/%s'%(ver_review_path, app['id'])
    context = {'appss': appss, 'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

