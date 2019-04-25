import socket
import tkinter as tk


# Function for scanning some standard ports from the list
def use_standard_ports():
    scan = socket.socket()

    host = fs_hostname.get()
    port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80, 443]

    for i in port:
        try:
            scan.settimeout(0.5)
            scan.connect((host, i))
        except socket.error:
            print(f"Port {i} -- [CLOSED]")
        else:
            print(f"Port {i} -- [OPEN]")


# Function for scanning custom port on users demand
def use_custom_port():
    host = ss_hostname.get()
    port = ss_port_number.get()

    try:
        scan = socket.socket()
        scan.settimeout(0.5)
        scan.connect((host, port))
    except socket.error:
        print("Port -- ", port, " -- [CLOSED]")
    else:
        print("Port -- ", port, " -- [OPEN]")


def do_selection():
    if rvar.get() == 0:
        fast_scan()
    elif rvar.get() == 1:
        special_scan()


def fast_scan():
    # Window settings
    fs = tk.Toplevel(None)
    fs.geometry("250x100+600+300")
    fs.resizable(width=False, height=False)

    # Widgets settings
    host_entry = tk.Entry(fs, textvariable=fs_hostname, width=22)
    host_entry.focus()
    host_entry.place(x=10, y=30)

    label_host_input = tk.Label(fs, text="Input required hostname:")
    label_host_input.place(x=10, y=7)

    ok_btn = tk.Button(fs, text="Ok", command=fs.destroy, width=12)
    ok_btn.place(x=34, y=60)

    fs.wait_window()  # Wait until window is closed
    use_standard_ports()


def special_scan():
    # Window settings
    ss = tk.Toplevel(None)
    ss.geometry("180x100+600+300")
    ss.resizable(width=False, height=False)
    ss.config(bg="LightGrey")

    # Widgets settings
    label_host = tk.Label(ss, text="HOST:", font=('', 12))
    label_host.place(x=5, y=5)
    label_host.config(bg="LightGrey")

    label_port = tk.Label(ss, text="PORT:", font=('', 12))
    label_port.place(x=120, y=5)
    label_port.config(bg="LightGrey")

    entry_host = tk.Entry(ss, textvariable=ss_hostname, width=15)
    entry_host.focus()
    entry_host.place(x=7, y=35)

    entry_port = tk.Entry(ss, textvariable=ss_port_number, width=7)
    entry_port.place(x=123, y=35)

    scan_btn = tk.Button(ss, text="Scan", width=22, command=ss.destroy)
    scan_btn.place(x=7, y=65)
    scan_btn.config(bg="LightGrey", font=('', 9))

    ss.wait_window()  # Wait until window is closed
    use_custom_port()


######################
# Main Window Config #
######################

# Window settings
root = tk.Tk(None)
root.title("Simple PortSonar")
root.geometry("300x200+520+250")
root.resizable(width=False, height=False)
root.config(bg="LightGrey")

# Global variables
fs_hostname = tk.StringVar()
ss_hostname = tk.StringVar()
ss_port_number = tk.IntVar()

# Widgets variables
rvar = tk.IntVar()
rvar.set(0)

# Widgets settings
fast_scan_rbtn = tk.Radiobutton(root, text="Fast Scan", variable=rvar, value=0)
fast_scan_rbtn.place(x=10, y=35)
fast_scan_rbtn.config(bg="LightGrey", font=('', 10))

special_scan_rbtn = tk.Radiobutton(root, text="Special Scan", variable=rvar, value=1)
special_scan_rbtn.place(x=10, y=60)
special_scan_rbtn.config(bg="LightGrey", font=('', 10))

select_btn = tk.Button(root, text="Select", command=do_selection, width=12)
select_btn.place(x=15, y=100)
select_btn.config(bg="LightGrey", font=('', 10))

exit_btn = tk.Button(root, text="Exit", command=root.quit, width=12)
exit_btn.place(x=15, y=150)
exit_btn.config(bg="LightGrey", font=('', 10))

output = tk.Text(root, width=19, height=10, state='disabled')
output.place(x=135, y=15)

scan_type_label = tk.Label(root, text="Choose scan type:")
scan_type_label.place(x=10, y=10)
scan_type_label.config(bg="LightGrey", font=('', 10))

root.mainloop()
