import flet as ft

def main(page: ft.Page):
    page.title = "Seleccionar método"
    page.bgcolor = "#f1f7f9"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.fonts = {
        "Montserrat": "https://fonts.gstatic.com/s/montserrat/v25/JTUQjIg1_i6t8kCHKm45_QphziTn89dtpQ.woff2"
    }
    page.font_family = "Montserrat"

    # ---------- FUNCION PARA TARJETAS ----------
    def card(icon_path, title, subtitle):
        return ft.Container(
            width=390,
            padding=28,
            border_radius=22,
            border=ft.border.all(2, "#4a6f3b"),
            bgcolor="#ffffff",
            content=ft.Column(
                alignment="center",
                horizontal_alignment="center",
                spacing=16,
                controls=[
                    # 🔽 AQUI VA LA IMAGEN (ICONO)
                    ft.Image(
                        src=icon_path,
                        width=68,
                        height=68,
                    ),
                    ft.Text(title, size=22, weight="bold", color="black", font_family="Montserrat"),
                    ft.Text(subtitle, size=15, color="black", font_family="Montserrat"),
                    ft.ElevatedButton(
                        "Seleccionar",
                        bgcolor="#a8c66c",
                        color="black",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=16,
                            text_style=ft.TextStyle(size=16, font_family="Montserrat", weight="bold")
                        )
                    )
                ]
            )
        )

    # ---------- CONTENIDO PRINCIPAL ----------
    page.add(
        ft.Column(
            alignment="center",
            horizontal_alignment="center",
            spacing=32,
            controls=[
                ft.Text(
                    "Selecciona tú método de comunicación",
                    size=32,
                    weight="bold",
                    text_align="center",
                    color="black",
                    font_family="Montserrat"
                ),
                ft.Text(
                    "Escoge como deseas interactuar con la aplicación",
                    size=18,
                    color="black",
                    font_family="Montserrat"
                ),
                ft.Row(
                    alignment="center",
                    spacing=32,
                    controls=[
                        # 🔽 TARJETA 1 (GESTOS)
                        card(
                            "assets/hand.png",  # <-- ICONO MANO
                            "Comunicación por gestos",
                            "Comunicación mediante movimiento y señas"
                        ),
                        # 🔽 TARJETA 2 (AUDIO, SIN ICONO)
                            card(
                                "assets/mic.png",  # <-- ICONO MICROFONO
                                "Comunicación por audio",
                                "Interacción utilizando la voz y micrófono"
                            ),
                    ]
                )
            ]
        )
    )

ft.app(target=main)