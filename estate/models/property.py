from odoo import fields, models

class PropertyType(models.Model):
    _name = "property.type"
    _description = "Types of properties"

    name = fields.Char(required=True)

class ProperyTags(models.Model):
    _name = "property.tags"
    _description = "Tags for properties"

    name = fields.Char(required=True)

class PropertyOffer(models.Model):
    _name = "property.offer"
    _description = "Offers for properties"

    price = fields.Float()
    status = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        copy=False,
    )
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('kuchen', string='Property', required=True)