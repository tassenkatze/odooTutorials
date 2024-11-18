from odoo import fields, models

class PropertyType(models.Model):
    _name = "property.type"

    name = fields.Char(required=True)

class ProperyTags(models.Model):
    _name = "property.tags"

    name = fields.Char(required=True)