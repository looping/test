#coding: utf-8
from bottle import route, view, request, template
import c
@route('/')
def root():
	return c.root()
