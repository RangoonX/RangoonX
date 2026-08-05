# src/config/colors.py

import flet as ft
from config.fonts import AppFonts


class AppPalette:
    """
    RangoonX Design System Color Palette derived from docs/agent/theme_design.md
    """

    # Brand Specific Highlights
    BRAND_PRIMARY_BLUE = "#0088CC"
    BRAND_CHARCOAL = "#1A1C1E"
    BRAND_CYAN = "#00D1FF"

    # Surface Colors
    SURFACE = "#F7F9FB"
    SURFACE_DIM = "#D8DADC"
    SURFACE_BRIGHT = "#F7F9FB"
    SURFACE_CONTAINER_LOWEST = "#FFFFFF"
    SURFACE_CONTAINER_LOW = "#F2F4F6"
    SURFACE_CONTAINER = "#ECEEF0"
    SURFACE_CONTAINER_HIGH = "#E6E8EA"
    SURFACE_CONTAINER_HIGHEST = "#E0E3E5"
    ON_SURFACE = "#191C1E"
    ON_SURFACE_VARIANT = "#3F4850"
    INVERSE_SURFACE = "#2D3133"
    INVERSE_ON_SURFACE = "#EFF1F3"
    SURFACE_VARIANT = "#E0E3E5"
    SURFACE_TINT = "#006497"

    # Outline / Borders
    OUTLINE = "#6F7881"
    OUTLINE_VARIANT = "#BFC7D2"

    # Primary Colors
    PRIMARY = "#006193"
    ON_PRIMARY = "#FFFFFF"
    PRIMARY_CONTAINER = "#007BB9"
    ON_PRIMARY_CONTAINER = "#FDFCFF"
    INVERSE_PRIMARY = "#92CCFF"

    # Secondary Colors
    SECONDARY = "#5D5E61"
    ON_SECONDARY = "#FFFFFF"
    SECONDARY_CONTAINER = "#E2E2E5"
    ON_SECONDARY_CONTAINER = "#636467"

    # Tertiary Colors
    TERTIARY = "#00647C"
    ON_TERTIARY = "#FFFFFF"
    TERTIARY_CONTAINER = "#007F9C"
    ON_TERTIARY_CONTAINER = "#FAFDFF"

    # Error Colors
    ERROR = "#BA1A1A"
    ON_ERROR = "#FFFFFF"
    ERROR_CONTAINER = "#FFDAD6"
    ON_ERROR_CONTAINER = "#93000A"

    # Primary Fixed Colors
    PRIMARY_FIXED = "#CCE5FF"
    PRIMARY_FIXED_DIM = "#92CCFF"
    ON_PRIMARY_FIXED = "#001D31"
    ON_PRIMARY_FIXED_VARIANT = "#004B73"

    # Secondary Fixed Colors
    SECONDARY_FIXED = "#E2E2E5"
    SECONDARY_FIXED_DIM = "#C6C6C9"
    ON_SECONDARY_FIXED = "#1A1C1E"
    ON_SECONDARY_FIXED_VARIANT = "#454749"

    # Tertiary Fixed Colors
    TERTIARY_FIXED = "#B7EAFF"
    TERTIARY_FIXED_DIM = "#4CD6FF"
    ON_TERTIARY_FIXED = "#001F28"
    ON_TERTIARY_FIXED_VARIANT = "#004E60"

    # Background Colors
    BACKGROUND = "#F7F9FB"
    ON_BACKGROUND = "#191C1E"

    # Shortcuts for components / backward compatibility
    L_BG = SURFACE
    L_SURFACE = SURFACE_CONTAINER_LOWEST
    L_PRIMARY = PRIMARY
    L_TEXT = ON_SURFACE
    L_SECONDARY = SECONDARY
    L_BORDER = OUTLINE_VARIANT

    D_BG = "#0C1117"
    D_SURFACE = "#161B22"
    D_PRIMARY = INVERSE_PRIMARY
    D_TEXT = INVERSE_ON_SURFACE
    D_SECONDARY = SECONDARY_FIXED_DIM
    D_BORDER = ON_SURFACE_VARIANT


def get_app_theme(mode: ft.ThemeMode = ft.ThemeMode.LIGHT) -> ft.Theme:
    """
    Generates a Flet Theme object based on RangoonX Design System (Material 3 spec).
    """
    if mode == ft.ThemeMode.LIGHT:
        color_scheme = ft.ColorScheme(
            surface=AppPalette.SURFACE,
            surface_dim=AppPalette.SURFACE_DIM,
            surface_bright=AppPalette.SURFACE_BRIGHT,
            surface_container_lowest=AppPalette.SURFACE_CONTAINER_LOWEST,
            surface_container_low=AppPalette.SURFACE_CONTAINER_LOW,
            surface_container=AppPalette.SURFACE_CONTAINER,
            surface_container_high=AppPalette.SURFACE_CONTAINER_HIGH,
            surface_container_highest=AppPalette.SURFACE_CONTAINER_HIGHEST,
            on_surface=AppPalette.ON_SURFACE,
            on_surface_variant=AppPalette.ON_SURFACE_VARIANT,
            inverse_surface=AppPalette.INVERSE_SURFACE,
            on_inverse_surface=AppPalette.INVERSE_ON_SURFACE,
            outline=AppPalette.OUTLINE,
            outline_variant=AppPalette.OUTLINE_VARIANT,
            surface_tint=AppPalette.SURFACE_TINT,
            primary=AppPalette.PRIMARY,
            on_primary=AppPalette.ON_PRIMARY,
            primary_container=AppPalette.PRIMARY_CONTAINER,
            on_primary_container=AppPalette.ON_PRIMARY_CONTAINER,
            inverse_primary=AppPalette.INVERSE_PRIMARY,
            secondary=AppPalette.SECONDARY,
            on_secondary=AppPalette.ON_SECONDARY,
            secondary_container=AppPalette.SECONDARY_CONTAINER,
            on_secondary_container=AppPalette.ON_SECONDARY_CONTAINER,
            tertiary=AppPalette.TERTIARY,
            on_tertiary=AppPalette.ON_TERTIARY,
            tertiary_container=AppPalette.TERTIARY_CONTAINER,
            on_tertiary_container=AppPalette.ON_TERTIARY_CONTAINER,
            error=AppPalette.ERROR,
            on_error=AppPalette.ON_ERROR,
            error_container=AppPalette.ERROR_CONTAINER,
            on_error_container=AppPalette.ON_ERROR_CONTAINER,
            primary_fixed=AppPalette.PRIMARY_FIXED,
            primary_fixed_dim=AppPalette.PRIMARY_FIXED_DIM,
            on_primary_fixed=AppPalette.ON_PRIMARY_FIXED,
            on_primary_fixed_variant=AppPalette.ON_PRIMARY_FIXED_VARIANT,
            secondary_fixed=AppPalette.SECONDARY_FIXED,
            secondary_fixed_dim=AppPalette.SECONDARY_FIXED_DIM,
            on_secondary_fixed=AppPalette.ON_SECONDARY_FIXED,
            on_secondary_fixed_variant=AppPalette.ON_SECONDARY_FIXED_VARIANT,
            tertiary_fixed=AppPalette.TERTIARY_FIXED,
            tertiary_fixed_dim=AppPalette.TERTIARY_FIXED_DIM,
            on_tertiary_fixed=AppPalette.ON_TERTIARY_FIXED,
            on_tertiary_fixed_variant=AppPalette.ON_TERTIARY_FIXED_VARIANT,
        )
    else:
        color_scheme = ft.ColorScheme(
            primary=AppPalette.D_PRIMARY,
            surface=AppPalette.D_BG,
            on_surface=AppPalette.D_TEXT,
            secondary=AppPalette.D_SECONDARY,
            outline=AppPalette.D_BORDER,
        )

    return ft.Theme(
        font_family=AppFonts.DEFAULT_FAMILY,
        color_scheme=color_scheme,
    )
