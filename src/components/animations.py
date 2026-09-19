import flet as ft


@ft.component
def PopInContainer(content, is_active: bool = True, duration: int = 500, initial_scale: float = 0.88):
    return ft.Container(
        content=content,
        opacity=1.0 if is_active else 0.0,
        scale=1.0 if is_active else initial_scale,
        animate_opacity=ft.Animation(duration, ft.AnimationCurve.EASE_OUT),
        animate_scale=ft.Animation(duration, ft.AnimationCurve.EASE_OUT_BACK),
    )
