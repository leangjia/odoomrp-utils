# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    is_package = fields.Boolean(string='Is package')
