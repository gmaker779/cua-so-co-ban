from guizero import App, Text

cuaso = App("Hộp thoại của tôi")
ten = Text(cuaso, "Đình Thăng")
ten.text_color = "darkblue"
hoc = Text(cuaso, "Học GUI thật thú vị!")
hoc.text_color = "red"

cuaso.display()