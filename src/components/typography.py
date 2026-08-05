#/src/components/typography.py

import flet as ft
from models.app_route_model import LocalizationContext

from config.fonts import AppFonts

@ft.component
def AppText(
    value_key: str, 
    variant: str = "body", 
    bold: bool = False,
    **kwargs
):
    """
    Custom Typography component that handles localization and font scaling automatically.
    
    Args:
        value_key (str): The translation key from the JSON file.
        variant (str): 'h1', 'h2', 'h3', 'body', 'caption'. Defaults to 'body'.
        bold (bool): Set True to use Padauk-Bold font family automatically.
        **kwargs: Additional ft.Text arguments (color, weight, font_family, etc.)
    """
    loc = ft.use_context(LocalizationContext)
    
    # Pre-defined sizes for different variants
    sizes = {
        "h1": 32,
        "h2": 24,
        "h3": 20,
        "body": 16,
        "caption": 12
    }
    
    base_size = sizes.get(variant, 16)
    
    # Calculate responsive scale based on viewport width
    page_width = ft.context.page.width if ft.context.page and ft.context.page.width else 1024
    
    if page_width < 600:         # Mobile View
        responsive_scale = 0.85
    elif page_width < 1024:      # Tablet View
        responsive_scale = 1.0
    else:                        # Desktop View
        responsive_scale = 1.15
        
    # Calculate final size based on localization font_scale and responsive_scale
    final_size = base_size * loc.font_scale * responsive_scale
    
    # Automatically set Padauk-Bold font_family when bold=True or weight is bold
    if "font_family" not in kwargs:
        if bold or kwargs.get("weight") in ("bold", ft.FontWeight.BOLD, "w700", "w800", "w900"):
            kwargs["font_family"] = AppFonts.MYANMAR_BOLD
    
    return ft.Text(
        value=loc.get(value_key),
        size=final_size,
        **kwargs
    )


@ft.component
def AppButton(
    value_key: str = None,
    text: str = None,
    content: str | ft.Control = None,
    variant: str = "button",
    bold: bool = True,
    **kwargs
):
    """
    Custom Button component that handles localization and font scaling automatically,
    while inheriting all parameters supported by ft.Button (on_click, icon, style, width, height, etc.).
    
    Args:
        value_key (str): Translation key from localization JSON files.
        text (str): Direct raw text if localization key is not used.
        content (str | ft.Control): Custom content control or string for button label.
        variant (str): Button style variant ('button', 'filled', 'elevated', 'outlined', 'text', 'filled_tonal').
        bold (bool): Whether the button text uses bold typography automatically.
        **kwargs: All parameters supported by ft.Button (on_click, style, icon, width, height, disabled, etc.)
    """
    loc = ft.use_context(LocalizationContext)
    
    # Resolve button label content
    if content is None:
        if value_key:
            content = loc.get(value_key)
        elif text:
            content = text

    button_classes = {
        "button": ft.Button,
        "filled": ft.FilledButton,
        "elevated": ft.ElevatedButton,
        "outlined": ft.OutlinedButton,
        "text": ft.TextButton,
        "filled_tonal": ft.FilledTonalButton,
    }
    
    button_cls = button_classes.get(str(variant).lower(), ft.Button)
    
    if content is not None:
        kwargs["content"] = content

    return button_cls(**kwargs)
