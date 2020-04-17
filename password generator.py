# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:32:43 2020

@author: Manan
"""



import tkinter as tk
import string 
import random

def generate_password():
    password=[]
    for i in range(5):
        alpha=random.choice(string.ascii_letters)
        symbol=random.choice(string.punctuation)
        numbers=random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
        
        
        passwords= "".join(str(x) for x in password)
        label.config(text=passwords)
        
        
root = tk.Tk()
root.geometry("300x300")
button = tk.Button(root, text="genrate password" , command=generate_password )
button.grid(row=2 , column=2)
label=tk.Label(root,font=("times" , 15, "bold")) 
label.grid(row=4, column=2)
root.mainloop()       