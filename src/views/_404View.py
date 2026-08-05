
#src/views/404View.py


import flet as ft 


@ft.component
def four_zero_four():
    
    return ft.Container(
        alignment=ft.Alignment.CENTER,
        expand=True,
        content= ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("404",color= ft.Colors.GREEN, font_family="Padauk-Regular",weight=30,size=70),
                ft.Text("Not Found")
            ]
        )
    )