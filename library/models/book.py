from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _rec_name = 'name'

    no_inventaris = fields.Char(string='No Inventaris', required=True)
    name = fields.Char(string='Nama Buku', required=True)
    writer_id = fields.Many2many(comodel_name='library.writer', string='Penulis', required=True)
    publish_year = fields.Char(string='Tahun Terbit', required=True)
    publisher_id = fields.Many2one(comodel_name='library.publisher', string='Penerbit', required=True)
    isbn = fields.Char(string='ISBN', required=True)
    borrow_ids = fields.One2many(comodel_name="library.borrowed", inverse_name="book_id", string="Peminjaman")
    return_ids = fields.One2many(comodel_name="library.returned", inverse_name="book_id", string="Pengembalian")
