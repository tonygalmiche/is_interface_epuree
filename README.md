# is_interface_epuree

Module Odoo 20 développé par [InfoSaône](http://www.infosaone.com) : page de connexion épurée et publicité pour Odoo Enterprise retirée de l'interface, sans fichiers recopiés dans chaque module client.

Cahier des charges : `~/Documents/Développement/Documentation/modules-generiques/is_interface_epuree.md`.

## Ce qui change

| Élément | Module |
|---|---|
| Lien « Pas encore de compte ? » | Inscription sur invitation (`b2b`) **à l'installation** ; réactivable dans Paramètres → Généraux → Accès client |
| Lien « Réinitialiser le mot de passe » | Désactivé **à l'installation** ; réactivable dans Paramètres → Généraux |
| Connexion en superutilisateur | Supprimée : bouton de la page de connexion, entrée du menu de débogage, route `/web/become` (404) |
| Pied de page « Gérer les bases » et « Généré par Odoo » | Toujours masqué (le gestionnaire de bases reste réglé par `list_db`) |
| Clé d'accès (`auth_passkey`, `auth_passkey_portal`) | Désinstallés **à l'installation** ; un `-u` ne fait rien |
| Modules Enterprise dans Applications | Masqués (filtre `to_buy = False` sur l'action) |
| Options « Entreprise » des Paramètres | Retirées, avec les blocs devenus vides |

Les réglages faits à l'installation (fichiers `data/` en `noupdate`) ne sont jamais remis par un `-u`.

## Fonctionnement

- `views/login_templates.xml` : héritage de `web.login_layout` (pied de page) et `web.login` (bouton superutilisateur).
- `controllers/main.py` : `/web/become` renvoie une 404.
- `static/src/js/debug_menu.js` : entrée « Devenir superutilisateur » retirée du menu de débogage.
- `views/ir_module_module_views.xml` : filtre sur l'action Applications (`base.open_module_tree`), retiré par `uninstall_hook`.
- `models/res_config_settings.py` : `_get_view` retire les `<setting>` des champs `widget="upgrade_boolean"`, puis les `<block>` vides.
- `data/ir_config_parameter.xml`, `data/ir_module_module.xml` : réglages et désinstallation à l'installation seulement.
