from odoo import models, fields, api
import datetime 

class Borrowed(models.Model):
    _name = 'library.borrowed'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'borrow_code'

    # status
    state = fields.Selection([('draft', 'Rancangan'), ('ongoing', 'Dipinjam'), ('returned', 'Kembali')], string='Status', default='draft', tracking=True)
    
    # mandatory field
    borrow_code = fields.Char(string="Kode")
    member_id = fields.Many2one(comodel_name='library.anggota', string='Member', required=True, tracking=True)
    book_id = fields.Many2one(comodel_name='library.book', string='Book', required=True, tracking=True)
    borrow_date = fields.Date(default=datetime.date.today(), string='Start', required=True, tracking=True)
    due_date = fields.Date(string='End', required=True, tracking=True)
    librarian = fields.Many2one(comodel_name='res.users', string='Admin', default=lambda self: self.env.user.id, required=True)

    @api.model
    def create(self, vals):
        prefix = "LIB"

        borrow_date = vals.get('borrow_date')
        if borrow_date:
            borrow_date_obj = fields.Date.from_string(borrow_date)
            borrow_date_str = borrow_date_obj.strftime('%Y%m%d')
        else:
            borrow_date_str = ''
        
        last_record = self.env['library.borrowed'].search([], order='borrow_code desc', limit=1)
        last_sequence = 0
        if last_record:
            last_sequence = int(last_record.borrow_code[-3:])
        next_sequence = last_sequence + 1

        code = f'{prefix}/{borrow_date_str}/{next_sequence:03d}'
        vals['borrow_code'] = code

        borrowed = super(Borrowed, self).create(vals)
        return borrowed
    
    def action_dipinjam(self):
        self.state = 'ongoing'

    def action_selesai(self):
        self.state = 'returned'
        self.due_date = datetime.date.today()