# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from listas_app import facade
from routes.listass.admin import new, edit


def delete(_handler, listas_id):
    facade.delete_listas_cmd(listas_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_listass_cmd()
    listass = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.listas_short_form()

    def short_listas_dict(listas):
        listas_dct = short_form.fill_with_model(listas)
        listas_dct['edit_path'] = router.to_path(edit_path, listas_dct['id'])
        listas_dct['delete_path'] = router.to_path(delete_path, listas_dct['id'])
        return listas_dct

    short_listass = [short_listas_dict(listas) for listas in listass]
    context = {'listass': short_listass,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

