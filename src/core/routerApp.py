# src/core/routerApp.py

import flet as ft
from config import logger
from models.app_route_model import (
    ThemeContext, ThemeContextModel,
    LocalizationContext, LocalizationContextModel
)
from core.auth_provider import build_auth_state
from config.localization import LocalizationManager
from components.pageWrapper import create_page_wrapper
from core.auth_context import AuthContext, use_auth
from views.homeView import homeView
from views.serviceView import serviceView
from views.contactView import contactView
from views._404View import four_zero_four
from core.appLayout import rootLayout

@ft.component
def routingApp():
    logger.info("RoutingApp is started ... ")
    # ── Theme State ─────────────────────────────────────────────────────────
    theme_mode, set_theme_mode = ft.use_state(ft.ThemeMode.LIGHT)
    language, set_language = ft.use_state("mm")
    auth_value = build_auth_state()
    
    def handle_toggle_theme(mode: ft.ThemeMode = None):
        if mode:
            set_theme_mode(mode)
        else:
            new_mode = (
                ft.ThemeMode.DARK
                if theme_mode == ft.ThemeMode.LIGHT
                else ft.ThemeMode.LIGHT
            )
            set_theme_mode(new_mode)
            
    toggle_theme = ft.use_callback(handle_toggle_theme, [theme_mode])
    
    theme_value = ft.use_memo(
        lambda: ThemeContextModel(mode=theme_mode, toggle=toggle_theme),
        [theme_mode, toggle_theme],
    )

    def update_theme_mode():
        logger.info(f"Theme mode changed to: {theme_mode}")
        ft.context.page.theme_mode = theme_mode
        ft.context.page.scroll = None

    ft.on_updated(update_theme_mode, [theme_mode])
    
    loc_value = ft.use_memo(
        lambda: LocalizationContextModel(
            lang=language,
            get=lambda k: LocalizationManager.get_string(language, k),
            font_scale=0.85 if language == "mm" else 1.0,
            set_lang=set_language,
        ),
        [language],
    )
    
    wrap = create_page_wrapper(theme_value, loc_value, auth_value)
    
    not_found_route = ft.Route(path="/404", component=wrap(four_zero_four))

    # ── Route Definitions ───────────────────────────────────────────────────
    standalone_routes = [
        ft.Route(
            component=wrap(rootLayout),
            children=[
                ft.Route(path="/", index=True, component=wrap(homeView)),
                ft.Route(path="/services", component=wrap(serviceView)),
                ft.Route(path="/contact", component=wrap(contactView)),
            ]
        ),
    ]
    
    app_router = ft.Router(
        routes=[
            *standalone_routes,
            not_found_route
        ],
        manage_views=False,
        not_found=lambda: ft.context.page.go("/404")
    )
    
    try:
        return AuthContext(
            auth_value,
            lambda: ThemeContext(
                theme_value,
                lambda: LocalizationContext(
                    loc_value,
                    lambda: app_router,
                ),
            ),
        )
    except Exception as e:
        logger.error(f"Error in routingApp: {e}")
        raise