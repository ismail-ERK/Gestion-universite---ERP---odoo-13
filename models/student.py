from odoo import models, fields, api


class StudentClass(models.Model):
    _name = 'school.student'
    _inherit = 'mail.thread'
    _description = 'student table'

    name = fields.Char(string="Nom de l'étudiant", required=True)
    email = fields.Char(string="Email de l'étudiant")
    adresse = fields.Text(string="Adresse de l'étudiant")
    tel = fields.Char(string="Numero du telephone de l'étudiant")
    description = fields.Text(string="Description")
    courses_ids = fields.Many2many('school.course', string="His courses")
    image = fields.Binary(string="Son image")
    parent_ids = fields.Many2many('school.parent', string="Parents")
    filieres_id = fields.Many2one('school.filiere', string="Filiere")
    note_f = fields.Float(digits=(4, 2), compute='_get_note', string="Note Finale")
    faculte_id = fields.Many2one('school.faculte', string="Sa Faculte")
    departement_id = fields.Many2one('school.departement',string="Departement")
    absence_ids = fields.Many2many('school.absence', string="Absences")
    note_ids = fields.One2many('school.note',
                               'student_id',
                               string="Notes")

    def print_check(self, cr, uid, ids, context=None):
        if not ids:
            return {}
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'account.check.print',
            'datas': {
                'model': 'school.student',
                'id': ids and ids[0] or False,
                'ids': ids and ids or [],
                'report_type': 'webkit'
            },
            'nodestroy': True
        }

    @api.depends('note_ids')
    def _get_note(self):
        count = 0
        for r in self:
            for l in r.note_ids:
                count = count + l.note
        if len(r.note_ids) == 0:
            r.note_f = 0
        else:
            r.note_f = count / len(r.note_ids)


    def send_mail_student(self):
        self.ensure_one()
        template_id = self.env.ref("gestiond'ecole.email_template_student").id
        ctx = {
            'default_model': 'school.student',
            'default_res_id': self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'email_to': self.email,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }






