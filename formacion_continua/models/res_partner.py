from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    es_formador = fields.Boolean(string="Es formador")

    especialidad_id = fields.Many2one(
        'formacion.especialidad',
        string="Especialidad"
    )