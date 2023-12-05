import logging
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)

class ProductVendorCode(models.Model):
    _name = 'jt.product.vendorcode'
    _description = 'Product Vendorcode'
    _order = 'sequence, code'

    sequence = fields.Integer(
        'Sequence', default=1,
        help="Gives the sequence order when displaying.")
    
    code = fields.Char('code', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    vendor_ids = fields.Many2many('res.partner', string='Vendors', required=True)