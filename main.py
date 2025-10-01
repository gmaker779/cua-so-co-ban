from guizero import App, Text

app = App("Luyện tập Bài 2")
app.width=600
app.height=400
app.bg = "lightblue"
text = Text(app, "Xin chào, tôi đang học GUIZERO")
text.text_color = "red"
text.size = 16
app.display()