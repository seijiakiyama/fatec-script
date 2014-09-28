from __future__ import absolute_import, unicode_literals
from gaepermission.decorator import login_not_required
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from tekton import router


@login_not_required
@no_csrf
def index():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


@login_not_required
@no_csrf
def salvar(_resp, **kwargs):
    app_form = AppForm(**kwargs)
    errors = app_form.validate()
    if errors:
        contexto = {'salvar_path': router.to_path(salvar),
                    'errors': errors,
                    'app': app_form}
        return TemplateResponse(contexto, 'appss/form.html')
    else:
        campos = app_form.normalize()
        user = App(**campos)
        user.put()
        _resp.write(kwargs)


class App(ndb.Model):
    nome = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required=True)
    avaliacao = ndb.FloatProperty(required=True)
    descricao = ndb.StringProperty(required=True)


class AppForm(ModelForm):
    _model_class = App
    _include = [App.nome, App.link, App.avaliacao, App.descricao]
    #_exclude = [User.nome]
    #nome=base.StringProperty(required=True) #base.Form