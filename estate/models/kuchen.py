from odoo import fields, models
from dateutil.relativedelta import relativedelta

class Kuchen(models.Model):
    _name = "kuchen"
    _description = "Hier wird kuchen gesammelt"


    def _default_date_availability(self):
            return fields.Date.context_today(self) + relativedelta(months=3)
    
    active=True

    name = fields.Char(required=True, default="unknown")
    state = "New"

    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    availability_date = fields.Date(copy=False, default=lambda self: self._default_date_availability())
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    description = fields.Text()
    postcode = fields.Char()
    bedrooms = fields.Integer(default=2)
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')])