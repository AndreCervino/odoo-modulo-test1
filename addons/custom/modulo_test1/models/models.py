# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modulo_test1(models.Model):
#     _name = 'modulo_test1.modulo_test1'
#     _description = 'modulo_test1.modulo_test1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields

class Tarea(models.Model):
    _name = 'modulo_test1.tarea'
    _description = 'Tarea de Agenda'

    name = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha')
    realizada = fields.Boolean(string='Realizada', default=False)