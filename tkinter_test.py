from tkinter import *
import socket
from datetime import datetime

root = Tk()

e = Entry(width=20)
b = Button(text='Scan')
t = Text(width=50, height=10, bg='black', fg='white')


def get_host_by_name(event):
    s = e.get()
    s = socket.gethostbyname(s)
    t1 = datetime.now()
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((s, port))
            if result == 0:
                t.insert('1.0', f"Port {port}: 	 Open\n")
            sock.close()

    except KeyboardInterrupt:
        t.insert('1.0', "You pressed Ctrl+C\n")
        sys.exit()

    except socket.gaierror:
        t.insert('1.0', 'Hostname could not be resolved. Exiting\n')
        sys.exit()

    except socket.error:
        t.insert('1.0', "Couldn't connect to server\n")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    t.insert('1.0', f'Scanning Completed in: {total}\n')


b.bind('<Button-1>', get_host_by_name)
e.bind('<Return>', get_host_by_name)

e.pack()
b.pack()
t.pack(side=RIGHT)
root.mainloop()
