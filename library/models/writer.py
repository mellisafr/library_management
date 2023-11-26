from odoo import models, fields, api

class Writer(models.Model):
    _name = 'library.writer'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    book_ids = fields.One2many(comodel_name='library.book', inverse_name='writer_id', string='List of Book')