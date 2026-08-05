# src/core/appLayout.py

import flet as ft
from config import logger
from components.typography import AppText
from core.helper import use_localization_context
from config.colors import AppPalette


@ft.component
def rootLayout():
    loc = use_localization_context()
    outlet = ft.use_route_outlet()
    page = ft.context.page

    # Screen width state in pixels for responsive breakpoints
    width, set_width = ft.use_state(page.width or 1200)

    # State for mobile navigation menu toggle
    is_mobile_menu_open, set_is_mobile_menu_open = ft.use_state(False)

    def on_resize(e):
        set_width(page.width)
        if page.width >= 768:
            set_is_mobile_menu_open(False)

    page.on_resized = on_resize

    def toggle_mobile_menu(e):
        set_is_mobile_menu_open(not is_mobile_menu_open)

    # Device Pixel Breakpoints
    is_mobile = width < 768
    is_tablet = 768 <= width < 1024

    # Current Active Route
    current_route = page.route if page and page.route else "/"

    # Helper function for Navigation Links with Active Underline Indicator
    def nav_item(value_key: str, target_route: str):
        is_active = (current_route == target_route) or (target_route == "/" and current_route == "")
        
        return ft.Container(
            content=AppText(
                value_key=value_key,
                variant="body",
                bold=is_active,
                color=AppPalette.PRIMARY if is_active else AppPalette.ON_SURFACE_VARIANT,
            ),
            padding=ft.Padding.only(bottom=6, left=12, right=12, top=6),
            border=ft.Border(
                top=ft.BorderSide(0, ft.Colors.TRANSPARENT),
                left=ft.BorderSide(0, ft.Colors.TRANSPARENT),
                right=ft.BorderSide(0, ft.Colors.TRANSPARENT),
                bottom=ft.BorderSide(
                    2,
                    AppPalette.PRIMARY if is_active else ft.Colors.TRANSPARENT,
                ),
            ),
            on_click=lambda e: (page.go(target_route), set_is_mobile_menu_open(False)),
            ink=True,
            bgcolor=ft.Colors.TRANSPARENT,
        )

    # Brand Logo & Title Container
    brand_header = ft.Row(
        controls=[
            ft.Image(
                src="images/favicon.png",
                width=32,
                height=32,
                fit=ft.BoxFit.CONTAIN,
            ),
            AppText(value_key="brand_name", variant='h2', color=AppPalette.PRIMARY, bold=True),
        ],
        spacing=10,
    )

    # Center Navigation Bar with Active Underline Indicators & Localization
    center_nav_links = ft.Row(
        controls=[
            nav_item("nav_home", "/"),
            nav_item("nav_services", "/services"),
            # nav_item("nav_projects", "/projects"),  # Reserved for next version
            nav_item("nav_contact", "/contact"),
        ],
        spacing=16,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Right Action Buttons (Language Switcher EN/MM)
    right_actions = ft.Row(
        controls=[
            ft.TextButton(
                "မြန်မာ" if loc.lang == "en" else "en",
                style=ft.ButtonStyle(color=AppPalette.PRIMARY),
                on_click=lambda e: loc.set_lang("mm" if loc.lang == "en" else "en")
            ),
            ft.Container(width=8),
        ],
        spacing=8,
    )

    # Routes mapping for Mobile Bottom Navigation Bar
    nav_routes = ["/", "/services", "/contact"]
    current_index = nav_routes.index(current_route) if current_route in nav_routes else 0

    def handle_nav_change(e):
        try:
            index = int(e.data)
            if 0 <= index < len(nav_routes):
                page.go(nav_routes[index])
        except Exception as err:
            logger.error(f"Error navigating via bottom bar: {err}")

    # Mobile Bottom Navigation Bar
    mobile_bottom_bar = ft.NavigationBar(
        selected_index=current_index,
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        indicator_color=AppPalette.PRIMARY_FIXED,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label=loc.get("nav_home"),
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.WORK_OUTLINED,
                selected_icon=ft.Icons.WORK,
                label=loc.get("nav_services"),
            ),
            # ft.NavigationBarDestination(
            #     icon=ft.Icons.BUSINESS_CENTER_OUTLINED,
            #     selected_icon=ft.Icons.BUSINESS_CENTER,
            #     label=loc.get("nav_projects"),
            # ),
            ft.NavigationBarDestination(
                icon=ft.Icons.CONTACT_MAIL_OUTLINED,
                selected_icon=ft.Icons.CONTACT_MAIL,
                label=loc.get("nav_contact"),
            ),
        ],
        on_change=handle_nav_change,
        visible=is_mobile,
    )

    # Responsive AppBar Construction based on Device Pixel Width
    if is_mobile:
        # ── Mobile View (< 768px) ──
        appBar = ft.AppBar(
            leading=ft.Container(
                content=ft.Image(
                    src="images/favicon.png",
                    width=28,
                    height=28,
                    fit=ft.BoxFit.CONTAIN,
                ),
                padding=ft.Padding.only(left=12),
                alignment=ft.Alignment.CENTER_LEFT,
            ),
            leading_width=44,
            title=AppText(value_key="brand_name", variant='h1', color=AppPalette.PRIMARY, bold=True),
            center_title=False,
            actions=[
                right_actions,
            ],
            bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
            elevation=0,
            shadow_color=ft.Colors.TRANSPARENT,
        )
    elif is_tablet:
        # ── Tablet View (768px - 1024px) ──
        appBar = ft.AppBar(
            toolbar_height=68,
            leading=ft.Container(
                content=brand_header,
                padding=ft.Padding.only(left=12),
                alignment=ft.Alignment.CENTER_LEFT,
            ),
            leading_width=220,
            title=center_nav_links,
            center_title=True,
            actions=[
                right_actions,
            ],
            bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
            elevation=0,
            shadow_color=ft.Colors.TRANSPARENT,
        )
    else:
        # ── Desktop View (>= 1024px) ──
        appBar = ft.AppBar(
            toolbar_height=76,
            leading=ft.Container(
                content=brand_header,
                padding=ft.Padding.only(left=16),
                alignment=ft.Alignment.CENTER_LEFT,
            ),
            leading_width=240,
            title=center_nav_links,
            center_title=True,
            actions=[
                right_actions,
            ],
            bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
            elevation=0,
            shadow_color=ft.Colors.TRANSPARENT,
        )

    outlet_padding = (
        ft.Padding.all(0)
        if is_mobile
        else (
            ft.Padding.symmetric(horizontal=16, vertical=8)
            if is_tablet
            else ft.Padding.symmetric(horizontal=48, vertical=16)
        )
    )

    # ── Language Selection Pop-up Modal State (Declarative Top-level) ──────────
    show_lang_modal, set_show_lang_modal = ft.use_state(True)

    def select_lang(lang_code: str):
        if loc and hasattr(loc, "set_lang"):
            loc.set_lang(lang_code)
        set_show_lang_modal(False)

    def lang_card(flag_emoji: str, title: str, subtitle: str, lang_code: str):
        is_selected = loc and hasattr(loc, "lang") and loc.lang == lang_code
        return ft.Container(
            bgcolor=AppPalette.SURFACE_CONTAINER_LOW,
            border=ft.Border.all(1.5, AppPalette.PRIMARY if is_selected else AppPalette.OUTLINE_VARIANT),
            border_radius=ft.BorderRadius.all(12),
            content=ft.ListTile(
                leading=ft.Text(flag_emoji, size=28),
                title=ft.Text(title, size=15, weight=ft.FontWeight.BOLD, color=AppPalette.ON_SURFACE),
                subtitle=ft.Text(subtitle, size=12, color=AppPalette.ON_SURFACE_VARIANT),
                trailing=ft.Icon(
                    ft.Icons.CHECK_CIRCLE_ROUNDED if is_selected else ft.Icons.ARROW_FORWARD_IOS_ROUNDED,
                    size=18,
                    color=AppPalette.PRIMARY,
                ),
                on_click=lambda e: select_lang(lang_code),
            ),
        )

    lang_modal_overlay = ft.Container(
        expand=True,
        left=0,
        top=0,
        right=0,
        bottom=0,
        bgcolor=ft.Colors.with_opacity(0.75, ft.Colors.BLACK),
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.all(16),
        content=ft.Container(
            width=360,
            bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
            border_radius=ft.BorderRadius.all(16),
            padding=ft.Padding.all(24),
            border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
            content=ft.Column(
                tight=True,
                spacing=0,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.LANGUAGE_ROUNDED, color=AppPalette.PRIMARY, size=24),
                            ft.Text("Choose Your Language", size=18, weight=ft.FontWeight.BOLD, color=AppPalette.ON_SURFACE),
                        ],
                        spacing=8,
                    ),
                    ft.Container(height=12),
                    ft.Text(
                        "ကျေးဇူးပြု၍ သုံးစွဲလိုသော ဘာသာစကားကို ရွေးချယ်ပါ / Choice your language:",
                        size=13,
                        color=AppPalette.ON_SURFACE_VARIANT,
                    ),
                    ft.Container(height=16),
                    lang_card("🇲🇲", "မြန်မာ (Myanmar)", "မြန်မာဘာသာစကား သုံးစွဲမည်", "mm"),
                    ft.Container(height=10),
                    lang_card("🇺🇸", "English", "Use American English", "en"),
                ],
            ),
        ),
    )

    layout_content = ft.Container(
        expand=True,
        padding=0,
        bgcolor=AppPalette.SURFACE,
        content=ft.Column(
            expand=True,
            spacing=0,
            controls=[
                appBar,
                ft.Container(content=outlet, expand=True, padding=outlet_padding) if outlet else ft.Container(),
                mobile_bottom_bar if is_mobile else ft.Container(),
            ]
        )
    )

    if show_lang_modal:
        return ft.Stack(
            controls=[
                layout_content,
                lang_modal_overlay,
            ],
            expand=True,
        )

    return layout_content