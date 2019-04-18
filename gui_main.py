import socket
from tkinter import *
from tkinter import ttk
from termcolor import colored


def use_standard_ports():
    # color_a = colored("[+] ", 'green')
    color_b = colored("[!] ", 'red')
    color_c = colored("[!] ", 'yellow')

    host = message.get()
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
            print(color_c + "Port -- ", i, " -- [OPEN]")


root = Tk()
root.title("Simple PortSonar")
root.geometry("325x120")

# Widgets in main window
message = StringVar()

entry_1 = ttk.Entry(width=30, textvariable=message).grid(pady=5, padx=5)

scan_btn = ttk.Button(root, text="Default Scan", command=use_standard_ports)\
    .grid(row=0, column=1, sticky=(W, E), padx=5, pady=5)
# quit_btn = ttk.Button(root, text="Exit", command=root.quit)\
#     .grid(row=1, column=1, sticky=(W, E), padx=5, pady=5)

root.mainloop()
