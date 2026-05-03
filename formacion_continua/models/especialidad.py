from odoo import models, fields

class Especialidad(models.Model):
    _name = 'formacion.especialidad'
    _description = 'Especialidades de formación'

    name = fields.Char(string="Especialidad", required=True)