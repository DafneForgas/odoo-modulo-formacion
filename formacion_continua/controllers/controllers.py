# -*- coding: utf-8 -*-
# from odoo import http


# class FormacionContinua(http.Controller):
#     @http.route('/formacion_continua/formacion_continua', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formacion_continua/formacion_continua/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('formacion_continua.listing', {
#             'root': '/formacion_continua/formacion_continua',
#             'objects': http.request.env['formacion_continua.formacion_continua'].search([]),
#         })

#     @http.route('/formacion_continua/formacion_continua/objects/<model("formacion_continua.formacion_continua"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formacion_continua.object', {
#             'object': obj
#         })

