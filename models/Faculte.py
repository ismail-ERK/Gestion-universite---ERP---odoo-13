# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FaculteClass(models.Model):
    _name = 'school.faculte'
    _description = 'table des facultes'

    name = fields.Char(string="nom de la faculte", required=True)
    email = fields.Char(string="Boite electronique de la faculte")
    adresse = fields.Text(string="Adresse de la faculte")
    tel = fields.Char(string="Numero d telephone de la faculte")
    student_ids = fields.One2many('school.student',
                                  'faculte_id',
                                  string="Students")
    departement_ids = fields.One2many('school.departement',
                                      'faculte_id',
                                      string="Departements")
    courses_ids = fields.Many2many('school.course', string="Cours")
    filiere_ids = fields.Many2many('school.filiere', string="Filieres")
    image = fields.Binary(string="Son image")
    # absences_ids = fields.One2many('school.absence',
    #                                'professeur_id',
    #                                string='absence')





