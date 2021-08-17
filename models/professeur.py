# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProfesseurClass(models.Model):
    _name = 'school.professeur'
    _description = 'table des professeurs'

    name = fields.Char(string="nom du professeur", required=True)
    email = fields.Char(string="Boite electronique")
    adresse = fields.Text(string="Adresse student")
    tel = fields.Char(string="Numero du telephone professeur")
    date_naissance = fields.Date(string="Date de naissance")
    courses_ids = fields.Many2many('school.course', string="Son courses")
    filiere_id = fields.Many2one('school.filiere', string="Sa Filiere")
    faculte_id = fields.Many2one('school.faculte', string="Sa Faculte")
    departement_id = fields.Many2one('school.departement',string="Departement")
    image = fields.Binary(string="His image")
    # absences_ids = fields.One2many('school.absence',
    #                                'professeur_id',
    #                                string='absence')





