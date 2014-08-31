# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class reviews(Node):
    app = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required=True)
    nota = ndb.IntegerProperty(required=True)
    descricao = ndb.StringProperty(required=True)

