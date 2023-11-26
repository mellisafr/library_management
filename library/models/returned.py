from odoo import models, fields, api
from datetime import datetime

class Returned(models.Model):
    _name = 'library.returned'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'borrow_id'

    # status
    state = fields.Selection([('draft', 'Rancangan'), ('returned', 'Kembali')], string='Status', default='draft', Tracking=True)
    
    # mandatory field
    borrow_id = fields.Many2one(comodel_name='library.borrowed', string='Borrow Id', Tracking=True)
    return_date = fields.Date(string='Return Date', Tracking=True)
    librarian = fields.Many2one(comodel_name='res.users', string='Admin', default=lambda self: self.env.user.id, required=True)
    book_id = fields.Many2one(comodel_name='library.book', string='Book', required=True)
    member_id = fields.Many2one(comodel_name='library.anggota', string='Member')
    borrow_date = fields.Date(string='Start', required=True)
    due_date = fields.Date(string='End', required=True)
    duration = fields.Integer(compute='_compute_duration', string='Durasi (hari)', store=True)

    def action_selesai(self):
        self.state = 'returned'
        self.borrow_id.state = 'returned'
    
    @api.onchange('borrow_id')
    def set_email(self):
        for record in self :
            record.member_id = record.borrow_id.member_id
            record.book_id = record.borrow_id.book_id
            record.borrow_date = record.borrow_id.borrow_date
            record.due_date = record.borrow_id.due_date
    
    @api.depends('borrow_date', 'return_date')
    def _compute_duration(self):
        for record in self:
            if record.borrow_date and record.return_date:
                borrow_date = record.borrow_date
                return_date = record.return_date
                duration = (return_date - borrow_date).days
                record.duration = duration
        


