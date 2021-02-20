# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class colectaCategory(models.Model):
    _name = 'recolecta.colecta.category'

    _parent_store = True
    _parent_name = "parent_id"  # optional if field is 'parent_id'

    name = fields.Char('Category')
    description = fields.Text('Description')
    parent_id = fields.Many2one(
        'recolecta.colecta.category',
        string='Parent Category',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'recolecta.colecta.category', 'parent_id',
        string='Child Categories')
    parent_path = fields.Char(index=True)

    colecta_ids = fields.One2many('recolecta.colecta', 'category_id', 'colectas')

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive categories.')