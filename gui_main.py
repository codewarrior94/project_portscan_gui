import socket
import sys
import tkinter as tk
from termcolor import colored


# Function for scanning some standard ports from the list
def use_standard_ports():
    color_a = colored("[+] ", 'green')
    color_b = colored("[!] ", 'red')

    host = only_host_var.get()
    print("\n")
    port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80]

    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, i))
        except socket.error:
            print(color_b + "Port -- ", i, " -- [CLOSED]")
        else:
            print(color_a + "Port -- ", i, " -- [OPEN]")


# Function for scanning custom port on users demand
def use_custom_port():
    scan = socket.socket()

    host = host_var.get()
    port = port_var.get()

    color_a = colored("[+] ", 'green')
    color_b = colored("[!] ", 'red')

    try:
        scan.settimeout(0.5)
        scan.connect((host, port))
    except socket.error:
        print(color_b + "Port -- ", port, " -- [CLOSED]")
    else:
        print(color_a + "Port -- ", port, " -- [OPEN]")


def do_selection():
    if rvar.get() == 0:
        fast_scan()
    elif rvar.get() == 1:
        use_custom_port()


def fast_scan():
    # Window settings
    fs = tk.Toplevel()
    fs.title("Fast Scan mode")
    fs.geometry("180x100")
    fs.resizable(width=False, height=False)

    # Widgets settings
    hostname_var = tk.StringVar
    host_entry = tk.Entry(fs, textvariable=hostname_var, width=22)
    label_host_input = tk.Label(fs, text="Input required hostname:")
    ok_btn = tk.Button(fs, text="Ok", command=fs.destroy, width=12)

    # Widget place manage & special configurations
    label_host_input.place(x=10, y=7)
    host_entry.place(x=10, y=30)
    ok_btn.place(x=34, y=60)

    fs.wait_window()
    return hostname_var


######################
# Main Window Config #
######################

# Window settings
root = tk.Tk()
root.title("Simple PortSonar")
root.geometry("300x200+520+250")
root.resizable(width=False, height=False)

# Widget variables
rvar = tk.IntVar()
rvar.set(0)

# Button & Radiobutton section
fast_scan_rbtn = tk.Radiobutton(root, text="Fast Scan", variable=rvar, value=0)
special_scan_rbtn = tk.Radiobutton(root, text="Special Scan", variable=rvar, value=1)
scan_btn = tk.Button(root, text="Scan", command=do_selection, width=12)
exit_btn = tk.Button(root, text="Exit", command=root.quit, width=12)

# Textbox, listbox etc. section
output = tk.Text(root, width=19, height=10)
scan_type_label = tk.Label(root, text="Choose scan type:")

# Place manager & widget special configuration
scan_type_label.place(x=10, y=10)
fast_scan_rbtn.place(x=10, y=30)
special_scan_rbtn.place(x=10, y=50)
scan_btn.place(x=10, y=80)
exit_btn.place(x=10, y=154)
output.place(x=135, y=15)

root.mainloop()
