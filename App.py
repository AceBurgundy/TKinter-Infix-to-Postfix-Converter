import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
import tkinter
import webbrowser
from CustomButton import HoverButton
from InfixToPostfix import Convert


class App():

    def __init__(self):
        self.__done = False

    def clear(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def newButton(self):

        new_button_box_shadow = ttk.Frame(
            main_frame, style='input_box_shadow.TFrame', width=122, padding=20, height=87)

        new_button_box_shadow.place(x=28, y=27)

        new_button_box_shadow.grid_propagate(False)

        new_button = Button(main_frame, text="New", command=lambda: self.clear(),
                            bg='#25292C', fg="white", padx=-5, pady=3, font=('Courier', 35))

        new_button.grid(column=0, row=0, pady=16, padx=20)

    def clicked(self):

        def printer(index):
            resulted_expression.delete("1.0", "end-1c")
            stack_result.delete("1.0", "end-1c")

            resulted_expression.insert(INSERT, Converter.getLogs()[index][1])
            stack_result.insert(INSERT, Converter.getLogs()[index][0])

        self.newButton()

        if self.__done:

            if resulted_expression.get("1.0", "end-1c") != "":
                resulted_expression.delete("1.0", "end-1c")

            resulted_expression.insert(INSERT, "'New' for new expression")

            return False

        else:

            self.__done = True

            user_input = input.get()

            if resulted_expression.get("1.0", "end-1c") != "":
                resulted_expression.delete("1.0", "end-1c")

            result = Converter.convert(user_input)

            resulted_expression.insert(INSERT, result)

            try:
                stack_result.insert(INSERT, Converter.getLogs()[-1][0])
            except (IndexError):
                stack_result.insert(INSERT, "Press 'New'")

                self.newButton()

            def blink_text():
                current_color = timestamps.cget("fg")
                next_color = "green" if current_color == "red" else "red"
                timestamps.config(fg=next_color)
                timestamps.after(1000, blink_text
                                 )
            timestamps = Text(main_frame, highlightthickness=0, borderwidth=0,
                              fg='red', wrap=WORD, bg='#171c22', width=22, font=('Courier', 20), height=5)

            timestamps.place(x=340, y=10)

            blink_text()

            timestamps.insert(
                INSERT, "Click and scroll through timestamps to see changes in real time")

            canvas = Canvas(result_section, width=0, background='#1d2219')

            canvas.pack(side=LEFT, fill=BOTH, expand=True)

            scroll = Scrollbar(result_section, orient=VERTICAL,
                               command=canvas.yview, bg='green',)

            scroll.pack(side="right", fill=Y)

            canvas.configure(yscrollcommand=scroll.set,
                             highlightthickness=0, borderwidth=0)

            canvas.bind('<Configure>', lambda event: canvas.configure(
                scrollregion=canvas.bbox("all")))

            second_frame = Frame(canvas, background='#1d2219')

            canvas.create_window((0, 0), window=second_frame, anchor="nw")

            index = 0

            for index in range(len(Converter.getLogs())):

                entry = HoverButton(second_frame, text=Converter.getLogs()[index][2], width=21, highlightthickness=0, borderwidth=0, font=(
                    "Courier", 20), background='#1d2219', anchor=W, fg='white', height=2, activebackground='#1d2219', activeforeground="orange", command=lambda e=index: printer(e))

                entry.grid(row=index, column=0, padx=15, pady=0)

            self.newButton()


if __name__ == '__main__':

    Converter = Convert()

    app = App()

    root = tkinter.Tk()

    root.iconphoto(False, PhotoImage(file="switch.png"))

    root.title("Infix to Postfix Converter")

    style = ttk.Style()

    root.resizable(False, False)

    window_height = 720
    window_width = 1080

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width,
                                       window_height, x_cordinate, y_cordinate))

    root.columnconfigure(0, weight=65)
    root.columnconfigure(1, weight=35)
    root.rowconfigure(0, weight=85)
    root.rowconfigure(1, weight=15)

    style.configure('frame.TFrame', background='#171c22')

    style.configure('result_section.TFrame', background='#1d2219')

    main_frame = ttk.Frame(root, style='frame.TFrame')

    main_frame.grid_propagate(False)

    input_section = ttk.Frame(
        root, style='frame.TFrame')

    input_section.grid_propagate(False)

    result_section = ttk.Frame(
        root, style='result_section.TFrame')

    result_section.grid_propagate(False)

    result_section.grid(column=1, row=0, sticky="WENS", rowspan=2)

    main_frame.grid(column=0, row=0, sticky="WENS")

    input_section.grid(column=0, row=1, sticky="WENS")

    input_section.columnconfigure(0, weight=1)
    input_section.columnconfigure(1, weight=1)
    input_section.rowconfigure(0, weight=10)
    input_section.rowconfigure(1, weight=80)
    input_section.rowconfigure(2, weight=10)

    resulted_expression = Text(
        main_frame, highlightthickness=0, borderwidth=0, fg='white', bg='#171c22', wrap=WORD, width=22, font=('Courier', 40))

    resulted_expression.place(x=20, y=200)

    stack_result = Text(
        main_frame, highlightthickness=0, borderwidth=0, fg='white', wrap=WORD, bg='#171c22', width=22, font=('Courier', 40))

    stack_result.place(x=20, y=400)

    input_box_shadow = ttk.Frame(
        input_section, style='input_box_shadow.TFrame', width=503, padding=20, height=66)

    input_box_shadow.place(x=22, y=27)

    input_box_shadow.grid_propagate(False)

    input = Entry(input_section, width=20, highlightthickness=0, borderwidth=0, font=(
        'Courier', 30), justify=CENTER, background='#25292C', fg='white', insertbackground="white")

    input.grid(column=0, row=1, ipadx=12, ipady=10)

    style.configure('input_box_shadow.TFrame', background='#846e6e')

    convert_button = Button(input_section, text="CONVERT",
                            bg='#25292C', fg="white", command=app.clicked, padx=5, pady=10, font=('Courier', 20))

    convert_button.grid(column=1, row=1)

    def on_closing():

        yes = askyesno(
            title="Exit", message="Check out the Javascript version of this app?")

        if yes:
            webbrowser.open_new_tab(
                "https://infix-to-postfix-converter.vercel.app/")
        else:
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
