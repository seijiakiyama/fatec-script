# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from reviews_app import facade
from routes.reviewss.admin import new, edit


def delete(_handler, reviews_id):
    facade.delete_reviews_cmd(reviews_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_reviewss_cmd()
    reviewss = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.reviews_short_form()

    def short_reviews_dict(reviews):
        reviews_dct = short_form.fill_with_model(reviews)
        reviews_dct['edit_path'] = router.to_path(edit_path, reviews_dct['id'])
        reviews_dct['delete_path'] = router.to_path(delete_path, reviews_dct['id'])
        return reviews_dct

    short_reviewss = [short_reviews_dict(reviews) for reviews in reviewss]
    context = {'reviewss': short_reviewss,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

