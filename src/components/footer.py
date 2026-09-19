import flet as ft
from components.typography import AppText
from config.colors import AppPalette
from core.helper import use_screen_context


@ft.component
def AppFooter():
    screen = use_screen_context()

    is_mobile = screen.is_mobile
    is_tablet = screen.is_tablet

    text_align_mode = ft.TextAlign.CENTER if is_mobile else ft.TextAlign.LEFT
    cross_align_mode = ft.CrossAxisAlignment.CENTER if is_mobile else ft.CrossAxisAlignment.START
    main_align_mode = ft.MainAxisAlignment.CENTER if is_mobile else ft.MainAxisAlignment.START

    return ft.Container(
        bgcolor=AppPalette.SURFACE_CONTAINER_LOWEST,
        border=ft.Border.only(top=ft.BorderSide(1, AppPalette.OUTLINE_VARIANT)),
        padding=ft.Padding.symmetric(
            horizontal=20 if is_mobile else (36 if is_tablet else 64),
            vertical=32,
        ),
        content=ft.Column(
            horizontal_alignment=cross_align_mode,
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="images/favicon.png",
                                        width=20,
                                        height=20,
                                        fit=ft.BoxFit.CONTAIN,
                                    ),
                                    AppText(
                                        value_key="brand_name",
                                        variant="h3",
                                        bold=True,
                                        color=AppPalette.PRIMARY,
                                    ),
                                ],
                                spacing=8,
                            ),
                        ),
                        ft.Container(
                            width=1,
                            height=20,
                            bgcolor=AppPalette.OUTLINE_VARIANT,
                        ),
                        AppText(
                            value_key="footer_slogan",
                            variant="caption",
                            color=AppPalette.ON_SURFACE_VARIANT,
                        ),
                    ],
                    alignment=main_align_mode,
                    wrap=True,
                    spacing=12,
                ),
                ft.Container(height=16),
                ft.Divider(color=AppPalette.OUTLINE_VARIANT, height=1),
                ft.Container(height=12),
                AppText(
                    value_key="copyright",
                    variant="caption",
                    color=AppPalette.ON_SURFACE_VARIANT,
                    text_align=text_align_mode,
                ),
            ],
            spacing=0,
        ),
    )
