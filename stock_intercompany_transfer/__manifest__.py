# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies (<https://www.cybrosys.com>)
#    Author: Manasa T P (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Inter Company Stock Transfer',
    'version': '18.0.1.0.0',
    'category': 'Inventory',
    'summary': """Create counterpart Receipt/Delivery Orders between
    companies.""",
    'description': """Automatically Create Receipt/Delivery orders if any
    company validates a Deliver Order/Receipt to the selected company,
    Inter Company Stock Transfer, Stock Transfer,Create counterpart
    Receipt/Delivery Orders between companies""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['stock', 'account'],
    'data': [
        'views/res_company_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
