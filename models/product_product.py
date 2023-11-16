import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = "product.product"

    vendor_code_ids = fields.One2many('jt.product.vendorcode', 'product_id', string='Vendor codes')

    def _get_vendor_code(self, vendor):
        self.ensure_one()
        if self.vendor_code_ids:
            for vendor_code in self.vendor_code_ids:
                if vendor in vendor_code.vendor_ids:
                    return vendor_code.code
        return None