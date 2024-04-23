import flet as ft


def main(page: ft.Page):

    page.title = "Othello"

    # ウィンドウの上下左右から中央に配置する
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # オセロ盤のマスを作成
    row = []
    board = []

    for i in range(8):
        for j in range(8):
            culumn = ft.Container(
                bgcolor=ft.colors.GREEN,
                width=75,
                height=75,
                border_radius=10,
                on_click=lambda e: print(f"place {i},{j}")
            )
            row.append(culumn)
            print(i, j)
        board.append(ft.Row(row))

    # オセロ盤をページに追加
    page.add(ft.Column(board))


ft.app(target=main)
