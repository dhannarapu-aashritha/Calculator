import tkinter as tk

class BasicCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Calculator")
        self.geometry("320x420")
        self.configure(bg="#222222")
        self.resizable(False, False)

        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        # Display entry (readonly)
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Helvetica", 28),
            bd=0,
            bg="#333333",
            fg="#ffffff",
            justify="right",
            state="readonly",
            readonlybackground="#333333"
        )
        self.display.pack(fill="both", ipady=20, padx=10, pady=20)

        # Buttons frame
        buttons_frame = tk.Frame(self, bg="#222222")
        buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Button style
        btn_font = ("Helvetica", 18)
        btn_fg = "#ffffff"
        btn_bg = "#444444"
        btn_active_bg = "#555555"

        # Buttons layout
        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0, 2), (".", 3, 2), ("+", 3, 3),
            ("C", 4, 0), ("DEL", 4, 1), ("=", 4, 2, 2),
        ]

        for (text, row, col, colspan) in map(lambda b: b if len(b) ==4 else (*b,1), buttons):
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=btn_font,
                fg=btn_fg,
                bg=btn_bg,
                activebackground=btn_active_bg,
                bd=0,
                relief="flat",
                command=lambda t=text: self.on_button_click(t),
                cursor="hand2"
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.update_display()
        elif char == "DEL":
            self.expression = self.expression[:-1]
            self.update_display()
        elif char == "=":
            self.calculate_result()
        else:
            self.expression += char
            self.update_display()

    def update_display(self):
        self.display_var.set(self.expression if self.expression else "0")

    def calculate_result(self):
        try:
            result = eval(self.expression)
            if isinstance(result, float):
                result = round(result, 10)
            self.expression = str(result)
            self.update_display()
        except Exception:
            self.expression = ""
            self.display_var.set("Error")

if __name__ == "__main__":
    app = BasicCalculator()
    app.mainloop()

