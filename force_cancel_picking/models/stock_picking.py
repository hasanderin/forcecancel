from odoo import models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_force_cancel(self):
        for picking in self:
            if picking.state in ['done', 'assigned']:
                # Hareketleri de zorla iptal et
                moves = picking.move_lines | picking.move_line_ids
                moves._action_cancel()
                picking.state = 'cancel' 