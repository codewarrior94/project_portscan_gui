import tkinter as tk
import time
import sys

class Display(tk.Frame):
    def __init__(self,parent=0):
       tk.Frame.__init__(self,parent)
       self.input = tk.Text(self, width=100, height=15)
       self.input.pack()
       self.doIt = tk.Button(self,text="URL to Hash", command=self.onEnter)
       self.doIt.pack()
       self.output = tk.Text(self, width=100, height=15)
       self.output.pack()
       sys.stdout = self
       self.pack()

    def onEnter(self):
        text_input = self.input.get(1.0,tk.END)
        product_url_list = text_input.split('\n')
        url_list_to_hash(product_url_list)

### I used the code below to somewhat successfully call the functions from another script
### but it did not solve my issue though.
        # p = subprocess.Popen(['python', './image_url_to_hash.py', self.input.get(1.0,"end-1c")],
        #              stdout=subprocess.PIPE,
        #              stderr=subprocess.STDOUT,
        #              )
        # for line in iter(p.stdout.readline, ''):
        #     print line

    def write(self, txt):
        self.output.insert(tk.END,str(txt))
#######This is the missing line!!!!:
        self.update_idletasks()

def input_to_hash(text_input):
    product_url_list = text_input.split('\n')
    ### This is just some dummy code to simulate the output.
    ### There is a delay is processing each url, but I would like to capture output as it's running
    for link in product_url_list:
        time.sleep(1)
        print(link)

if __name__ == '__main__':
    Display().mainloop()