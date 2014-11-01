from __future__ import absolute_import, unicode_literals
from gaepermission.decorator import login_not_required
from google.appengine.ext import ndb
from tekton.gae.middleware.redirect import RedirectResponse
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton import router
from gaeforms.ndb.form import ModelForm
from routes import reviewss
from routes.appss import admin


@login_not_required
@no_csrf
def index():
    contexto = {'salvar_path': router.to_path(salvar), 'admin_path': router.to_path(admin)}
    return TemplateResponse(contexto)

def salvar(_resp, **kwargs):
    review_form = ReviewForm(**kwargs)
    erros = review_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'errors': erros,
                    'reviews': review_form}
        return TemplateResponse(contexto, 'reviewss/form.html')
    else:
        review = review_form.fill_model()
        review.put()
        return RedirectResponse(router.to_path(reviewss))

class Review(ndb.Model):
    app = ndb.StringProperty(required=True)
    nota = ndb.IntegerProperty(required=True)
    descricao = ndb.StringProperty(required=True)
    deleted = ndb.IntegerProperty(required=False, default=0)


class ReviewForm(ModelForm):
    _include = [Review.app, Review.nota, Review.descricao]
    _model_class = Review
    ##_exclude = []
    #nome=base.StringProperty(required=True) #base.Form

@no_csrf
def edit_form(review_id):
    review_id = int(review_id)
    review = Review.get_by_id(review_id)
    review_form = ReviewForm()
    review_form.fill_with_model(review)
    contexto = {'salvar_path': router.to_path(editar, review_id),
                'reviews': review_form,
                'admin_path': router.to_path(admin)}
    return TemplateResponse(contexto, 'reviewss/form.html')

def editar(review_id, **kwargs):
    review_id = int(review_id)
    review = Review.get_by_id(review_id)
    review_form = ReviewForm(**kwargs)
    erros = review_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'errors': erros,
                    'reviews': review_form}
        return TemplateResponse(contexto, 'reviewss/form.html')
    else:
        review_form.fill_model(review)
        review.put()
        return RedirectResponse(router.to_path(reviewss))

@no_csrf
def deletar(review_id, **kwargs):
    review_id = int(review_id)
    review = Review.get_by_id(review_id)
    review.deleted = 1
    review.put()
    return RedirectResponse(router.to_path(reviewss))

@no_csrf
def teleportToReview(app_id, **kwargs):
    review_form = ReviewForm()
    review = Review()
    review.app = app_id
    review_form.fill_with_model(review)
    contexto = {'salvar_path': router.to_path(reviewss.form.salvar),
                'reviews': review_form,
                'admin_path': router.to_path(admin)}
    return TemplateResponse(contexto, 'reviewss/form.html')