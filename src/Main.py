import time
import tkinter as tk
from tkinter.constants import E, END, EW, W
import pyautogui

class Application(tk.Frame):

  def __init__(self, master=None):
    super().__init__(master)

    self.master = master
    self.master.title("Spam")
    self.master.geometry("500x500")

    self.pack()
    self.create_widgets()

  def create_widgets(self):
    # Set up for message box label
    self.messageLabel = tk.Label(self, text="Message")
    self.messageLabel.grid(row=0, column=0, sticky=W)

    # Set up for message box
    self.scrollbar = tk.Scrollbar(self)
    self.messageBox = tk.Text(self, width=40, height=5, wrap='word')
    self.scrollbar.config(command=self.messageBox.yview)
    self.messageBox.config(yscrollcommand=self.scrollbar.set)
    self.scrollbar.grid(row=0, column=2)
    self.messageBox.grid(row=0, column=1, pady=15, sticky=EW, padx=[5, 0])

    # Set up for delay label
    self.delayLabel = tk.Label(self, text="Delay time")
    self.delayLabel.grid(row=1, column=0, pady=15, sticky=W)

    # Set up for delay input box
    self.delayInput = tk.Entry(self, width=10)
    self.delayInput.grid(row=1, column=1, sticky=W, padx=5)
    
    # Set up for count label
    self.countLabel = tk.Label(self, text="Count")
    self.countLabel.grid(row=2, column=0, pady=15, sticky=W)

    # Set up for count input box
    self.countInput = tk.Entry(self, width=10)
    self.countInput.grid(row=2, column=1, sticky=W, padx=5)

    # Set up for start spam button
    self.startspamButton = tk.Button(self, width=12, height=2, text="Start Spam", command=self.startSpam)
    self.startspamButton.grid(row=3, column=1, sticky=E)

  def startSpam(self):
    time.sleep(float(self.delayInput.get()))

    for i in range(int(self.countInput.get())):
      pyautogui.write(self.messageBox.get('1.0', END))

if __name__ == "__main__":
  app = Application(tk.Tk())
  app.mainloop()