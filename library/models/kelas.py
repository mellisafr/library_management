from odoo import fields, models, api


class Kelas(models.Model):
    _name = 'library.kelas'
    _rec_name = 'name'

    name = fields.Char(string="Kelas", required=True)
    member_ids = fields.One2many(comodel_name="library.anggota", inverse_name="class_id", string="Anggota")

