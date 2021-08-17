# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ParentClass(models.Model):
    _name = 'school.parent'
    _inherit = 'mail.thread'
    _description = 'table des parent'

    name = fields.Char(string="nom du parent", required=True)
    email = fields.Char(string="Boite éléctronique du parent")
    adresse = fields.Text(string="Adresse student")
    tel = fields.Char(string="Numero du telephone parent")
    date_naissance = fields.Date(string="Date de naissance")
    fils_ids = fields.Many2many('school.student', string='Fils')
    image = fields.Binary(string="Son image")
