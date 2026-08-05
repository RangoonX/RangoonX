# src/components/splashScreen.py

import flet as ft
from config.colors import AppPalette


@ft.component
def SplashScreen():
    """
    App Initial Loading & Splash Screen with RangoonX logo, favicon.png, and pulsing animation.
    """
    is_animating, set_is_animating = ft.use_state(False)

    def trigger_animation():
        set_is_animating(True)

    ft.on_updated(trigger_animation, [])

    return ft.Container(
        expand=True,
        bgcolor=AppPalette.SURFACE,
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.all(24),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Pulsing RangoonX Logo & Favicon Container
                ft.Container(
                    content=ft.Stack(
                        controls=[
                            ft.Image(
                                src="images/rangoonX_logo.png",
                                width=140,
                                height=140,
                                fit=ft.BoxFit.CONTAIN,
                            ),
                            ft.Image(
                                src="images/favicon.png",
                                width=36,
                                height=36,
                                right=0,
                                bottom=0,
                            ),
                        ],
                    ),
                    scale=1.1 if is_animating else 0.85,
                    opacity=1.0 if is_animating else 0.0,
                    animate_scale=ft.Animation(800, ft.AnimationCurve.EASE_OUT_BACK),
                    animate_opacity=ft.Animation(600, ft.AnimationCurve.EASE_IN),
                ),
                ft.Container(height=24),
                # Brand Title
                ft.Text(
                    "RangoonX",
                    size=28,
                    weight=ft.FontWeight.W_900,
                    color=AppPalette.PRIMARY,
                ),
                ft.Text(
                    "PRECISION ENGINEERING",
                    size=12,
                    weight=ft.FontWeight.BOLD,
                    color=AppPalette.ON_SURFACE_VARIANT,
                ),
                ft.Container(height=32),
                # Modern Progress Indicator
                ft.ProgressRing(
                    width=28,
                    height=28,
                    stroke_width=3,
                    color=AppPalette.PRIMARY,
                ),
            ],
            spacing=4,
        ),
    )
