# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


class ProfesseurClass(models.Model):
    _name = 'school.absence'
    _description = 'table des professeurs'

    session_id = fields.Many2one('school.session', string='Seance')
    date_absence = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(4, 2), help="Durée dans un jour")
    student_ids = fields.Many2many('school.student', string='Etudiants absent')
    professeur_id = fields.Many2one('school.professeur', string='Professeur')

