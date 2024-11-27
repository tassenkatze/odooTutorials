from odoo import fields, models
from dateutil.relativedelta import relativedelta

class Kuchen(models.Model):
    _name = "kuchen"
    _description = "Hier wird kuchen gesammelt"


    def _default_date_availability(self):
            return fields.Date.context_today(self) + relativedelta(months=3)
    
    active=True

    # Fields
    name = fields.Char(required=True, default="unknown")
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    availability_date = fields.Date(copy=False, default=lambda self: self._default_date_availability())
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    description = fields.Text()
    postcode = fields.Char()
    bedrooms = fields.Integer(default=2)
    living_area = fields.Float(string="Living Area (sqm)")
    garden_area = fields.Float(string="Garden Area (sqm)")
    
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'), ('east', 'East'), ('south', 'South'), ('west', 'West')])
    
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )
    active = fields.Boolean("Active", default=True)

    type_id = fields.Many2one("property.type", string="Property Type")
    tag_ids = fields.Many2many("property.tags", string="Property Tags")

    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)

    offer_ids = fields.One2many('property.offer', 'property_id', string='Offers')

