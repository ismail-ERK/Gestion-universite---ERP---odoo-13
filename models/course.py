from odoo import models, fields, api


class CourseClass(models.Model):
    _name = 'school.course'
    _inherit = 'mail.thread'
    _description = 'course table'

    name = fields.Char(string="nom du cours", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('school.professeur',
                                     ondelete='set null', string="Responsable", index=True)
    session_ids = fields.One2many('school.session',
                                  'course_id',
                                  string="Sessions")
    filiere_ids = fields.Many2many('school.filiere', string="Filiere")
    student_ids = fields.Many2many('school.student', string="Notes")
    faculte_id = fields.Many2one('school.faculte', string="Sa Faculte")
    departement_id = fields.Many2one('school.departement', string="Departement")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "Le nom doit pas être la description du cours",),
        ('name_unisue',
         'UNIQUE(name)',
         "Le nom doit être unique",),

    ]

    # sql constaint chaque contrainte prend trois lignes
    # 1) le nom de la contarainte
    # 2) sql
    # 3) le contenu du message d'erreur
