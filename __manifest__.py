# -*- coding: utf-8 -*-
{
    "name": "InfoSaône - Interface épurée pour Odoo 20",
    "version": "20.0.1.0.2",
    "author": "InfoSaône / Tony Galmiche",
    "category": "InfoSaône",
    "summary": "Page de connexion épurée, inscription sur invitation, clé d'accès désinstallée, publicité Enterprise masquée",
    "description": """
        Page de connexion : pied de page « Généré par Odoo » masqué, connexion en superutilisateur supprimée.
        À l'installation seulement : inscription sur invitation, réinitialisation du mot de passe désactivée,
        clé d'accès (auth_passkey) désinstallée ; ces réglages restent modifiables ensuite.
        Modules Enterprise masqués dans Applications, options « Entreprise » retirées des Paramètres.
        Menu « My Subscription » (mysubscription) désinstallé : il appelle /web/database/list (bannissement fail2ban).
    """,
    "maintainer": "InfoSaône",
    "website": "http://www.infosaone.com",
    "depends": [
        'auth_signup',
        'base_setup',
        # Chargé après auth_passkey_portal (installé automatiquement avec portal) sur une base neuve, pour que
        # data/ir_module_module.xml le trouve installé et le désinstalle avec auth_passkey (même profondeur dans le
        # graphe des modules, ordre alphabétique)
        'portal',
        'web',
    ],
    "data": [
        'data/ir_config_parameter.xml',
        'data/ir_module_module.xml',
        'views/login_templates.xml',
        'views/ir_module_module_views.xml',
    ],
    "assets": {
        'web.assets_backend': [
            'is_interface_epuree/static/src/js/debug_menu.js',
        ],
    },
    "uninstall_hook": "uninstall_hook",
    "installable": True,
    "auto_install": False,
    "application": False,
    "license": "AGPL-3",
}
