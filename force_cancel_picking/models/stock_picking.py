from odoo import models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_force_cancel(self):
        for picking in self:
            if picking.state in ['done', 'assigned']:
                picking.move_lines._action_cancel()
                picking.state = 'cancel' 