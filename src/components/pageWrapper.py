# src/components/pageWrapper.py

import flet as ft
from models.app_route_model import (
    ThemeContext,
    LocalizationContext,
)
from core.auth_context import AuthContext


def create_page_wrapper(theme_value, loc_value, auth_value=None):
    """
    Returns a wrapper function `wrap(view_component)` that returns a callable
    component function for Flet Router.
    """
    def wrapper(view_component):
        def page_component():
            def build_content():
                component = view_component() if callable(view_component) else view_component
                return component

            if auth_value is not None:
                return AuthContext(
                    auth_value,
                    lambda: ThemeContext(
                        theme_value,
                        lambda: LocalizationContext(loc_value, build_content)
                    )
                )
            else:
                return ThemeContext(
                    theme_value,
                    lambda: LocalizationContext(loc_value, build_content)
                )

        return page_component

    return wrapper
