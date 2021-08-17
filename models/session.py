from datetime import timedelta

from odoo import models, fields, api, exceptions

from odoo.exceptions import UserError


class SessionClass(models.Model):
    _name = 'school.session'
    _description = 'session table'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(3, 1), help="Durée dans un jour")
    seats = fields.Integer(string="number of seats")
    filiere_id = fields.Many2one('school.filiere', string='Filiere')
    faculte_id = fields.Many2one('school.faculte', string="Sa Faculte", required=True)

    course_id = fields.Many2one('school.course',
                                ondelete='cascade', string="Cours", required=True)
    attendee_ids = fields.Many2many('school.student', string="Etudiant")
    taken_seats = fields.Float(string='Places sont prises', compute='_taken_seats')
    absences = fields.One2many('school.absence',
                               'session_id',
                               string="Absences")
    departement_id = fields.Many2one('school.departement', string="Departement")
    absences = fields.One2many('school.absence',
                               'session_id',
                               string="Absences")
    attendees_count = fields.Integer(string="Nombre des étudiants", compute="_get_attendees_count", store=True)
    color = fields.Integer()

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                test_taken_seats = 100 * len(r.attendee_ids) / r.seats
                if test_taken_seats > 100:
                    raise UserError('La session est paleine!')
                else:
                    r.taken_seats = test_taken_seats

                # declance est stop le traitement
            # if r.taken_seats > 100:
            #     raise UserError('La session est paleine!')
            # declance mais ne stop pas le traitement

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Le nombre des places est incorrect !",
                    'message': "Le nombre des placesne peut pas être négatif !",
                },
            }

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)
