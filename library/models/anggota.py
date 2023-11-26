from odoo import models, fields, api

class Member(models.Model):
    _name = 'library.anggota'
    _rec_name ='name'

    name = fields.Char(string="Nama", required=True)
    nis = fields.Char(string='NIS', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', required=True)
    class_id = fields.Many2one(comodel_name='library.kelas', string='Class', required=True)
    borrow_ids = fields.One2many(comodel_name='library.borrowed', inverse_name='member_id', string="Peminjaman")
    return_ids = fields.One2many(comodel_name='library.returned', inverse_name='member_id', string="Pengembalian")