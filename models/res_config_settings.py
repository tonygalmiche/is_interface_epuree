# -*- coding: utf-8 -*-
from odoo import api, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.model
    def _get_view(self, view_id=None, view_type='form', **options):
        arch, view = super()._get_view(view_id, view_type, **options)
        if view_type == 'form':
            # Options « Entreprise » (badge, fenêtre « Passez à Odoo Enterprise ») retirées, avec leur <setting>
            for field in arch.xpath("//field[@widget='upgrade_boolean']"):
                settings = field.xpath("ancestor::setting[1]")
                node = settings[0] if settings else field
                if node.getparent() is not None:
                    node.getparent().remove(node)
            # Blocs devenus vides : pas de titre de section seul
            for block in arch.xpath("//block[not(.//setting)]"):
                block.getparent().remove(block)
        return arch, view
