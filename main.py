import flet as ft
from random import choice
from clipboard import copy

def main(page: ft.Page):
    page.window_width = 750
    page.window_height = 450
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False
    page.window_frameless = True
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT

    ######### Backend ##########
    def make_password():
        base = "abcdefghijklmnopqrstuvwxyz"
        pswd = ""
        if include_numbers_box.value:
            base += "1234567890"
        if include_capitals_box.value:
            base += "abcdefghijklmnopqrstuvwxyz".upper()
        if include_special_box.value:
            base += """`-=[]\\;',./~!@#$%^&*()_+{}|:"<>?"""

        for _ in range(int(pswd_len.value)):
            pswd += choice(base)
        final_pswd.value = pswd
        final_pswd.update()
        copy(pswd)
        

    ######### Backend ##########


    page.fonts = {"interFont": "src/InterDisplay-Regular.ttf",
                  "interFontB": "src/Inter-ExtraBold.ttf"}

    title_bar = ft.WindowDragArea(ft.Container(bgcolor=ft.colors.TRANSPARENT, width=700, height=50, border_radius=10), left=0, top=0)
    def animate_btn(e):
        if e.data == 'true':
            close_btn.bgcolor = "#333333"
            close_btn.update()
        else:
            close_btn.bgcolor = "#000000"
            close_btn.update()

    close_btn = ft.Container(width=30, height=30, border_radius=15, bgcolor="#000000", alignment=ft.alignment.center, content=ft.Icon(ft.icons.CLOSE_ROUNDED, size=15), right=15, top=10, on_hover=animate_btn, on_click=lambda _:page.window_close(), animate=ft.animation.Animation(duration=150))

    title = ft.Text(value="Password Generator", font_family="interFontB", size=40, left=150, top=10, color="#ffffff")

    common_x = 260
    include_numbers_box = ft.Checkbox(label="", left=common_x, top=0, fill_color={ft.MaterialState.SELECTED: "#ff5050", "": "#000000"}, check_color="#ffffff", active_color="#ffffff", scale=1.1, hover_color="#000000")
    include_numbers_title = ft.Text(value="Include Numbers", font_family="interFont", left=include_numbers_box.left+35, top=include_numbers_box.top+5, size=15, color="#ffffff")

    include_capitals_box = ft.Checkbox(label="", left=common_x, top=include_numbers_box.top+50, fill_color={ft.MaterialState.SELECTED: "#ff5050", "": "#000000"}, check_color="#ffffff", active_color="#ffffff", scale=1.1, hover_color="#000000")
    include_capitals_title = ft.Text(value="Include Capital Alphabets", font_family="interFont", left=include_capitals_box.left+35, top=include_capitals_box.top+5, size=15, color="#ffffff")

    include_special_box = ft.Checkbox(label="", left=common_x, top=include_capitals_box.top+50, fill_color={ft.MaterialState.SELECTED: "#ff5050", "": "#000000"}, check_color="#ffffff", active_color="#ffffff", scale=1.1, hover_color="#000000")
    include_special_title = ft.Text(value="Include Special Symbols", font_family="interFont", left=include_special_box.left+35, top=include_special_box.top+5, size=15, color="#ffffff")

    generate_btn = ft.Container(width=200, height=50, left=common_x-50, top=150, content=ft.FloatingActionButton(bgcolor="#ff5050", shape=ft.RoundedRectangleBorder(radius=30), content=ft.Text("Generate Password", font_family="interFont", size=15, weight=ft.FontWeight.W_500, color="#ffffff"), on_click=lambda _: make_password()))

    text_input = ft.Container(width=80, height=40, left=generate_btn.left+generate_btn.width+10, top=155, alignment=ft.alignment.center, content=(pswd_len:=ft.TextField(border_color="#ff5050", value="20", color="#ffffff", border_radius=15, input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), text_align=ft.TextAlign.CENTER, dense=False)))

    password = ft.Container(width=700, height=50, bottom=30, alignment=ft.alignment.center, content=(final_pswd:=ft.Text(size=20, font_family="interFontB", color="#ffffff")))

    lower = ft.Container(width=700, height=300, bottom=0, bgcolor=ft.colors.TRANSPARENT, content=ft.Stack([include_numbers_box, include_numbers_title, include_capitals_box, include_capitals_title, include_special_box, include_special_title, generate_btn, text_input, password]))

    body = ft.Container(width=700, height=400, bgcolor="#000000",
                        shadow=ft.BoxShadow(
                            spread_radius=5,
                            blur_radius=30,
                            blur_style=ft.ShadowBlurStyle.NORMAL,
                            offset=ft.Offset(0, 0),
                            color="#000000"
                        ),
                        border_radius=30,
                        content=ft.Stack([title, title_bar, close_btn, lower]))

    page.add(body)
    page.window_center()
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
