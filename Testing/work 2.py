
import mysql.connector
query = "delete from personal where id = 1;"
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pcoe1234",
    database="record"
)

cursor = conn.cursor()


operation = query.split()[0]
if operation.lower() == "delete":
    table = query.split()[2]
    cursor.execute(query)
elif operation.lower() == "update":
    table = query.split()[1]
    cursor.execute(query)
else:
    table = query.split()[2][0 : query.split()[2].find("(")]
    cursor.execute(query)
                              
print(table)



cursor.execute(f"SELECT * FROM {table}")
results = cursor.fetchall()
conn.commit()
for result in results:
    print(result)


cursor.close()
conn.close()






















































"""
#importing libraries
import tkinter as tk
import customtkinter as ctk

#main window
window = ctk.CTk()

#window resolution
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")
window.overrideredirect(True)

#functions
def close_window(event = None):
    window.destroy()

#buttons
exit_button = ctk.CTkButton(window, text = "Exit [ESC]", command = close_window)
exit_button.place(x = 1100, y = 660)

#key bindings
window.bind('<Escape>', close_window)
#run event controller
window.mainloop()

















from tkinter import *; import customtkinter as ctk;ctk.set_appearance_mode("dark");root = ctk.CTk()
root.title('Tkinter.com - Custom Tkinter!');root.geometry('600x350')

def show_frame(frame):
    page_1.pack_forget()
    page_2.pack_forget()
    page_3.pack_forget()
    frame.pack(expand = True, fill = 'both')

page_1 = ctk.CTkFrame(root)
page_2 = ctk.CTkFrame(root)
page_3 = ctk.CTkFrame(root)

label_1 = ctk.CTkLabel(page_1, text = "This is frame 1")
label_1.pack(pady = 20)
label_2 = ctk.CTkLabel(page_2, text = "This is frame 2")
label_2.pack(pady = 20)
label_3 = ctk.CTkLabel(page_3, text = "This is frame 3")
label_3.pack(pady = 20)

navigation_frame = ctk.CTkFrame(root, height = 38 )  # Set background color here
navigation_frame.pack(side='top', fill='x')

button_1 = ctk.CTkButton(navigation_frame, text="page 1", command= lambda:show_frame(page_1))
button_1.place( x = 700 , y = 5)
button_2 = ctk.CTkButton(navigation_frame, text="page 2", command= lambda:show_frame(page_2))
button_2.place( x = 900 , y = 5)
button_3 = ctk.CTkButton(navigation_frame, text="page 3", command= lambda:show_frame(page_3))
button_3.place( x = 1100 , y = 5)

show_frame(page_1)
root.mainloop()

"""

























"""
def add(matrix1, matrix2):
    matrixOut = []
    for row in range(len(matrix1)):
        for column in range(len(matrix2)):
            matrixOut.append(int(matrix1[row][column]) + int(matrix2[row][column]))

    for _ in range(len(matrixOut)):
        print(f"{matrixOut[_]}", end=" ")
        if (_ + 1) % 3 == 0:
            print()
            
def subtract(matrix1, matrix2):
    matrixOut = []
    for row in range(len(matrix1)):
        for column in range(len(matrix2)):
            matrixOut.append(int(matrix1[row][column]) - int(matrix2[row][column]))
   
    for _ in range(len(matrixOut)):
        print(f"{matrixOut[_]}", end=" ")
        if (_ + 1) % 3 == 0:
            print()

def product(matrix1, matrix2):
    pass

def firstIn(): row = [input().split(" ") for _ in range(int(input("Enter number of rows on your first matrix:   ")))]; return row
def secondIn(): row = [input().split(" ") for _ in range(int(input("\nEnter number of rows on your second matrix:   ")))]; return row

f = [['1', '2', '3'], 
     ['4', '3', '2'], 
     ['8', '2', '1']]

s = [['-3', '8', '2'], 
     ['1', '43', '2'], 
     ['9', '2', '-11']]

#use firstIn() and secondIn() as arguments
add(f, s) 
subtract(f, s)
"""