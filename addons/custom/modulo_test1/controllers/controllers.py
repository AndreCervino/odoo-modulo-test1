# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloTest1(http.Controller):
#     @http.route('/modulo_test1/modulo_test1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_test1/modulo_test1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_test1.listing', {
#             'root': '/modulo_test1/modulo_test1',
#             'objects': http.request.env['modulo_test1.modulo_test1'].search([]),
#         })

#     @http.route('/modulo_test1/modulo_test1/objects/<model("modulo_test1.modulo_test1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_test1.object', {
#             'object': obj
#         })

