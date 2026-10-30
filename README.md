# Interface épurée

[![Licence : AGPL-3](https://img.shields.io/badge/licence-AGPL--3-blue.png)](http://www.gnu.org/licenses/agpl-3.0-standalone.html)
[![Odoo 20.0](https://img.shields.io/badge/odoo-20.0-875A7B.png)](https://github.com/tonygalmiche/is_interface_epuree/tree/20.0)

Ce module épure la page de connexion d'Odoo et retire de l'interface la publicité pour Odoo Enterprise.

Page de connexion :

- inscription sur invitation et réinitialisation du mot de passe désactivée à l'installation (réactivables) ;
- connexion en superutilisateur supprimée ;
- pied de page « Gérer les bases » et « Généré par Odoo » masqué ;
- clé d'accès (`auth_passkey`, `auth_passkey_portal`) désinstallée à l'installation.

Publicité pour Odoo Enterprise :

- modules Enterprise (bouton « Mettre à niveau ») masqués dans Applications ;
- options « Entreprise » retirées des Paramètres, ainsi que les sections devenues vides ;
- menu « My Subscription » (`mysubscription`, abonnement Odoo.com) désinstallé à chaque installation et mise à jour : son tableau de bord appelle `/web/database/list`, ce qui fait bannir l'utilisateur par une jail fail2ban qui surveille le gestionnaire de bases.

**Table des matières**

- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Problèmes connus / Feuille de route](#problèmes-connus--feuille-de-route)
- [Signaler un problème](#signaler-un-problème)
- [Crédits](#crédits)

## Installation

Installer le module depuis Applications. À l'installation :

- l'accès client passe sur « Sur invitation » ;
- la réinitialisation du mot de passe est désactivée ;
- les modules `auth_passkey` et `auth_passkey_portal` sont désinstallés.

Ces réglages ne sont faits qu'une fois : une mise à jour du module ne les remet pas.

## Configuration

Le module n'ajoute aucune option. Les réglages standard restent modifiables dans *Paramètres → Paramètres généraux* :

- **Accès client** « Inscription libre » : réaffiche le lien « Pas encore de compte ? » ;
- **Réinitialisation du mot de passe** : réaffiche le lien « Réinitialiser le mot de passe ».

Pour utiliser les clés d'accès, réinstaller `auth_passkey`.

Le gestionnaire de bases reste réglé comme en standard par le fichier de configuration d'Odoo (`list_db`) : seul son lien dans le pied de page disparaît.

## Utilisation

Rien à faire : la page de connexion, Applications et les Paramètres sont épurés dès l'installation, y compris pour les applications installées ensuite.

## Problèmes connus / Feuille de route

- Sur une base neuve, `auth_passkey_portal` (installé automatiquement avec `portal`) restait installé sans `auth_passkey` (« Some modules are not loaded… ['auth_passkey_portal'] » à chaque démarrage) : corrigé par la dépendance à `portal`, qui fait charger ce module après lui. Sur une base où c'est déjà arrivé : désinstaller `auth_passkey_portal` depuis Applications.
- La désinstallation du module rend la page de connexion standard, la connexion en superutilisateur et l'affichage des modules et options Enterprise. Les modules de clé d'accès ne sont pas réinstallés.

## Signaler un problème

Les problèmes se signalent sur [GitHub Issues](https://github.com/tonygalmiche/is_interface_epuree/issues).

## Crédits

### Auteurs

- InfoSaône

### Contributeurs

- Tony Galmiche ([InfoSaône](http://www.infosaone.com))

### Mainteneurs

Ce module est maintenu par [InfoSaône](http://www.infosaone.com).
