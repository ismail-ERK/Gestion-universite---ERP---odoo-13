from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    # instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('school.session',
                                   string="Attended Sessions")
