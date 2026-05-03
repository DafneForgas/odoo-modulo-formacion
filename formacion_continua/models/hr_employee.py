from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    formacion_ids = fields.Many2many(
        'formacion.accion',
        string="Acciones formativas"
    )
    
