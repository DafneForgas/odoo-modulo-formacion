# -*- coding: utf-8 -*-
{
    'name': "Formación Continua",

    'summary': "Gestión de cursos",

    'description':"Módulo para controlar la formación continua de los trabajadores",

    'author': "Dafne Forgas",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    
'depends': ['base', 'hr'],

    'installable': True,
    'application': True,

'data': [
    'security/formacion_security.xml',
    'security/ir.model.access.csv',
    'views/accion_formativa_views.xml',
    'views/res_partner_views.xml',
    'views/hr_employee_views.xml',
    'views/menu.xml',
],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

