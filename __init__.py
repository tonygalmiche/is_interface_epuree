# -*- coding: utf-8 -*-
from . import controllers
from . import models


def uninstall_hook(env):
    # Filtre des modules Enterprise posé sur une action de base : non retiré par la désinstallation
    env.ref('base.open_module_tree').domain = False
