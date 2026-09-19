import flet as ft
from components.typography import AppText, AppButton
from config.colors import AppPalette


@ft.component
def four_zero_four():
    page = ft.context.page

    is_visible, set_is_visible = ft.use_state(False)

    def trigger_animation():
        set_is_visible(True)

    ft.on_updated(trigger_animation, [])

    return ft.Container(
        alignment=ft.Alignment.CENTER,
        expand=True,
        bgcolor=AppPalette.SURFACE,
        padding=ft.Padding.all(32),
        content=ft.Container(
            opacity=1.0 if is_visible else 0.0,
            scale=1.0 if is_visible else 0.9,
            animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(500, ft.AnimationCurve.EASE_OUT_BACK),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "404",
                        size=80,
                        weight=ft.FontWeight.W_900,
                        color=AppPalette.PRIMARY,
                    ),
                    ft.Container(height=8),
                    ft.Text(
                        "Page Not Found",
                        size=20,
                        weight=ft.FontWeight.W_600,
                        color=AppPalette.ON_SURFACE,
                    ),
                    ft.Container(height=8),
                    ft.Text(
                        "The page you're looking for doesn't exist or has been moved.",
                        size=14,
                        color=AppPalette.ON_SURFACE_VARIANT,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=28),
                    AppButton(
                        value_key="nav_home",
                        variant="filled",
                        icon=ft.Icons.HOME_OUTLINED,
                        on_click=lambda e: page.navigate("/"),
                        style=ft.ButtonStyle(
                            bgcolor=AppPalette.PRIMARY,
                            color=AppPalette.ON_PRIMARY,
                            padding=ft.Padding.symmetric(horizontal=28, vertical=14),
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                    ),
                ],
                spacing=0,
            ),
        ),
    )
