# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NotesClass(models.Model):
    _name = 'school.note'
    _description = 'table des notes'

    student_id = fields.Many2one('school.student', string="nom de l'étudiant", required=True)
    cours_id = fields.Many2one('school.course', string="nom du cours", required=True)
    professeur_id = fields.Many2one('school.professeur', string="nom du professeur", required=True)
    note = fields.Float( digits=(5, 3), string="La note")
    departement_id = fields.Many2one('school.departement',string="Departement")
    filiere_id = fields.Many2one('school.filiere', string="nom de la filiere", required=True)





