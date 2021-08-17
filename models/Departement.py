# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FaculteClass(models.Model):
    _name = 'school.departement'
    _inherit = 'mail.thread'
    _description = 'table des departements'

    name = fields.Char(string="nom de la departement", required=True)
    email = fields.Char(string="Boite electronique de la departement")
    tel = fields.Char(string="Numero d telephone de la departement")
    image = fields.Binary(string="Son image")
    Chef_Departement = fields.Many2one('school.professeur', string="Chef de departement")
    faculte_id = fields.Many2one('school.faculte', string="nom de la Faculte")
    student_ids = fields.One2many('school.student',
                                  'departement_id',
                                  string="Students")
    courses_ids = fields.One2many('school.course',
                                  'departement_id',
                                  string="Courses")
    filiere_ids = fields.One2many('school.filiere',
                                  'departement_id',
                                  string="Filieres")
    professeur_ids = fields.One2many('school.professeur',
                                  'departement_id',
                                  string="Professieurs")
