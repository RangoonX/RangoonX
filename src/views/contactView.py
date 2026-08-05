# src/views/contactView.py

import json
import os
import flet as ft
from components.typography import AppText, AppButton
from config.colors import AppPalette


def get_company_info():
    """
    Load company contact info from JSON config file without os.path dependency.
    """
    candidate_paths = [
        "config/company_info.json",
        "assets/config/company_info.json",
        "src/assets/config/company_info.json",
    ]
    for path in candidate_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    return {
        "company_name": "RangoonX Software House",
        "phone": "+959 785955940",
        "phone_url": "tel:+959785955940",
        "email": "rangoonx.com@gmail.com",
        "email_url": "mailto:rangoonx.com@gmail.com",
        "viber": "+959 785955940",
        "viber_url": "viber://chat?number=%2B959785955940",
        "tiktok": "@rangoonx_official",
        "tiktok_url": "https://www.tiktok.com/@rangoonx_official",
        "business_card_url": "https://rangoonx.com/card",
        "address": "Level 8, Tower B, HAGL Myanmar Centre, Yangon, Myanmar",
        "maps_url": "https://maps.google.com/?q=HAGL+Myanmar+Centre"
    }


@ft.component
def PopInContainer(content, is_active: bool = True, duration: int = 500, initial_scale: float = 0.88):
    """
    Reusable Scroll Reveal Pop-in Animation component.
    """
    return ft.Container(
        content=content,
        opacity=1.0 if is_active else 0.0,
        scale=1.0 if is_active else initial_scale,
        animate_opacity=ft.Animation(duration, ft.AnimationCurve.EASE_OUT),
        animate_scale=ft.Animation(duration, ft.AnimationCurve.EASE_OUT_BACK),
    )


@ft.component
def contactView():
    page = ft.context.page
    width = page.width if page and page.width else 1200
    company_info = get_company_info()

    is_mobile = width < 768
    is_tablet = 768 <= width < 1024

    text_align_mode = ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT
    cross_align_mode = ft.CrossAxisAlignment.CENTER if is_mobile else ft.CrossAxisAlignment.START
    main_align_mode = ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START

    # ── Form Refs (use_ref prevents character overwrite on keystrokes) ──────────
    first_name_ref = ft.use_ref()
    last_name_ref = ft.use_ref()
    email_ref = ft.use_ref()
    interest_ref = ft.use_ref()
    message_ref = ft.use_ref()

    submitted, set_submitted = ft.use_state(False)

    def handle_submit(e):
        set_submitted(True)

    # ── Scroll Reveal State Management ──────────────────────────────────────────
    hero_revealed, set_hero_revealed = ft.use_state(False)
    content_revealed, set_content_revealed = ft.use_state(False)

    def trigger_auto_animations():
        set_hero_revealed(True)
        set_content_revealed(True)

    ft.on_updated(trigger_auto_animations, [])

    # ── 1. Page Header Section ──────────────────────────────────────────────────
    header_section = ft.Container(
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=28 if is_mobile else 44,
        ),
        content=PopInContainer(
            content=ft.Column(
                horizontal_alignment=cross_align_mode,
                controls=[
                    AppText(
                        value_key="hero_tag",
                        variant="caption",
                        bold=True,
                        color=AppPalette.PRIMARY,
                        text_align=text_align_mode,
                    ),
                    ft.Container(height=4),
                    AppText(
                        value_key="contact_page_title",
                        variant="h1",
                        bold=True,
                        color=AppPalette.ON_SURFACE,
                        text_align=text_align_mode,
                    ),
                    ft.Container(height=8),
                    AppText(
                        value_key="contact_page_subtitle",
                        variant="body",
                        color=AppPalette.ON_SURFACE_VARIANT,
                        text_align=text_align_mode,
                    ),
                ],
                spacing=4,
            ),
            is_active=hero_revealed,
            duration=500,
        ),
    )

    # ── 2. Interactive Contact Info & Details Card ──────────────────────────────
    def create_interactive_info_row(
        icon: str,
        title_key: str,
        display_text: str,
        url: str = None,
        subtitle_text: str = None,
    ):
        return ft.Container(
            url=url,
            ink=True if url else False,
            border_radius=ft.BorderRadius.all(8),
            padding=ft.Padding.symmetric(horizontal=8, vertical=6),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(icon, size=22, color=AppPalette.PRIMARY),
                        bgcolor=AppPalette.SURFACE_CONTAINER,
                        padding=ft.Padding.all(10),
                        border_radius=ft.BorderRadius.all(8),
                    ),
                    ft.Container(width=12),
                    ft.Column(
                        controls=[
                            AppText(value_key=title_key, variant="body", bold=True, color=AppPalette.ON_SURFACE),
                            ft.Text(
                                display_text,
                                size=13,
                                color=AppPalette.PRIMARY if url else AppPalette.ON_SURFACE_VARIANT,
                                weight=ft.FontWeight.W_600 if url else ft.FontWeight.NORMAL,
                            ),
                            ft.Text(subtitle_text, size=11, color=AppPalette.ON_SURFACE_VARIANT) if subtitle_text else ft.Container(),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                    ft.Icon(ft.Icons.OPEN_IN_NEW_ROUNDED, size=16, color=AppPalette.PRIMARY) if url else ft.Container(),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    contact_info_card = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
        border_radius=ft.BorderRadius.all(12),
        padding=ft.Padding.all(20),
        content=ft.Column(
            controls=[
                create_interactive_info_row(
                    icon=ft.Icons.LOCATION_ON_OUTLINED,
                    title_key="contact_hq_title",
                    display_text=company_info.get("address"),
                    url=company_info.get("maps_url"),
                ),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                create_interactive_info_row(
                    icon=ft.Icons.EMAIL_OUTLINED,
                    title_key="contact_email_title",
                    display_text=company_info.get("email"),
                    url=company_info.get("email_url"),
                ),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                create_interactive_info_row(
                    icon=ft.Icons.PHONE_OUTLINED,
                    title_key="contact_phone_title",
                    display_text=company_info.get("phone"),
                    url=company_info.get("phone_url"),
                ),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                create_interactive_info_row(
                    icon=ft.Icons.VIDEO_LIBRARY_OUTLINED,
                    title_key="solutions",
                    display_text=f"TikTok: {company_info.get('tiktok')}",
                    url=company_info.get("tiktok_url"),
                    subtitle_text="Follow us on TikTok",
                ),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                create_interactive_info_row(
                    icon=ft.Icons.CHAT_OUTLINED,
                    title_key="connect",
                    display_text=f"Viber: {company_info.get('viber')}",
                    url=company_info.get("viber_url"),
                    subtitle_text="Tap to open Viber Chat",
                ),
            ],
            spacing=10,
        ),
    )

    location_badge_card = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOW,
        border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
        border_radius=ft.BorderRadius.all(12),
        padding=ft.Padding.all(20),
        url=company_info.get("business_card_url"),
        ink=True,
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.CONTACT_PAGE_OUTLINED, size=24, color=AppPalette.PRIMARY),
                ft.Container(width=10),
                ft.Column(
                    controls=[
                        ft.Text("🎴 Digital Business Card", size=14, weight=ft.FontWeight.BOLD, color=AppPalette.ON_SURFACE),
                        ft.Text("Tap to view official business card", size=12, color=AppPalette.PRIMARY, weight=ft.FontWeight.W_600),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED, size=16, color=AppPalette.PRIMARY),
            ],
        ),
    )

    left_column = ft.Container(
        content=ft.Column(
            controls=[
                contact_info_card,
                location_badge_card,
            ],
            spacing=20,
        ),
        col={"sm": 12, "md": 5, "lg": 5},
    )

    # ── 3. Contact Form Card (Refs prevent character overwrite on keystrokes) ─
    form_content = ft.Column(
        controls=[
            AppText(value_key="contact_sales", variant="h2", bold=True, color=AppPalette.ON_SURFACE),
            ft.Container(height=4),
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                AppText(value_key="form_first_name", variant="caption", bold=True, color=AppPalette.ON_SURFACE_VARIANT),
                                ft.TextField(
                                    ref=first_name_ref,
                                    hint_text="John",
                                    border_radius=ft.BorderRadius.all(8),
                                    border_color=AppPalette.OUTLINE_VARIANT,
                                    focused_border_color=AppPalette.PRIMARY,
                                    text_size=14,
                                ),
                            ],
                            spacing=4,
                        ),
                        col={"sm": 12, "md": 6},
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                AppText(value_key="form_last_name", variant="caption", bold=True, color=AppPalette.ON_SURFACE_VARIANT),
                                ft.TextField(
                                    ref=last_name_ref,
                                    hint_text="Doe",
                                    border_radius=ft.BorderRadius.all(8),
                                    border_color=AppPalette.OUTLINE_VARIANT,
                                    focused_border_color=AppPalette.PRIMARY,
                                    text_size=14,
                                ),
                            ],
                            spacing=4,
                        ),
                        col={"sm": 12, "md": 6},
                    ),
                ],
                spacing=16,
                run_spacing=16,
            ),
            ft.Container(height=12),
            AppText(value_key="form_email", variant="caption", bold=True, color=AppPalette.ON_SURFACE_VARIANT),
            ft.TextField(
                ref=email_ref,
                hint_text="john@company.com",
                border_radius=ft.BorderRadius.all(8),
                border_color=AppPalette.OUTLINE_VARIANT,
                focused_border_color=AppPalette.PRIMARY,
                text_size=14,
            ),
            ft.Container(height=12),
            AppText(value_key="form_interest", variant="caption", bold=True, color=AppPalette.ON_SURFACE_VARIANT),
            ft.Dropdown(
                ref=interest_ref,
                value="Custom Software Development",
                options=[
                    ft.dropdown.Option("Custom Software Development"),
                    ft.dropdown.Option("Cloud Infrastructure & Migration"),
                    ft.dropdown.Option("AI & Machine Learning Integration"),
                    ft.dropdown.Option("Other Inquiry"),
                ],
                border_radius=ft.BorderRadius.all(8),
                border_color=AppPalette.OUTLINE_VARIANT,
                focused_border_color=AppPalette.PRIMARY,
                text_size=14,
            ),
            ft.Container(height=12),
            AppText(value_key="form_message", variant="caption", bold=True, color=AppPalette.ON_SURFACE_VARIANT),
            ft.TextField(
                ref=message_ref,
                hint_text="Tell us about your technical requirements...",
                multiline=True,
                min_lines=4,
                max_lines=6,
                border_radius=ft.BorderRadius.all(8),
                border_color=AppPalette.OUTLINE_VARIANT,
                focused_border_color=AppPalette.PRIMARY,
                text_size=14,
            ),
            ft.Container(height=20),
            ft.Row(
                controls=[
                    AppButton(
                        value_key="form_submit",
                        variant="filled",
                        on_click=handle_submit,
                        style=ft.ButtonStyle(
                            bgcolor=AppPalette.PRIMARY,
                            color=AppPalette.ON_PRIMARY,
                            padding=ft.Padding.symmetric(horizontal=32, vertical=16),
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                ],
                alignment=main_align_mode,
            ),
            ft.Container(height=8) if submitted else ft.Container(),
            ft.Container(
                bgcolor=AppPalette.PRIMARY_CONTAINER,
                border_radius=ft.BorderRadius.all(8),
                padding=ft.Padding.symmetric(horizontal=16, vertical=12),
                content=AppText(value_key="form_success", variant="caption", bold=True, color=AppPalette.ON_PRIMARY_CONTAINER),
            ) if submitted else ft.Container(),
        ],
        spacing=4,
    )

    right_column = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        border=ft.Border.only(
            top=ft.BorderSide(3, AppPalette.PRIMARY),
            left=ft.BorderSide(1, AppPalette.OUTLINE_VARIANT),
            right=ft.BorderSide(1, AppPalette.OUTLINE_VARIANT),
            bottom=ft.BorderSide(1, AppPalette.OUTLINE_VARIANT),
        ),
        border_radius=ft.BorderRadius.all(12),
        padding=ft.Padding.all(28),
        content=form_content,
        col={"sm": 12, "md": 7, "lg": 7},
    )

    main_grid_section = ft.Container(
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=24 if is_mobile else 36,
        ),
        content=PopInContainer(
            content=ft.ResponsiveRow(
                controls=[
                    left_column,
                    right_column,
                ],
                spacing=24,
                run_spacing=24,
            ),
            is_active=content_revealed,
            duration=600,
        ),
    )

    # ── 4. Footer Section ──────────────────────────────────────────────────────
    footer_section = ft.Container(
        bgcolor=AppPalette.SURFACE,
        border=ft.Border.only(top=ft.BorderSide(1, AppPalette.OUTLINE_VARIANT)),
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=28,
        ),
        content=ft.Column(
            horizontal_alignment=cross_align_mode,
            controls=[
                ft.Row(
                    controls=[
                        AppText(value_key="brand_name", variant="h3", bold=True, color=AppPalette.PRIMARY),
                        ft.Text("•", color=AppPalette.OUTLINE),
                        AppText(value_key="footer_slogan", variant="caption", color=AppPalette.ON_SURFACE_VARIANT),
                    ],
                    alignment=main_align_mode,
                    wrap=True,
                    spacing=12,
                ),
                ft.Container(height=12),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                ft.Container(height=8),
                AppText(
                    value_key="copyright",
                    variant="caption",
                    color=AppPalette.ON_SURFACE_VARIANT,
                    text_align=text_align_mode,
                ),
            ],
            spacing=4,
        ),
    )

    # ── Scrollable ListView ───────────────────────────────────────────────────
    return ft.ListView(
        expand=True,
        spacing=0,
        controls=[
            header_section,
            main_grid_section,
            footer_section,
        ]
    )
