from __future__ import absolute_import, unicode_literals
from gaepermission.decorator import login_not_required
from google.appengine.ext import ndb
from tekton.gae.middleware.redirect import RedirectResponse
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton import router
from gaeforms.ndb.form import ModelForm
from routes import appss, reviewss
from routes.appss import admin
from routes.reviewss.form import ReviewForm, Review


@login_not_required
@no_csrf
def index():
    contexto = {'salvar_path': router.to_path(salvar), 'admin_path': router.to_path(admin)}
    return TemplateResponse(contexto)


def salvar(**kwargs):
    app_form = AppForm(**kwargs)
    erros = app_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'errors': erros,
                    'apps': app_form}
        return TemplateResponse(contexto, 'appss/form.html')
    else:
        app = app_form.fill_model()
        app.put()
        return RedirectResponse(router.to_path(appss))


class App(ndb.Model):
    nome = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required=True)
    avaliacao = ndb.FloatProperty(required=True)
    descricao = ndb.StringProperty()
    deleted = ndb.IntegerProperty(required=False, default=0)


class AppForm(ModelForm):
    _model_class = App
    _include = [App.nome, App.link, App.avaliacao, App.descricao, App.deleted]
    # _exclude = [User.nome]
    #nome=base.StringProperty(required=True) #base.Form


@no_csrf
def edit_form(app_id):
    app_id = int(app_id)
    app = App.get_by_id(app_id)
    app_form = AppForm()
    app_form.fill_with_model(app)
    contexto = {'salvar_path': router.to_path(editar, app_id),
                'apps': app_form,
                'admin_path': router.to_path(admin)}
    return TemplateResponse(contexto, 'appss/form.html')


def editar(app_id, **kwargs):
    app_id = int(app_id)
    app = App.get_by_id(app_id)
    app_form = AppForm(**kwargs)
    erros = app_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'errors': erros,
                    'apps': app_form}
        return TemplateResponse(contexto, 'appss/form.html')
    else:
        app_form.fill_model(app)
        app.put()
        return RedirectResponse(router.to_path(appss))

@login_not_required
@no_csrf
def deletar(app_id):
    app_id = int(app_id)
    app = App.get_by_id(app_id)
    app.deleted = 1
    app.put()


