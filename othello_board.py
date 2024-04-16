import flet as ft


def main(page: ft.Page):
    page.title = "Reversi"

    # ウィンドウの上下左右から中央に配置する
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # 背景を描画(page)
    page.add(ft.Rectangle(width=500, height=500, fill="green"))


ft.app(target=main)
