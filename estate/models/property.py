from odoo import fields, models, api
from datetime import timedelta

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

    validity = fields.Integer(default = 7)
    date_deadline = fields.Datetime(compute="_compute_date_deadline")

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = (record.create_date or fields.Datetime.now()) + timedelta(days=record.validity)