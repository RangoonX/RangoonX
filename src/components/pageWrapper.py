# src/components/pageWrapper.py

import flet as ft
from models.app_route_model import (
    ThemeContext,
    LocalizationContext,
    ScreenContext,
)
from core.auth_context import AuthContext


def create_page_wrapper(theme_value, loc_value, auth_value=None, screen_value=None):
    def wrapper(view_component):
        def page_component():
            def build_content():
                component = view_component() if callable(view_component) else view_component
                return component

            def with_screen():
                if screen_value is not None:
                    return ScreenContext(screen_value, build_content)
                return build_content()

            if auth_value is not None:
                return AuthContext(
                    auth_value,
                    lambda: ThemeContext(
                        theme_value,
                        lambda: LocalizationContext(loc_value, with_screen)
                    )
                )
            else:
                return ThemeContext(
                    theme_value,
                    lambda: LocalizationContext(loc_value, with_screen)
                )

        return page_component

    return wrapper
