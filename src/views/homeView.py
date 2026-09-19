import flet as ft
from components.typography import AppText, AppButton
from components.animations import PopInContainer
from components.footer import AppFooter
from config.colors import AppPalette
from core.helper import use_screen_context


@ft.component
def CapabilityBlock(
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
                ft.Container(height=6),
                AppText(
                    value_key=desc_key,
                    variant="body",
                    color=AppPalette.ON_SURFACE_VARIANT,
                    text_align=text_align_mode,
                ),
                ft.Container(height=12) if badge_controls else ft.Container(),
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
def homeView():
    page = ft.context.page
    screen = use_screen_context()

    is_mobile = screen.is_mobile
    is_tablet = screen.is_tablet

    text_align_mode = ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT
    cross_align_mode = ft.CrossAxisAlignment.CENTER if is_mobile else ft.CrossAxisAlignment.START
    main_align_mode = ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START

    hero_revealed, set_hero_revealed = ft.use_state(False)
    capabilities_revealed, set_capabilities_revealed = ft.use_state(False)
    contact_revealed, set_contact_revealed = ft.use_state(False)

    def trigger_auto_animations():
        set_hero_revealed(True)
        set_capabilities_revealed(True)
        set_contact_revealed(True)

    ft.on_updated(trigger_auto_animations, [])

    # ── Hero Section ──────────────────────────────────────────────────────────
    hero_text_column = ft.Column(
        horizontal_alignment=cross_align_mode,
        controls=[
            ft.Container(
                content=AppText(
                    value_key="hero_tag",
                    variant="caption",
                    bold=True,
                    color=AppPalette.PRIMARY,
                    text_align=text_align_mode,
                ),
                bgcolor=AppPalette.PRIMARY_FIXED,
                padding=ft.Padding.symmetric(horizontal=14, vertical=6),
                border_radius=ft.BorderRadius.all(20),
            ),
            ft.Container(height=12),
            AppText(
                value_key="hero_title",
                variant="h1",
                bold=True,
                color=AppPalette.ON_SURFACE,
                text_align=text_align_mode,
            ),
            ft.Container(height=12),
            AppText(
                value_key="hero_subtitle",
                variant="body",
                color=AppPalette.ON_SURFACE_VARIANT,
                text_align=text_align_mode,
            ),
            ft.Container(height=24),
            ft.Row(
                controls=[
                    AppButton(
                        value_key="explore_services",
                        variant="filled",
                        on_click=lambda e: page.navigate("/services"),
                        style=ft.ButtonStyle(
                            bgcolor=AppPalette.PRIMARY,
                            color=AppPalette.ON_PRIMARY,
                            padding=ft.Padding.symmetric(horizontal=28, vertical=16),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            shadow_color=ft.Colors.with_opacity(0.2, AppPalette.PRIMARY),
                            elevation=4,
                        ),
                    ),
                    AppButton(
                        value_key="contact_sales",
                        variant="outlined",
                        on_click=lambda e: page.navigate("/contact"),
                        style=ft.ButtonStyle(
                            color=AppPalette.PRIMARY,
                            padding=ft.Padding.symmetric(horizontal=28, vertical=16),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            side=ft.BorderSide(1.5, AppPalette.PRIMARY),
                        ),
                    ),
                ],
                spacing=12,
                alignment=main_align_mode,
                wrap=True,
            ),
        ],
        spacing=0,
        expand=not (is_mobile or is_tablet),
    )

    hero_image_container = ft.Container(
        content=ft.Image(
            src="images/banner.png",
            fit=ft.BoxFit.COVER,
            border_radius=ft.BorderRadius.all(16),
        ),
        expand=not (is_mobile or is_tablet),
        height=260 if is_mobile else (360 if is_tablet else 440),
        alignment=ft.Alignment.CENTER,
        border_radius=ft.BorderRadius.all(16),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=24,
            color=ft.Colors.with_opacity(0.08, ft.Colors.BLACK),
            offset=ft.Offset(0, 8),
        ),
    )

    hero_layout = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[hero_text_column, hero_image_container],
        spacing=32,
    ) if (is_mobile or is_tablet) else ft.Row(
        controls=[
            hero_text_column,
            ft.Container(width=48),
            hero_image_container,
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    hero_section = ft.Container(
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=40 if is_mobile else 64,
        ),
        content=PopInContainer(
            content=hero_layout,
            is_active=hero_revealed,
            duration=500,
        ),
    )

    # ── Capabilities Section ──────────────────────────────────────────────────
    capabilities_header = ft.Column(
        horizontal_alignment=cross_align_mode,
        controls=[
            ft.Container(
                content=AppText(
                    value_key="our_capabilities",
                    variant="h1",
                    bold=True,
                    color=AppPalette.ON_SURFACE,
                    text_align=text_align_mode,
                ),
            ),
            ft.Container(height=8),
            AppText(
                value_key="capabilities_subtitle",
                variant="body",
                color=AppPalette.ON_SURFACE_VARIANT,
                text_align=text_align_mode,
            ),
        ],
        spacing=0,
    )

    capabilities_grid = ft.ResponsiveRow(
        controls=[
            CapabilityBlock(
                icon=ft.Icons.CLOUD_DONE_OUTLINED,
                title_key="cloud_title",
                desc_key="cloud_desc",
                tags=["AWS", "Azure", "Docker", "CI/CD"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=capabilities_revealed,
            ),
            CapabilityBlock(
                icon=ft.Icons.CODE_ROUNDED,
                title_key="custom_software_title",
                desc_key="custom_software_desc",
                tags=["ERP", "POS", "Enterprise Workflows"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=capabilities_revealed,
            ),
            CapabilityBlock(
                icon=ft.Icons.DEVELOPER_BOARD_OUTLINED,
                title_key="mobile_eng_title",
                desc_key="mobile_eng_desc",
                tags=["IoT", "Embedded", "Sensors", "PCB"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=capabilities_revealed,
            ),
            CapabilityBlock(
                icon=ft.Icons.MEMORY_OUTLINED,
                title_key="ai_ml_title",
                desc_key="ai_ml_desc",
                tags=["LLM", "Computer Vision", "Automation"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=capabilities_revealed,
            ),
        ],
        spacing=20,
        run_spacing=20,
    )

    capabilities_section = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOW,
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=48 if is_mobile else 64,
        ),
        content=PopInContainer(
            content=ft.Column(
                horizontal_alignment=cross_align_mode,
                controls=[
                    capabilities_header,
                    ft.Container(height=32),
                    capabilities_grid,
                ],
                spacing=0,
            ),
            is_active=capabilities_revealed,
            duration=500,
        ),
    )

    # ── Contact CTA Section ───────────────────────────────────────────────────
    contact_cta_section = ft.Container(
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=48 if is_mobile else 64,
        ),
        content=PopInContainer(
            content=ft.Container(
                bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
                border=ft.Border.all(1, AppPalette.OUTLINE_VARIANT),
                border_radius=ft.BorderRadius.all(16),
                padding=ft.Padding.symmetric(
                    horizontal=24 if is_mobile else 48,
                    vertical=36 if is_mobile else 48,
                ),
                shadow=ft.BoxShadow(
                    spread_radius=0,
                    blur_radius=12,
                    color=ft.Colors.with_opacity(0.04, ft.Colors.BLACK),
                    offset=ft.Offset(0, 4),
                ),
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
                            value_key="contact_sales",
                            variant="h1",
                            bold=True,
                            color=AppPalette.ON_SURFACE,
                            text_align=text_align_mode,
                        ),
                        ft.Container(height=8),
                        AppText(
                            value_key="capabilities_subtitle",
                            variant="body",
                            color=AppPalette.ON_SURFACE_VARIANT,
                            text_align=text_align_mode,
                        ),
                        ft.Container(height=24),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Icon(ft.Icons.EMAIL_OUTLINED, size=18, color=AppPalette.PRIMARY),
                                                bgcolor=AppPalette.PRIMARY_FIXED,
                                                padding=ft.Padding.all(8),
                                                border_radius=ft.BorderRadius.all(8),
                                            ),
                                            ft.Text(
                                                "rangoonx.com@gmail.com",
                                                size=14,
                                                weight=ft.FontWeight.W_600,
                                                color=AppPalette.ON_SURFACE,
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                ),
                                ft.Container(width=20 if not is_mobile else 0, height=0 if not is_mobile else 8),
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Container(
                                                content=ft.Icon(ft.Icons.LOCATION_ON_OUTLINED, size=18, color=AppPalette.PRIMARY),
                                                bgcolor=AppPalette.PRIMARY_FIXED,
                                                padding=ft.Padding.all(8),
                                                border_radius=ft.BorderRadius.all(8),
                                            ),
                                            ft.Text(
                                                "Yangon, Myanmar",
                                                size=14,
                                                weight=ft.FontWeight.W_600,
                                                color=AppPalette.ON_SURFACE,
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                ),
                            ],
                            alignment=main_align_mode,
                            wrap=True,
                        ),
                        ft.Container(height=28),
                        AppButton(
                            value_key="contact_sales",
                            variant="filled",
                            on_click=lambda e: page.navigate("/contact"),
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
                    spacing=0,
                ),
            ),
            is_active=contact_revealed,
            duration=600,
        ),
    )

    return ft.ListView(
        expand=True,
        spacing=0,
        controls=[
            hero_section,
            capabilities_section,
            contact_cta_section,
            AppFooter(),
        ],
    )
