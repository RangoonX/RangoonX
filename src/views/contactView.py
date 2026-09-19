import json
import flet as ft
from components.typography import AppText, AppButton
from components.animations import PopInContainer
from components.footer import AppFooter
from config.colors import AppPalette
from core.helper import use_screen_context


def get_company_info():
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    candidate_paths = [
        os.path.join(base_dir, "config", "company_info.json"),
        os.path.join(base_dir, "assets", "config", "company_info.json"),
        "config/company_info.json",
        "assets/config/company_info.json",
    ]
    for path in candidate_paths:
        if not os.path.isfile(path):
            continue
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
        "maps_url": "https://maps.google.com/?q=HAGL+Myanmar+Centre",
    }


@ft.component
def ContactInfoRow(
    icon: str,
    title_key: str,
    display_text: str,
    url: str = None,
    subtitle_text: str = None,
):
    return ft.Container(
        url=url,
        ink=True if url else False,
        border_radius=ft.BorderRadius.all(10),
        padding=ft.Padding.symmetric(horizontal=12, vertical=10),
        bgcolor=ft.Colors.TRANSPARENT,
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Icon(icon, size=20, color=AppPalette.PRIMARY),
                    bgcolor=AppPalette.PRIMARY_FIXED,
                    padding=ft.Padding.all(10),
                    border_radius=ft.BorderRadius.all(10),
                ),
                ft.Container(width=12),
                ft.Column(
                    controls=[
                        AppText(
                            value_key=title_key,
                            variant="caption",
                            bold=True,
                            color=AppPalette.ON_SURFACE_VARIANT,
                        ),
                        ft.Text(
                            display_text,
                            size=14,
                            color=AppPalette.PRIMARY if url else AppPalette.ON_SURFACE,
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Text(
                            subtitle_text,
                            size=11,
                            color=AppPalette.ON_SURFACE_VARIANT,
                        ) if subtitle_text else ft.Container(),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.Icon(
                    ft.Icons.ARROW_OUTWARD_ROUNDED,
                    size=16,
                    color=AppPalette.PRIMARY,
                    opacity=0.7,
                ) if url else ft.Container(),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


@ft.component
def contactView():
    page = ft.context.page
    screen = use_screen_context()
    company_info = get_company_info()

    is_mobile = screen.is_mobile
    is_tablet = screen.is_tablet

    text_align_mode = ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT
    cross_align_mode = ft.CrossAxisAlignment.CENTER if is_mobile else ft.CrossAxisAlignment.START
    main_align_mode = ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START

    first_name_ref = ft.use_ref()
    last_name_ref = ft.use_ref()
    email_ref = ft.use_ref()
    interest_ref = ft.use_ref()
    message_ref = ft.use_ref()

    submitted, set_submitted = ft.use_state(False)

    def handle_submit(e):
        set_submitted(True)

    hero_revealed, set_hero_revealed = ft.use_state(False)
    content_revealed, set_content_revealed = ft.use_state(False)

    def trigger_auto_animations():
        set_hero_revealed(True)
        set_content_revealed(True)

    ft.on_updated(trigger_auto_animations, [])

    # ── Page Header ───────────────────────────────────────────────────────────
    header_section = ft.Container(
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=36 if is_mobile else 52,
        ),
        content=PopInContainer(
            content=ft.Column(
                horizontal_alignment=cross_align_mode,
                controls=[
                    ft.Container(
                        content=AppText(
                            value_key="hero_tag",
                            variant="caption",
                            bold=True,
                            color=AppPalette.PRIMARY,
                        ),
                        bgcolor=AppPalette.PRIMARY_FIXED,
                        padding=ft.Padding.symmetric(horizontal=14, vertical=6),
                        border_radius=ft.BorderRadius.all(20),
                    ),
                    ft.Container(height=12),
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
                spacing=0,
            ),
            is_active=hero_revealed,
            duration=500,
        ),
    )

    # ── Contact Info Cards ────────────────────────────────────────────────────
    contact_info_card = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
        border_radius=ft.BorderRadius.all(14),
        padding=ft.Padding.all(16),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=8,
            color=ft.Colors.with_opacity(0.04, ft.Colors.BLACK),
            offset=ft.Offset(0, 2),
        ),
        content=ft.Column(
            controls=[
                ContactInfoRow(
                    icon=ft.Icons.LOCATION_ON_OUTLINED,
                    title_key="contact_hq_title",
                    display_text=company_info.get("address"),
                    url=company_info.get("maps_url"),
                ),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                ContactInfoRow(
                    icon=ft.Icons.EMAIL_OUTLINED,
                    title_key="contact_email_title",
                    display_text=company_info.get("email"),
                    url=company_info.get("email_url"),
                ),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                ContactInfoRow(
                    icon=ft.Icons.PHONE_OUTLINED,
                    title_key="contact_phone_title",
                    display_text=company_info.get("phone"),
                    url=company_info.get("phone_url"),
                ),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                ContactInfoRow(
                    icon=ft.Icons.VIDEO_LIBRARY_OUTLINED,
                    title_key="solutions",
                    display_text=f"TikTok: {company_info.get('tiktok')}",
                    url=company_info.get("tiktok_url"),
                    subtitle_text="Follow us on TikTok",
                ),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                ContactInfoRow(
                    icon=ft.Icons.CHAT_OUTLINED,
                    title_key="connect",
                    display_text=f"Viber: {company_info.get('viber')}",
                    url=company_info.get("viber_url"),
                    subtitle_text="Tap to open Viber Chat",
                ),
            ],
            spacing=4,
        ),
    )

    business_card_badge = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
        border_radius=ft.BorderRadius.all(14),
        padding=ft.Padding.all(16),
        url=company_info.get("business_card_url"),
        ink=True,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=8,
            color=ft.Colors.with_opacity(0.04, ft.Colors.BLACK),
            offset=ft.Offset(0, 2),
        ),
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Icon(ft.Icons.CONTACT_PAGE_OUTLINED, size=20, color=AppPalette.PRIMARY),
                    bgcolor=AppPalette.PRIMARY_FIXED,
                    padding=ft.Padding.all(10),
                    border_radius=ft.BorderRadius.all(10),
                ),
                ft.Container(width=12),
                ft.Column(
                    controls=[
                        ft.Text(
                            "Digital Business Card",
                            size=14,
                            weight=ft.FontWeight.BOLD,
                            color=AppPalette.ON_SURFACE,
                        ),
                        ft.Text(
                            "Tap to view official business card",
                            size=12,
                            color=AppPalette.PRIMARY,
                            weight=ft.FontWeight.W_600,
                        ),
                    ],
                    spacing=2,
                    expand=True,
                ),
                ft.Icon(
                    ft.Icons.ARROW_OUTWARD_ROUNDED,
                    size=16,
                    color=AppPalette.PRIMARY,
                    opacity=0.7,
                ),
            ],
        ),
    )

    left_column = ft.Container(
        content=ft.Column(
            controls=[contact_info_card, business_card_badge],
            spacing=16,
        ),
        col={"sm": 12, "md": 5, "lg": 5},
    )

    # ── Contact Form ──────────────────────────────────────────────────────────
    def styled_field(ref, hint, multiline=False, min_lines=1, max_lines=1):
        return ft.TextField(
            ref=ref,
            hint_text=hint,
            multiline=multiline,
            min_lines=min_lines,
            max_lines=max_lines,
            border_radius=ft.BorderRadius.all(10),
            border_color=AppPalette.OUTLINE_VARIANT,
            border_width=1,
            focused_border_color=AppPalette.PRIMARY,
            focused_border_width=2,
            text_size=14,
            content_padding=ft.Padding.symmetric(horizontal=16, vertical=14),
        )

    form_content = ft.Column(
        controls=[
            AppText(
                value_key="contact_sales",
                variant="h2",
                bold=True,
                color=AppPalette.ON_SURFACE,
            ),
            ft.Container(height=8),
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                AppText(
                                    value_key="form_first_name",
                                    variant="caption",
                                    bold=True,
                                    color=AppPalette.ON_SURFACE_VARIANT,
                                ),
                                ft.Container(height=4),
                                styled_field(first_name_ref, "John"),
                            ],
                            spacing=0,
                        ),
                        col={"sm": 12, "md": 6},
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                AppText(
                                    value_key="form_last_name",
                                    variant="caption",
                                    bold=True,
                                    color=AppPalette.ON_SURFACE_VARIANT,
                                ),
                                ft.Container(height=4),
                                styled_field(last_name_ref, "Doe"),
                            ],
                            spacing=0,
                        ),
                        col={"sm": 12, "md": 6},
                    ),
                ],
                spacing=16,
                run_spacing=16,
            ),
            ft.Container(height=16),
            AppText(
                value_key="form_email",
                variant="caption",
                bold=True,
                color=AppPalette.ON_SURFACE_VARIANT,
            ),
            ft.Container(height=4),
            styled_field(email_ref, "john@company.com"),
            ft.Container(height=16),
            AppText(
                value_key="form_interest",
                variant="caption",
                bold=True,
                color=AppPalette.ON_SURFACE_VARIANT,
            ),
            ft.Container(height=4),
            ft.Dropdown(
                ref=interest_ref,
                value="Custom Software Development",
                options=[
                    ft.dropdown.Option("Custom Software Development"),
                    ft.dropdown.Option("Cloud Infrastructure & Migration"),
                    ft.dropdown.Option("AI & Machine Learning Integration"),
                    ft.dropdown.Option("IoT & Electronics Hardware"),
                    ft.dropdown.Option("ERP & POS Systems"),
                    ft.dropdown.Option("Other Inquiry"),
                ],
                border_radius=ft.BorderRadius.all(10),
                border_color=AppPalette.OUTLINE_VARIANT,
                border_width=1,
                focused_border_color=AppPalette.PRIMARY,
                focused_border_width=2,
                text_size=14,
                content_padding=ft.Padding.symmetric(horizontal=16, vertical=14),
            ),
            ft.Container(height=16),
            AppText(
                value_key="form_message",
                variant="caption",
                bold=True,
                color=AppPalette.ON_SURFACE_VARIANT,
            ),
            ft.Container(height=4),
            styled_field(
                message_ref,
                "Tell us about your technical requirements...",
                multiline=True,
                min_lines=4,
                max_lines=6,
            ),
            ft.Container(height=24),
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
                            shape=ft.RoundedRectangleBorder(radius=10),
                            shadow_color=ft.Colors.with_opacity(0.2, AppPalette.PRIMARY),
                            elevation=4,
                        ),
                    ),
                ],
                alignment=main_align_mode,
            ),
            ft.Container(height=12) if submitted else ft.Container(),
            ft.Container(
                bgcolor=AppPalette.PRIMARY_FIXED,
                border_radius=ft.BorderRadius.all(10),
                padding=ft.Padding.symmetric(horizontal=16, vertical=14),
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, size=18, color=AppPalette.PRIMARY),
                        ft.Container(width=8),
                        AppText(
                            value_key="form_success",
                            variant="caption",
                            bold=True,
                            color=AppPalette.PRIMARY,
                        ),
                    ],
                    spacing=0,
                ),
            ) if submitted else ft.Container(),
        ],
        spacing=0,
    )

    right_column = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
        border_radius=ft.BorderRadius.all(14),
        padding=ft.Padding.all(28),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=12,
            color=ft.Colors.with_opacity(0.06, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),
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
                controls=[left_column, right_column],
                spacing=24,
                run_spacing=24,
            ),
            is_active=content_revealed,
            duration=600,
        ),
    )

    return ft.ListView(
        expand=True,
        spacing=0,
        controls=[
            header_section,
            main_grid_section,
            AppFooter(),
        ],
    )
