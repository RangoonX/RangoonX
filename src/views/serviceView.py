# src/views/serviceView.py

import flet as ft
from components.typography import AppText, AppButton
from config.colors import AppPalette


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
def ServiceCard(
    icon: str,
    title_key: str,
    desc_key: str,
    tags: list[str] = None,
    col_span: int = 12,
    cross_align_mode=ft.CrossAxisAlignment.START,
    main_align_mode=ft.MainAxisAlignment.START,
    text_align_mode=ft.TextAlign.LEFT,
    is_revealed: bool = True,
):
    """
    Service Card with top primary accent border, hover scale & scroll reveal.
    """
    is_hovered, set_is_hovered = ft.use_state(False)

    badge_controls = []
    if tags:
        badge_controls = [
            ft.Container(
                content=ft.Text(tag, size=12, weight=ft.FontWeight.W_600, color=AppPalette.PRIMARY),
                bgcolor=AppPalette.SURFACE_CONTAINER,
                padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                border_radius=ft.BorderRadius.all(6),
            ) for tag in tags
        ]

    def handle_hover(e):
        set_is_hovered(e.data == "true")

    return ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        border=ft.Border.only(
            top=ft.BorderSide(3, AppPalette.PRIMARY if is_hovered else AppPalette.PRIMARY_CONTAINER),
            left=ft.BorderSide(1, AppPalette.OUTLINE_VARIANT),
            right=ft.BorderSide(1, AppPalette.OUTLINE_VARIANT),
            bottom=ft.BorderSide(1, AppPalette.OUTLINE_VARIANT),
        ),
        border_radius=ft.BorderRadius.all(12),
        padding=ft.Padding.all(24),
        opacity=1.0 if is_revealed else 0.0,
        scale=1.02 if is_hovered else (1.0 if is_revealed else 0.90),
        animate_opacity=ft.Animation(450, ft.AnimationCurve.EASE_OUT),
        animate_scale=ft.Animation(350, ft.AnimationCurve.EASE_OUT_BACK),
        on_hover=handle_hover,
        content=ft.Column(
            horizontal_alignment=cross_align_mode,
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(icon, size=28, color=AppPalette.PRIMARY),
                            bgcolor=AppPalette.SURFACE_CONTAINER_LOW,
                            padding=ft.Padding.all(10),
                            border_radius=ft.BorderRadius.all(8),
                        ),
                        ft.Container(width=12),
                        ft.Column(
                            controls=[
                                AppText(value_key=title_key, variant="h3", bold=True, color=AppPalette.ON_SURFACE),
                            ],
                            spacing=2,
                            expand=True,
                        ),
                    ],
                    alignment=main_align_mode,
                ),
                ft.Container(height=12),
                AppText(
                    value_key=desc_key,
                    variant="body",
                    color=AppPalette.ON_SURFACE_VARIANT,
                    text_align=text_align_mode,
                ),
                ft.Container(height=16) if badge_controls else ft.Container(),
                ft.Row(controls=badge_controls, spacing=8, alignment=main_align_mode, wrap=True) if badge_controls else ft.Container(),
            ],
            spacing=4,
        ),
        col={"sm": 12, "md": col_span, "lg": col_span},
    )


@ft.component
def serviceView():
    page = ft.context.page
    width = page.width if page and page.width else 1200

    is_mobile = width < 768
    is_tablet = 768 <= width < 1024

    text_align_mode = ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT
    cross_align_mode = ft.CrossAxisAlignment.CENTER if is_mobile else ft.CrossAxisAlignment.START
    main_align_mode = ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START

    # ── Auto Pop-up Animation State Management ──────────────────────────────────
    hero_revealed, set_hero_revealed = ft.use_state(False)
    cards_revealed, set_cards_revealed = ft.use_state(False)
    banner_revealed, set_banner_revealed = ft.use_state(False)

    def trigger_auto_animations():
        set_hero_revealed(True)
        set_cards_revealed(True)
        set_banner_revealed(True)

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
                        value_key="services_page_title",
                        variant="h1",
                        bold=True,
                        color=AppPalette.ON_SURFACE,
                        text_align=text_align_mode,
                    ),
                    ft.Container(height=8),
                    AppText(
                        value_key="services_page_subtitle",
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

    # ── 2. Services Grid Section ────────────────────────────────────────────────
    services_grid = ft.ResponsiveRow(
        controls=[
            ServiceCard(
                icon=ft.Icons.CODE_ROUNDED,
                title_key="service_1_title",
                desc_key="service_1_desc",
                tags=["React", "Node.js", "Flutter", "Python"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=cards_revealed,
            ),
            ServiceCard(
                icon=ft.Icons.CLOUD_SYNC_OUTLINED,
                title_key="service_2_title",
                desc_key="service_2_desc",
                tags=["AWS", "Azure", "DevOps", "Docker"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=cards_revealed,
            ),
            ServiceCard(
                icon=ft.Icons.PSYCHOLOGY_OUTLINED,
                title_key="service_3_title",
                desc_key="service_3_desc",
                tags=["Machine Learning", "Python", "Data Engineering"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=cards_revealed,
            ),
            ServiceCard(
                icon=ft.Icons.SUPPORT_AGENT_OUTLINED,
                title_key="service_4_title",
                desc_key="service_4_desc",
                tags=["SLA", "Security Audit", "24/7 Monitoring"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=cards_revealed,
            ),
        ],
        spacing=20,
        run_spacing=20,
    )

    services_section = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOW,
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=32 if is_mobile else 48,
        ),
        content=services_grid,
    )

    banner_height = 280 if is_mobile else (360 if is_tablet else 400)

    banner_image_container = ft.Container(
        height=banner_height,
        content=ft.Stack(
            controls=[
                ft.Image(
                    src="images/service_banner.png",
                    fit=ft.BoxFit.COVER,
                    width=float("inf"),
                    height=banner_height,
                ),
                ft.Container(
                    height=banner_height,
                    width=float("inf"),
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment.TOP_CENTER if is_mobile else ft.Alignment.CENTER_LEFT,
                        end=ft.Alignment.BOTTOM_CENTER if is_mobile else ft.Alignment.CENTER_RIGHT,
                        colors=[
                            ft.Colors.with_opacity(0.96, AppPalette.SURFACE_CONTAINER_LOWEST),
                            ft.Colors.with_opacity(0.75, AppPalette.SURFACE_CONTAINER_LOWEST),
                            ft.Colors.TRANSPARENT,
                        ],
                        stops=[0.0, 0.45, 0.85] if not is_mobile else [0.0, 0.65, 1.0],
                    ),
                    padding=ft.Padding.all(24 if is_mobile else 48),
                    alignment=ft.Alignment.CENTER if is_mobile else ft.Alignment.CENTER_LEFT,
                    content=ft.Container(
                        width=None if is_mobile else 480,
                        content=ft.Column(
                            horizontal_alignment=cross_align_mode,
                            alignment=main_align_mode,
                            controls=[
                                AppText(
                                    value_key="services_cta_title",
                                    variant="h2",
                                    bold=True,
                                    color=AppPalette.ON_SURFACE,
                                    text_align=text_align_mode,
                                ),
                                ft.Container(height=6),
                                AppText(
                                    value_key="services_cta_desc",
                                    variant="body",
                                    color=AppPalette.ON_SURFACE_VARIANT,
                                    text_align=text_align_mode,
                                ),
                                ft.Container(height=20),
                                AppButton(
                                    value_key="get_in_touch",
                                    variant="filled",
                                    on_click=lambda e: page.go("/contact"),
                                    style=ft.ButtonStyle(
                                        bgcolor=AppPalette.PRIMARY,
                                        color=AppPalette.ON_PRIMARY,
                                        padding=ft.Padding.symmetric(horizontal=28, vertical=16),
                                        shape=ft.RoundedRectangleBorder(radius=8),
                                    ),
                                ),
                            ],
                            spacing=4,
                        ),
                    ),
                ),
            ]
        ),
        border_radius=ft.BorderRadius.all(16),
        border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
    )

    banner_section = ft.Container(
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=36 if is_mobile else 52,
        ),
        content=PopInContainer(
            content=banner_image_container,
            is_active=banner_revealed,
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
            services_section,
            banner_section,
            footer_section,
        ]
    )
