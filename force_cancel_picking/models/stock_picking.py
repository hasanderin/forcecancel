from odoo import models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_force_cancel(self):
        for picking in self:
            # Tüm hareketleri force ile iptal et
            for move in picking.move_lines:
                if move.state not in ('cancel',):
                    try:
                        move._action_cancel()
                    except Exception:
                        # Hata olursa state'i doğrudan cancel yap
                        move.state = 'cancel'
            picking.state = 'cancel' 