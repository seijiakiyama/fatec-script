# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from apps_app import facade
from routes.appss.admin import new, edit


def delete(_handler, apps_id):
    facade.delete_apps_cmd(apps_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_appss_cmd()
    appss = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.apps_short_form()

    def short_apps_dict(apps):
        apps_dct = short_form.fill_with_model(apps)
        apps_dct['edit_path'] = router.to_path(edit_path, apps_dct['id'])
        apps_dct['delete_path'] = router.to_path(delete_path, apps_dct['id'])
        return apps_dct

    short_appss = [short_apps_dict(apps) for apps in appss]
    context = {'appss': short_appss,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

