# -*- coding: utf-8 -*-

import math

from odoo import models, fields, api

class AccionFormativa(models.Model):
    _name = 'formacion.accion'
    _description = 'Acción Formativa'

    name = fields.Char(string='Nombre del curso', required=True)

    formador_id = fields.Many2one(
        'res.partner',
        string='Formador'
    )

    participante_ids = fields.Many2many(
        'hr.employee',
        string='Participantes'
    )

    horas_totales = fields.Float(string='Horas totales')
    horas_sesion = fields.Float(string='Horas por sesión')

    num_sesiones = fields.Integer(
        string='Número de sesiones',
        compute='_compute_num_sesiones',
        store=True
    )

    fecha_inicio = fields.Datetime(string="Fecha inicio")


    
    @api.depends('horas_totales', 'horas_sesion')
    def _compute_num_sesiones(self):
        for r in self:
            if r.horas_sesion > 0:
                r.num_sesiones = math.ceil(r.horas_totales / r.horas_sesion)
            else:
                r.num_sesiones = 0
                
