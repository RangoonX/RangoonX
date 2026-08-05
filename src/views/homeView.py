import flet as ft
from components.typography import AppText, AppButton
from config.colors import AppPalette
from models.app_route_model import LocalizationContext


@ft.component
def PopInContainer(content, is_active: bool = True, duration: int = 500, initial_scale: float = 0.88):
    """
    Reusable Scroll Reveal Pop-in Animation component.
    Scales and fades in content smoothly when is_active is True.
    """
    return ft.Container(
        content=content,
        opacity=1.0 if is_active else 0.0,
        scale=1.0 if is_active else initial_scale,
        animate_opacity=ft.Animation(duration, ft.AnimationCurve.EASE_OUT),
        animate_scale=ft.Animation(duration, ft.AnimationCurve.EASE_OUT_BACK),
    )


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
    """
    Interactive Capability Block with Scroll Reveal Pop-in animation & hover feedback.
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
            left=ft.BorderSide(3, AppPalette.PRIMARY if is_hovered else AppPalette.OUTLINE_VARIANT)
        ),
        padding=ft.Padding.symmetric(horizontal=24, vertical=20),
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
                        ft.Icon(icon, size=28, color=AppPalette.PRIMARY),
                        ft.Container(width=8),
                        AppText(value_key=title_key, variant="h3", bold=True, color=AppPalette.ON_SURFACE),
                    ],
                    alignment=main_align_mode,
                ),
                ft.Container(height=4),
                AppText(
                    value_key=desc_key,
                    variant="body",
                    color=AppPalette.ON_SURFACE_VARIANT,
                    text_align=text_align_mode,
                ),
                ft.Container(height=8) if badge_controls else ft.Container(),
                ft.Row(controls=badge_controls, spacing=8, alignment=main_align_mode) if badge_controls else ft.Container(),
            ],
            spacing=6,
        ),
        col={"sm": 12, "md": col_span, "lg": col_span},
    )


HAS_CHOSEN_LANG = False


@ft.component
def homeView():
    global HAS_CHOSEN_LANG
    page = ft.context.page
    width = page.width if page and page.width else 1200

    is_mobile = width < 768
    is_tablet = 768 <= width < 1024

    text_align_mode = ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT
    cross_align_mode = ft.CrossAxisAlignment.CENTER if is_mobile else ft.CrossAxisAlignment.START
    main_align_mode = ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START

    # ── Scroll Reveal State Management ──────────────────────────────────────────
    hero_revealed, set_hero_revealed = ft.use_state(True)
    capabilities_revealed, set_capabilities_revealed = ft.use_state(not is_mobile)
    contact_revealed, set_contact_revealed = ft.use_state(not is_mobile)

    def handle_scroll(e: ft.OnScrollEvent):
        if is_mobile:
            pos = e.extent_before
            if pos >= 80 and not capabilities_revealed:
                set_capabilities_revealed(True)
            if pos >= 320 and not contact_revealed:
                set_contact_revealed(True)

    # ── 1. Hero Section ────────────────────────────────────────────────────────
    hero_text_column = ft.Column(
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
                value_key="hero_title",
                variant="h1",
                bold=True,
                color=AppPalette.ON_SURFACE,
                text_align=text_align_mode,
            ),
            ft.Container(height=8),
            AppText(
                value_key="hero_subtitle",
                variant="body",
                color=AppPalette.ON_SURFACE_VARIANT,
                text_align=text_align_mode,
            ),
            ft.Container(height=16),
            ft.Row(
                controls=[
                    AppButton(
                        value_key="explore_services",
                        variant="filled",
                        on_click=lambda e: page.go("/services"),
                        style=ft.ButtonStyle(
                            bgcolor=AppPalette.PRIMARY,
                            color=AppPalette.ON_PRIMARY,
                            padding=ft.Padding.symmetric(horizontal=24, vertical=16),
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                    AppButton(
                        value_key="contact_sales",
                        variant="outlined",
                        on_click=lambda e: page.go("/contact"),
                        style=ft.ButtonStyle(
                            color=AppPalette.PRIMARY,
                            padding=ft.Padding.symmetric(horizontal=24, vertical=16),
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                ],
                spacing=16,
                alignment=main_align_mode,
                wrap=True,
            ),
        ],
        spacing=8,
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
    )

    hero_section = ft.Container(
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=28 if is_mobile else 52,
        ),
        content=PopInContainer(
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    hero_text_column,
                    hero_image_container,
                ],
                spacing=28,
            ) if (is_mobile or is_tablet) else ft.Row(
                controls=[
                    hero_text_column,
                    ft.Container(width=32),
                    hero_image_container,
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            is_active=hero_revealed,
            duration=500,
        ),
    )

    # ── 2. Capabilities Section ───────────────────────────────────────────
    capabilities_header = ft.Column(
        horizontal_alignment=cross_align_mode,
        controls=[
            AppText(
                value_key="our_capabilities",
                variant="h1",
                bold=True,
                color=AppPalette.ON_SURFACE,
                text_align=text_align_mode,
            ),
            AppText(
                value_key="capabilities_subtitle",
                variant="body",
                color=AppPalette.ON_SURFACE_VARIANT,
                text_align=text_align_mode,
            ),
        ],
        spacing=8,
    )

    capabilities_grid = ft.ResponsiveRow(
        controls=[
            CapabilityBlock(
                icon=ft.Icons.CLOUD_DONE_OUTLINED,
                title_key="cloud_title",
                desc_key="cloud_desc",
                tags=["Kubernetes", "Docker", "AWS"],
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
                tags=["Enterprise Workflows", "Scalable Architecture"],
                col_span=6,
                cross_align_mode=cross_align_mode,
                main_align_mode=main_align_mode,
                text_align_mode=text_align_mode,
                is_revealed=capabilities_revealed,
            ),
            CapabilityBlock(
                icon=ft.Icons.SMARTPHONE_OUTLINED,
                title_key="mobile_eng_title",
                desc_key="mobile_eng_desc",
                tags=["Flutter", "iOS & Android", "Native UI/UX"],
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
                tags=["Generative AI", "Predictive Analytics", "Python"],
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
            vertical=36 if is_mobile else 52,
        ),
        content=PopInContainer(
            content=ft.Column(
                horizontal_alignment=cross_align_mode,
                controls=[
                    capabilities_header,
                    ft.Container(height=16),
                    capabilities_grid,
                ],
                spacing=16,
            ),
            is_active=capabilities_revealed,
            duration=500,
        ),
    )

    # ── 3. Contact & Call-to-Action Section ─────────────────────────────────────
    contact_cta_section = ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=40 if is_mobile else 56,
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
                    ft.Container(height=20),
                    ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.EMAIL_OUTLINED, size=20, color=AppPalette.PRIMARY),
                                    ft.Text("contact@rangoonx.com", size=15, weight=ft.FontWeight.W_600, color=AppPalette.ON_SURFACE),
                                ],
                                spacing=8,
                            ),
                            ft.Container(width=16 if not is_mobile else 0, height=0 if not is_mobile else 8),
                            ft.Row(
                                controls=[
                                    ft.Icon(ft.Icons.LOCATION_ON_OUTLINED, size=20, color=AppPalette.PRIMARY),
                                    ft.Text("Yangon, Myanmar", size=15, weight=ft.FontWeight.W_600, color=AppPalette.ON_SURFACE),
                                ],
                                spacing=8,
                            ),
                        ],
                        alignment=main_align_mode,
                        wrap=True,
                    ),
                    ft.Container(height=24),
                    AppButton(
                        value_key="contact_sales",
                        variant="filled",
                        on_click=lambda e: page.go("/contact"),
                        style=ft.ButtonStyle(
                            bgcolor=AppPalette.PRIMARY,
                            color=AppPalette.ON_PRIMARY,
                            padding=ft.Padding.symmetric(horizontal=32, vertical=18),
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                ],
                spacing=4,
            ),
            is_active=contact_revealed,
            duration=600,
        ),
    )

    # ── 4. Footer Section ──────────────────────────────────────────────────
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

    # ── Overall Main Layout Scrollable Container with Scroll Reveal ────────────────
    return ft.ListView(
        expand=True,
        spacing=0,
        on_scroll=handle_scroll,
        controls=[
            hero_section,
            capabilities_section,
            contact_cta_section,
            footer_section,
        ]
    )