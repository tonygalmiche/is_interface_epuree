import { registry } from "@web/core/registry";

// Entrée « Devenir superutilisateur » retirée du menu de débogage (route /web/become en 404)
registry.category("debug").category("default").remove("becomeSuperuser");
