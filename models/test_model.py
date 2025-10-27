from odoo import models, fields

class TestAppStoreModel(models.Model):
    _name = 'test.appstore.model'
    _description = 'Modelo de prueba para Odoo App Store'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string='Activo', default=True)
