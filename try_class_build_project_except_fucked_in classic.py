import sys
import socket
import tkinter as tk

# Radiobutton variable
rvar = tk.IntVar()
rvar.set(0)


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Simple PortSonar")
        self.geometry("300x200+520+250")
        self.resizable(width=False, height=False)
        self.config(bg="LightGrey")

        # Global variables
        fs_hostname = tk.StringVar()
        ss_hostname = tk.StringVar()
        ss_port_number = tk.IntVar()

        # sys.stdout = TextRedirector()

        # Widgets settings
        self.fast_scan_rbtn = tk.Radiobutton(self, text="Fast Scan", variable=rvar, value=0)
        self.fast_scan_rbtn.place(x=10, y=35)
        self.fast_scan_rbtn.config(bg="LightGrey", font=('', 10))

        self.special_scan_rbtn = tk.Radiobutton(self, text="Special Scan", variable=rvar, value=1)
        self.special_scan_rbtn.place(x=10, y=60)
        self.special_scan_rbtn.config(bg="LightGrey", font=('', 10))

        self.select_btn = tk.Button(self, text="Select", command=self.do_selection, width=12)
        self.select_btn.place(x=15, y=100)
        self.select_btn.config(bg="LightGrey", font=('', 10))

        self.exit_btn = tk.Button(self, text="Exit", command=self.quit, width=12)
        self.exit_btn.place(x=15, y=150)
        self.exit_btn.config(bg="LightGrey", font=('', 10))

        self.output = tk.Text(self, width=19, height=10, state='disabled')
        self.output.place(x=135, y=15)
        self.output.tag_configure("stdout", foreground="#b22222")

        self.scan_type_label = tk.Label(self, text="Choose scan type:")
        self.scan_type_label.place(x=10, y=10)
        self.scan_type_label.config(bg="LightGrey", font=('', 10))

    def do_selection(self):
        if rvar.get() == 0:
            self.fast_scan()
        elif rvar.get() == 1:
            self.special_scan()

    def fast_scan(self):
        # Window settings
        fs = tk.Toplevel()
        fs.geometry("155x100+600+300")
        fs.resizable(width=False, height=False)
        fs.config(bg="LightGrey")

        # Widgets settings
        host_entry = tk.Entry(fs, textvariable=self.fs_hostname, width=22)
        host_entry.focus()
        host_entry.place(x=10, y=35)

        label_host_input = tk.Label(fs, text="HOST:")
        label_host_input.place(x=10, y=7)
        label_host_input.config(bg="LightGrey", font=('', 12))

        scan_btn = tk.Button(fs, text="Scan", command=fs.destroy, width=18)
        scan_btn.place(x=10, y=60)
        scan_btn.config(bg="LightGrey", font=('', 9))

        fs.wait_window()  # Wait until window is closed
        self.use_standard_ports()

    def special_scan(self):
        pass


class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, _str_):
        self.widget.configure(state="normal")
        self.widget.insert("end", _str_, (self.tag,))
        self.widget.configure(state="disabled")


if __name__ == "__main__":
    main_app = MainApp()
    main_app.mainloop()
