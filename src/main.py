import os
import flet as ft
from config import (fonts , colors)
from core.routerApp import routingApp


async def main(page: ft.Page):
    
    
    page.title = f"RangoonX {'| Software House' if ft.context.page.route == '/' else ft.context.page.route}"
    page.window.icon = r"images/favicon.png"
    page.fonts = fonts.AppFonts.FONTS_MAPPING
    page.theme = colors.get_app_theme(ft.ThemeMode.LIGHT)
    page.dark_theme = colors.get_app_theme(ft.ThemeMode.DARK)
    page.render(routingApp)
    page.padding = 0
    
    

    
if __name__ == "__main__":
    ft.run(main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)

