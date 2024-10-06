from customtkinter import *
from tkinter import font
import customtkinter as ctk
from datetime import datetime
from tkinter import PhotoImage
from PIL import Image

class Task():
     def __init__(self,master):
          self.Frame = CTkFrame(master,height=600,width=500,fg_color="transparent")
          self.Label = CTkLabel(master,text="Your To Do",bg_color="transparent",font=ctk.CTkFont(family="Product Sans",size=30))
          self.Frame.grid(column=0,row=0) 
          self.Label.grid(column=0,row=0,padx=10,pady=5,sticky="nw")
          
          self.button_color = "light blue"
          self.clicked_color = "lightcoral"
          self.hover_color = "lightgreen"
          
          self.tasks = []
          try:
               image = Image.open("trash.png")
               trash_icon = CTkImage(image)
          except Exception as e:
               print(e)

          self.Button = CTkButton(master,text="New Task",fg_color=self.button_color,text_color="black")
          self.Button.grid(column=0,row=0,padx=630,pady=10,sticky="nw")
          self.Entry = CTkEntry(master,corner_radius=5)
          self.Entry_delete = CTkEntry(master,corner_radius=5)

          self.delete_button = CTkButton(master,text="Delete",image=trash_icon,command=self.remove_task)
          self.delete_button.grid(row=0,column=0,padx=450,pady=10,sticky="nw")

          #self.task = CTkLabel(master,text="Homework",fg_color="transparent",font=CTkFont(family="Arial",size=20))

          self.TaskListFrame = CTkFrame(master,fg_color="transparent")
          self.TaskListFrame.grid(column=0,row=0,padx=20,pady=80,sticky="nw")

          self.selected_item = None # self.Entry.get()
          self.Entry.bind("<Return>",self.on_added)
          self.Button.bind("<Button-1>",self.on_click)
          self.task_row = 0
          self.value = 1
          self.time = datetime.now().strftime("%Y-%m-%d")
          
     def show_entry(self):
          self.Entry.grid(column=0,row=0,padx=0,pady=50,sticky="n")
     def show_delete_entry(self):
          self.Entry_delete.grid(column=0,row=0,padx=450,pady=50,sticky="nw")
     def on_click(self,event):
          self.add_task()
     def on_added(self,event):
          self.add_task()
     def add_task(self):
          self.show_entry()
          self.selected_item = self.Entry.get()
          if self.selected_item:
               self.tasks.append(self.selected_item)
               self.Entry.delete(0,"end")
               self.update_task_list()
               print(self.selected_item) 
     def remove_task(self):
          self.show_delete_entry()
          selected_item_delete = self.Entry_delete.get()
          if selected_item_delete in self.tasks: 
               self.Entry_delete.delete(0,"end")
               self.tasks.remove(selected_item_delete)
               self.update_task_list()
          else:
               print("Task does not exist.")

     def update_task_list(self):
          for widget in self.TaskListFrame.winfo_children():
               widget.destroy()

          for task in self.tasks:
               task_label = CTkLabel(self.TaskListFrame, text=task, fg_color="transparent", font=CTkFont(family="Arial", size=20))
               date_label = CTkLabel(self.TaskListFrame,text=self.time,fg_color="transparent",font=CTkFont(family="Arial",size=15),text_color="grey")
               check_box = CTkCheckBox(self.TaskListFrame,text=None,corner_radius=3)

               task_label.grid(row=self.task_row,column=1,padx=10,pady=0,sticky="w") 
               date_label.grid(row=self.task_row ,column=3,padx=10,pady=10,sticky="we")
               check_box.grid(row=self.task_row,column=4,sticky="w")
               self.task_row += self.value 

          

window = ctk.CTk()
window.geometry("800x600")
window.title("TODO")
window.resizable(False,False)
task = Task(window)
window.mainloop()
