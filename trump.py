import tkinter as tk


class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        button = tk.Button(self, text="Open window", command=self.on_button)
        button.pack()

    def on_button(self):
        var, note = Update()
        a = var.get()
        b = note.get()
        print(f"a: {a} b: {b}")


def Update():
    Up = tk.Toplevel()
    Up.title("Update")
    tk.Label(Up, text ="Update", font=('Times', 20)).grid(row=0)

    var = tk.IntVar()
    tk.Radiobutton(Up, text="Fully", variable=var, value=1).grid(row=2, sticky="w")
    tk.Radiobutton(Up, text="Partly", variable=var, value=2).grid(row=3, sticky="w")
    tk.Radiobutton(Up, text="Un", variable=var, value=3).grid(row=4, sticky="w")

    evar = tk.StringVar()
    note = tk.Entry(Up, width=30, font=('Arial', 12,), textvariable=evar)
    note.grid(row=6)

    Button = tk.Button(Up, text="Task Complete and Send Invoice", command=Up.destroy).grid(row=7)

    Up.wait_window()
    print("done waiting...")
    return var, evar


if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
