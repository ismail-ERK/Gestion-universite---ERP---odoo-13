# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FiliereClass(models.Model):
    _name = 'school.filiere'
    _description = 'table des filieres'

    name = fields.Char(string="nom de la filiere", required=True)
    responsable_id = fields.Many2one('school.professeur', string="Responsable")
    course_ids = fields.Many2many('school.course', string='courses')
    student_ids = fields.One2many('school.student',
                                  'filieres_id',
                                  string='Students')
    faculte_id = fields.Many2one('school.faculte', string="Sa Faculte")
    departement_id = fields.Many2one('school.departement',string="Departement")
    session_ids = fields.One2many('school.session',
                                  'filiere_id',
                                  string='Students')
