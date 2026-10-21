# -*- coding: utf-8 -*-
from werkzeug.exceptions import NotFound

from odoo import http
from odoo.addons.web.controllers.home import Home


class IsHome(Home):

    @http.route()
    def switch_to_admin(self):
        # Connexion en superutilisateur (/web/become) supprimée : bouton de la page de connexion et menu de débogage
        raise NotFound()
