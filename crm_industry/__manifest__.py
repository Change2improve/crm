# Copyright 2015 Antiun Ingenieria S.L. - Javier Iniesta
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "CRM Industry",
    "summary": "Link leads/opportunities to industries",
    "version": "11.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://www.tecnativa.com",
    "author": "Tecnativa, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "crm",
        "partner_industry_secondary",
    ],
    "data": [
        "views/crm_lead_view.xml",
    ]
}
