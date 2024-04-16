import flet as ft


def main(page: ft.Page):

    page.title = "Othello"

    # ウィンドウの上下左右から中央に配置する
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    cell = ft.Container(
        bgcolor=ft.colors.GREEN,
        width=75,
        height=75,
        border_radius=10,
        on_click=lambda e: print("Clickable without Ink clicked!"),
    )

    culumn = []
    for i in range(8):
        culumn.append(cell)

    row = []
    for i in range(8):
        row.append(ft.Row(culumn))

    page.add(
        ft.Column(
            row
        )
    )


ft.app(target=main)
