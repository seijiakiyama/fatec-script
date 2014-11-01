# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.reviewss import admin
from routes.reviewss.form import edit_form, ReviewForm, Review, deletar, teleportToReview


@login_not_required
@no_csrf
def index():
    query = Review.query(Review.deleted != 1)
    # cmd = facade.list_appss_cmd()
    reviewss = query.fetch()
    public_form = ReviewForm()
    reviewss = [public_form.fill_with_model(reviews) for reviews in reviewss]
    editar_form_path = router.to_path(edit_form)
    for review in reviewss:
        review['edit_path'] = '%s/%s'%(editar_form_path, review['id'])
    deletar_form_path = router.to_path(deletar)
    for review in reviewss:
        review['delete_path'] = '%s/%s'%(deletar_form_path, review['id'])
    context = {'reviewss': reviewss,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

@no_csrf
def show_review(app_id):
    query = Review.query(Review.deleted != 1, Review.app == app_id)
    # cmd = facade.list_appss_cmd()
    reviewss = query.fetch()
    public_form = ReviewForm()
    reviewss = [public_form.fill_with_model(reviews) for reviews in reviewss]
    editar_form_path = router.to_path(edit_form)
    deletar_form_path = router.to_path(deletar)
    for review in reviewss:
        review['edit_path'] = '%s/%s'%(editar_form_path, review['id'])
        review['delete_path'] = '%s/%s'%(deletar_form_path, review['id'])
    context = {'reviewss': reviewss,'admin_path':router.to_path(admin), 'criar_review_path':router.to_path(teleportToReview, app_id)}
    return TemplateResponse(context, 'reviewss/home.html')