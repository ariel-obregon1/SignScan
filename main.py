import ssl
ssl._create_default_https_context = ssl._create_unverified_context
 
import flet as ft
 
# COLORES
VERDE = "#4E7D35"
VERDE_CLARO = "#A8C66C"
GRIS = "#CFCFCF"
FONDO = "#F5F5F5"
 
def main(page: ft.Page):
    page.title = "SignScan"
    page.window_width = 400
    page.window_height = 700
    page.bgcolor = FONDO
 
    # -------- CAMBIO DE PANTALLAS --------
    def cambiar(vista):
        page.controls.clear()
 
        if vista == "inicio":
            page.add(pantalla_inicio())
        elif vista == "login":
            page.add(pantalla_login())
        elif vista == "registro":
            page.add(pantalla_registro())
        elif vista == "perfil":
            page.add(pantalla_perfil())
 
        page.update()
 
    # -------- HEADER --------
    def header(titulo, subtitulo=""):
        return ft.Container(
            bgcolor=VERDE,
            width=400,
            height=140,
            content=ft.Column(
                [
                    ft.Text(titulo, size=34, color="white", weight="bold"),
                    ft.Text(subtitulo, size=18, color="white"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
 
    # -------- PANTALLA INICIO --------
    def pantalla_inicio():
        return ft.Column(
            [
                ft.Image(src="signscan/Assets/logo.png", width=220),
 
                ft.ElevatedButton(
                    "Continuar",
                    width=200,
                    on_click=lambda e: cambiar("login")
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
 
    # -------- PANTALLA LOGIN --------
    def pantalla_login():
        correo = ft.TextField(width=280, bgcolor=GRIS, color="black")
        password = ft.TextField(width=280, bgcolor=GRIS, color="black", password=True)
 
        return ft.Column(
            [
                header("SignScan", "Bienvenido usuario"),
 
                ft.Container(height=20),
 
                ft.Image(src="/Assets/user.png", width=100),
 
                ft.Container(height=20),
 
                ft.Text("Correo", color="black"),
                correo,
 
                ft.Text("Contraseña", color="black"),
                password,
 
                ft.Container(height=20),
 
                ft.ElevatedButton(
                    "Iniciar sesión",
                    bgcolor=VERDE_CLARO,
                    color="black",
                    width=220,
                    on_click=lambda e: cambiar("perfil")
                ),
 
                ft.TextButton(
                    "Registrar una cuenta",
                    on_click=lambda e: cambiar("registro")
                ),
 
                ft.Container(height=20),
 
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: cambiar("inicio")
                        ),
                        ft.IconButton(
                            icon=ft.Icons.ARROW_FORWARD,
                            on_click=lambda e: cambiar("perfil")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
 
    # -------- PANTALLA REGISTRO --------
    def pantalla_registro():
        usuario = ft.TextField(width=280, bgcolor=GRIS, color="black")
        correo = ft.TextField(width=280, bgcolor=GRIS, color="black")
        password = ft.TextField(width=280, bgcolor=GRIS, color="black", password=True)
        fecha = ft.TextField(width=280, bgcolor=GRIS, color="black")
 
        return ft.Column(
            [
                header("Crear cuenta"),
 
                ft.Container(height=20),
 
                ft.Text("Nombre", color="black"),
                usuario,
 
                ft.Text("Correo", color="black"),
                correo,
 
                ft.Text("Contraseña", color="black"),
                password,
 
                ft.Text("Fecha", color="black"),
                fecha,
 
                ft.Container(height=20),
 
                ft.ElevatedButton(
                    "Registrarse",
                    bgcolor=VERDE_CLARO,
                    color="black",
                    width=220
                ),
 
                ft.Container(height=20),
 
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: cambiar("login")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
 
    # -------- PANTALLA PERFIL --------
    def pantalla_perfil():
        return ft.Column(
            [
                header("Elige tu perfil"),
 
                ft.Container(height=30),
 
                ft.Image(src="Assets/perfil.png", width=120),
 
                ft.Text("Crea tu perfil", size=18),
 
                ft.Container(height=20),
 
                ft.Text("Elige una foto de tu galeria"),
 
                ft.Container(height=20),
 
                ft.Image(src="Assets/imagen.png", width=80),
 
                ft.Container(height=40),
 
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: cambiar("login")
                        ),
                        ft.IconButton(
                            icon=ft.Icons.ARROW_FORWARD,
                            on_click=lambda e: cambiar("perfil")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
 
    cambiar("inicio")
 
ft.app(target=main)