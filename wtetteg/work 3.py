#importing libraries
import tkinter as tk
import customtkinter as ctk
import mysql.connector as sql

#creating main window
window = ctk.CTk()

#configure window settings & appearance
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")
window.overrideredirect(True)
ctk.set_appearance_mode("dark")

#fixed parameters
firstx, firsty = 40, 100
secondx = 770
thirdx = 1160
gap = '*' * 256
valid_query = False
exitx, exity = 1360, 805
password = ""

#functions
def run_query():
    global query
    result_textbox.delete(1.0, tk.END)
    query = query_in.get().strip()
    if query:
        history_textbox.insert(tk.END, query + "\n")
        output(query)
    else:
        result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\nError: No query given, enter a query")
    query_in.delete(0, tk.END)

def execute(event = None):
    run_query()

def close_window(event = None):
    window.destroy()

def clear_history():
    history_textbox.delete(1.0, tk.END)

def clear_result():
    result_textbox.delete(1.0, tk.END)
    current_query_textbox.delete(1.0, tk.END)

def get_prev_query(event = None):
    if not query_in.get():
        index = history_textbox.index("end-1c").split(".")[0]
        query_in.insert(tk.END, history_textbox.get(f"{int(index) - 1}.0", f"{index}.end-1c"))

def clear_query_in(event = None):
    query_in.delete(0, tk.END)

def show_current_query(query_status):
    if query_status:
        current_query_textbox.delete(1.0, tk.END)
        current_query_textbox.insert(tk.END, query)
    else:
        current_query_textbox.delete(1.0, tk.END)
        current_query_textbox.insert(tk.END, "Invalid query")

def output(query):
    try:
        connection = sql.connect(
            host = "localhost",
            user = "root",
            password = password
        )
        
        if connection.is_connected():
            result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\n")
        
        cursor = connection.cursor()
        cursor.execute(query)

        if cursor.description:    
            fields = [field[0] for field in cursor.description]
            result_textbox.insert(tk.END, "\t\t".join(fields) + "\n")
            result_textbox.insert(tk.END, "-" * 448 + "\n")

            for record in cursor.fetchall():
                record_data = "\t\t".join([str(item) for item in record])
                result_textbox.insert(tk.END, record_data + "\n")
        else:
            result_textbox.insert(tk.END, f"Query executed successfully: {query}\n")

        cursor.close()
        connection.close()
        valid_query = True
    except sql.Error as e:
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, f"{gap}\nConnected to MySQL Server\n{gap}\n\nError: {e}\n")
        valid_query = False
    show_current_query(valid_query)

#headings
history_text = ctk.CTkLabel(window, text = "Query history")
history_text.place(x = firstx, y = firsty)
query_text = ctk.CTkLabel(window, text = "Enter a select query")
query_text.place(x = secondx, y = firsty)
current_query_text = ctk.CTkLabel(window, text = "Current query")
current_query_text.place(x = thirdx, y = firsty)
result_text = ctk.CTkLabel(window, text = "Result")
result_text.place(x = firstx, y = 360)

#output
history_textbox = ctk.CTkTextbox(window, width = 680, height = 150, state = tk.NORMAL)
history_textbox.place(x = firstx, y = firsty + 40)
result_textbox = ctk.CTkTextbox(window, width = 1460, height = 350, state = tk.NORMAL)
result_textbox.place(x = firstx, y = 400)
current_query_textbox = ctk.CTkTextbox(window, width = 340, height = 20, state = tk.NORMAL)
current_query_textbox.place(x = thirdx, y = firsty + 50)

#entry
query_in = ctk.CTkEntry(window, placeholder_text = "Type in your query here", width = 350)
query_in.place(x = secondx, y = firsty + 50)

#buttons
exit_button = ctk.CTkButton(window, text = "Exit [ESC]", command = close_window, fg_color="#313338", hover_color="#494D54")
exit_button.place(x = exitx, y = exity)
run_query_button = ctk.CTkButton(window, text = "Run query [ENTER]", command = run_query, width = 200, fg_color="#313338", hover_color="#494D54")
run_query_button.place(x = secondx, y = firsty + 100)
clear_history_button = ctk.CTkButton(window, text = "Clear history", command = clear_history, fg_color="#313338", hover_color="#494D54")
clear_history_button.place(x = firstx, y = 310)
clear_result_button = ctk.CTkButton(window, text = "Clear result window", command = clear_result, fg_color="#313338", hover_color="#494D54")
clear_result_button.place(x = firstx, y = 770)

#key bindings
query_in.bind('<Return>', execute)
query_in.bind('<Up>', get_prev_query)
query_in.bind('<Down>', clear_query_in)
window.bind('<Escape>', close_window)

#run event controller
window.mainloop()