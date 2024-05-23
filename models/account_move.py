from odoo import fields, models,api




class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.constrains('ref', 'move_type', 'partner_id', 'journal_id', 'invoice_date')
    def _check_duplicate_supplier_reference(self):
        pass

        




