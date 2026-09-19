# src/core/helper.py

import flet as ft
from models.app_route_model import LocalizationContext, ThemeContext, ScreenContext



def use_theme_context():
    return ft.use_context(ThemeContext)


#create a hook to use the whole context
def use_localization_context():
    return ft.use_context(LocalizationContext)


def use_loc():
    ctx = ft.use_context(LocalizationContext)

    def translate(key: str) -> str:
        if ctx is None:
            return key
        return ctx(key)

    return translate


def use_screen_context():
    return ft.use_context(ScreenContext)

