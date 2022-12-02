from tkinter import Button


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(foreground="orange")
        event.widget.config(background="#1d2219")
        event.widget.config(cursor="hand1")

    def on_leave(self, event):
        event.widget.config(foreground="white")
        event.widget.config(background="#1d2219")
        event.widget.config(cursor="arrow")
