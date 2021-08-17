# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'school2',
    'version': '1.1',
    'category': 'Accounting/Accounting',
    'depends': ['base', 'mail'],
    'description': """
Module for defining management school.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/Faculte.xml',
        'views/StudentView.xml',
        'views/SessionView.xml',
        'views/CourseView.xml',
        'views/PartnerView.xml',
        'views/Professeur.xml',
        'views/Absence.xml',
        'views/Parent.xml',
        'views/Filiere.xml',
        'views/Notes.xml',
        'views/Departement.xml',
        'reports/session_report.xml',
        'reports/student_report.xml',
        'reports/mail_template.xml',
    ],
    'demo': [
        'demo.xml',
    ],
    'author': 'ismailERK',
    'installable': True,
    'auto_install': False,
    'application': True,
}
