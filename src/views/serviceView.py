import flet as ft
from components.typography import AppText, AppButton
from components.animations import PopInContainer
from components.footer import AppFooter
from config.colors import AppPalette


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
    badge_controls = []
    if tags:
        badge_controls = [
            ft.Container(
                content=ft.Text(
                    tag,
                    size=11,
                    weight=ft.FontWeight.W_600,
                    color=AppPalette.PRIMARY,
                ),
                bgcolor=AppPalette.PRIMARY_FIXED,
                padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                border_radius=ft.BorderRadius.all(20),
            ) for tag in tags
        ]

    return ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
        border_radius=ft.BorderRadius.all(12),
        padding=ft.Padding.all(24),
        opacity=1.0 if is_revealed else 0.0,
        scale=1.0 if is_revealed else 0.90,
        animate_opacity=ft.Animation(450, ft.AnimationCurve.EASE_OUT),
        animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=4,
            color=ft.Colors.with_opacity(0.04, ft.Colors.BLACK),
            offset=ft.Offset(0, 2),
        ),
        content=ft.Column(
            horizontal_alignment=cross_align_mode,
            controls=[
                ft.Container(
                    content=ft.Icon(icon, size=24, color=AppPalette.ON_PRIMARY),
                    bgcolor=AppPalette.PRIMARY,
                    padding=ft.Padding.all(10),
                    border_radius=ft.BorderRadius.all(10),
                ),
                ft.Container(height=16),
                AppText(
                    value_key=title_key,
                    variant="h3",
                    bold=True,
                    color=AppPalette.ON_SURFACE,
                    text_align=text_align_mode,
                ),
                ft.Container(height=8),
                AppText(
                    value_key=desc_key,
                    variant="body",
                    color=AppPalette.ON_SURFACE_VARIANT,
                    text_align=text_align_mode,
                ),
                ft.Container(height=16) if badge_controls else ft.Container(),
                ft.Row(
                    controls=badge_controls,
                    spacing=6,
                    alignment=main_align_mode,
                    wrap=True,
                ) if badge_controls else ft.Container(),
            ],
            spacing=0,
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

    hero_revealed, set_hero_revealed = ft.use_state(False)
    cards_revealed, set_cards_revealed = ft.use_state(False)
    banner_revealed, set_banner_revealed = ft.use_state(False)

    def trigger_auto_animations():
        set_hero_revealed(True)
        set_cards_revealed(True)
        set_banner_revealed(True)

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
                spacing=0,
            ),
            is_active=hero_revealed,
            duration=500,
        ),
    )

    # ── Services Grid ─────────────────────────────────────────────────────────
    services_grid = ft.ResponsiveRow(
        controls=[
            ServiceCard(
                icon=ft.Icons.CODE_ROUNDED,
                title_key="service_1_title",
                desc_key="service_1_desc",
                tags=["React", "Flutter", "Python", "Node.js"],
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
                tags=["AWS", "Azure", "Docker", "CI/CD"],
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
                tags=["Machine Learning", "LLM", "Computer Vision"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=cards_revealed,
            ),
            ServiceCard(
                icon=ft.Icons.DEVELOPER_BOARD_OUTLINED,
                title_key="service_4_title",
                desc_key="service_4_desc",
                tags=["Embedded", "Sensors", "PCB", "Firmware"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=cards_revealed,
            ),
            ServiceCard(
                icon=ft.Icons.POINT_OF_SALE_OUTLINED,
                title_key="service_5_title",
                desc_key="service_5_desc",
                tags=["Inventory", "Finance", "Multi-branch"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=cards_revealed,
            ),
            ServiceCard(
                icon=ft.Icons.SECURITY_OUTLINED,
                title_key="service_6_title",
                desc_key="service_6_desc",
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
            vertical=40 if is_mobile else 56,
        ),
        content=services_grid,
    )

    # ── CTA Banner ────────────────────────────────────────────────────────────
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
                                ft.Container(height=8),
                                AppText(
                                    value_key="services_cta_desc",
                                    variant="body",
                                    color=AppPalette.ON_SURFACE_VARIANT,
                                    text_align=text_align_mode,
                                ),
                                ft.Container(height=24),
                                AppButton(
                                    value_key="get_in_touch",
                                    variant="filled",
                                    on_click=lambda e: page.go("/contact"),
                                    style=ft.ButtonStyle(
                                        bgcolor=AppPalette.PRIMARY,
                                        color=AppPalette.ON_PRIMARY,
                                        padding=ft.Padding.symmetric(horizontal=28, vertical=16),
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        shadow_color=ft.Colors.with_opacity(0.2, AppPalette.PRIMARY),
                                        elevation=4,
                                    ),
                                ),
                            ],
                            spacing=0,
                        ),
                    ),
                ),
            ],
        ),
        border_radius=ft.BorderRadius.all(16),
        border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=12,
            color=ft.Colors.with_opacity(0.06, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        ),
    )

    banner_section = ft.Container(
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=40 if is_mobile else 56,
        ),
        content=PopInContainer(
            content=banner_image_container,
            is_active=banner_revealed,
            duration=600,
        ),
    )

    return ft.ListView(
        expand=True,
        spacing=0,
        controls=[
            header_section,
            services_section,
            banner_section,
            AppFooter(),
        ],
    )
