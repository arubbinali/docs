# Course 1: GUI Programming

## Module 1

### 1. `Tk()` & `mainloop()`:
   - The main application window (which is often the only window being used by the application) is created by the tkinter method named `Tk()`.
   - To start the controller, you have to invoke the main window's method, named `mainloop()`.
  
      code:
            
      ```py
      import tkinter
   
      skylight = tkinter.Tk()
      skylight.mainloop()
      ```

### 2. `title()`
   - to name window's title bar
   
     code:
  
      ```py
      import tkinter
   
      skylight = tkinter.Tk()
      skylight.title("Skylight")
      skylight.mainloop()
      ```

### 3. `Button()` & `place()`
   - create a Button class object and place it inside the main window
   - first argument is obligatory (a reference to the target window), others are optional
   - the argument `text` displayts text on the button

   - `place()` used to place the widget inside a window
   - x & y coordinates are given, and the widget is placed having the x axis on the top & y axis on the left, unlike the cartesian system
        
     code:

      ```py
      import tkinter

      skylight = tkinter.Tk()
      skylight.title("Skylight")
      button = tkinter.Button(skylight, text="Bye!")
      button.place(x=10, y=10)
      skylight.mainloop()
      ```

### 4. Event handler
   - a piece of code responsible for responding to all clicks addressed to a button
   - this will only be invoked by the controller
  
   - a function designed to be invoked by someone/something else (not us)

   - the argument `command` t's set with the name of a callback that will be invoked when the button is clicked
   - there are no parentheses, as we don't want to invoke the callback here – we need its name to be passed to the Button object

     code:
      
      ```py
      import tkinter

      def Click():
          skylight.destroy()
          
      skylight = tkinter.Tk()
      skylight.title("Skylight")
      button = tkinter.Button(skylight, text="Bye!", command=Click)
      button.place(x=10, y=10)
      skylight.mainloop()
      ```

### 5. `messagebox`, `askquestion()` & modal windows
   - modal window --> a window which grabs the whole of the application's focus
   - messagebox creates dialog boxes intended to ask questions, display messages, and to receive a user's reply
   - the dialog box is an example of a modal window
   - `askquestion()`, takes in 2 arguments, dialog window title & the text inside the window

     code:
      ```py
      import tkinter
      from tkinter import messagebox
   
   
      def Click():
          replay = messagebox.askquestion("Quit?", "Are you sure?")
          if replay == 'yes':
              skylight.destroy()
   
   
      skylight = tkinter.Tk()
      skylight.title("Skylight")
      button = tkinter.Button(skylight, text="Bye!", command=Click)
      button.place(x=10, y=10)
      skylight.mainloop()
      ```

### 6.  Gemoetry managers - place, grid & pack
    - place - user decides where the widget goes by mentioning the x and y coordinates
    - grid - gives you a chance to express your general wishes and tries to deploy the widgets according to them, they aren't as precise as the ones used by place, but are far more detailed than those utilized by pack
    - pack - tries and finds the best possible location for each widget, these managers cannot be mixed. Only one of them can be used in one application
    
       1\. place:
       
         - parameters: h, w, x, y
         -    h & w - height and width, if the parameters are omitted, the widget's height & width will be determined automatically
         -    x - the widget's top-left pixel's horizontal coordinate measured relative to the home window's top-left corner
         -    y - the widget's top-left pixel's vertical coordinate measured relative to the home window's top-left corner
         
         code:
         ```py
         import tkinter as tk
         
         window = tk.Tk()
         button_1 = tk.Button(window, text="Button #1")
         button_2 = tk.Button(window, text="Button #2")
         button_3 = tk.Button(window, text="Button #3")
         button_1.place(x=10, y=10)
         button_2.place(x=20, y=40)
         button_3.place(x=30, y=70)
         window.mainloop()
         ```
         ```py
         import tkinter as tk
         
         window = tk.Tk()
         button_1 = tk.Button(window, text="Button #1")
         button_2 = tk.Button(window, text="Button #2")
         button_3 = tk.Button(window, text="Button #3")
         button_1.place(x=10, y=10, width=150)
         button_2.place(x=20, y=40)
         button_3.place(x=30, y=70, height=50)
         window.mainloop()
         ```

         2\. grid:

         paramters: column, row, rowspan, columnspan

       - column=c - deploys the widget in the column number c; note: the columns' numbers start from zero, and if you omit this argument, the manager will assume 0 (the left-most column)
       - row=r - deploys the widget in the row number r; if you omit this argument, the manager will assume the first free row starting from the top
       - columnspan=cs - determines how many neighboring columns the widget occupies; the parameter defaults to 1 (the widget won't cross a single grid's cell)
       - rowspan=rs - works as columnspan but refers to rows
                
          code:
          ```py
          import tkinter as tk

          window = tk.Tk()
          button_1 = tk.Button(window, text="Button #1")
          button_2 = tk.Button(window, text="Button #2")
          button_3 = tk.Button(window, text="Button #3")
          button_1.grid(row=0, column=0)
          button_2.grid(row=1, column=1)
          button_3.grid(row=2, column=2)
          window.mainloop()
          ```
          ```py
          import tkinter as tk

          window = tk.Tk()
          button_1 = tk.Button(window, text="Button #1")
          button_2 = tk.Button(window, text="Button #2")
          button_3 = tk.Button(window, text="Button #3")
          button_1.grid(row=0, column=0)
          button_2.grid(row=1, column=1)
          button_3.grid(row=2, column=0, columnspan=2)
          window.mainloop()
          ```

        3\. pack:

         parameters: (side: TOP, BOTTOM, LEFT, RIGHT), (fill: NONE, X, Y, BOTH)
       - side=s - forces the manager to pack the widgets in a specified direction
       - fill=f - suggests to the manager how to expand the widget if you want it to occupy more space than the default
             
         code:
          ```py
          import tkinter as tk

          window = tk.Tk()
          button_1 = tk.Button(window, text="Button #1")
          button_2 = tk.Button(window, text="Button #2")
          button_3 = tk.Button(window, text="Button #3")
          button_1.pack()
          button_2.pack()
          button_3.pack()
          window.mainloop()
          ```
          ```py
          import tkinter as tk

          window = tk.Tk()
          button_1 = tk.Button(window, text="Button #1")
          button_2 = tk.Button(window, text="Button #2")
          button_3 = tk.Button(window, text="Button #3")
          button_1.pack(side=tk.RIGHT)
          button_2.pack()
          button_3.pack()
          window.mainloop()
          ```
          ```py
          import tkinter as tk

          window = tk.Tk()
          button_1 = tk.Button(window, text="Button #1")
          button_2 = tk.Button(window, text="Button #2")
          button_3 = tk.Button(window, text="Button #3")
          button_1.pack(side=tk.RIGHT, fill=tk.Y)
          button_2.pack()
          button_3.pack()
          window.mainloop()
          ```

### 7. Coloring widgets
        arguments: bg, fg, activeforeground, activebackground
   - last 2 are for when the button is pressed and not yet released
                
     Hex codes
      - #000000 is black
      - #FFFFFF is white
      - #FF0000 is red
      - #00FF00 is green
      - #0000FF is blue
      - #00FFFF is turquoise
      - #FF00FF is violet
       ...

     code:
      ```py
      import tkinter as tk

      window = tk.Tk()
      button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
      button.pack()
      window.mainloop()
      ```
      ```py
      import tkinter as tk

      window = tk.Tk()
      button = tk.Button(window, text="Button #1",
                      bg="MediumPurple",
                      fg="LightSalmon",
                      activeforeground="LavenderBlush",
                      activebackground="HotPink")
      button.pack()
      window.mainloop()
      ```
      ```py
      import tkinter as tk

      window = tk.Tk()
      button = tk.Button(window, text="Button #1",
                      bg="#9370DB",
                      fg="#FFA07A",
                      activeforeground="#FFF0F5",
                      activebackground="#FF69B4")
      button.pack()
      window.mainloop()
      ```

### 8. A GUI application from scratch
     1) construct a window and launch an event controller

         code:
          ```py
          import tkinter as tk
   
          window = tk.Tk()
          window.mainloop()
          ```   

     2) Label()
         - a non-clickable widget able to present short textual information, passed to the widget's constructor using a text argument
     
         code:
        ```py
        import tkinter as tk
   
        window = tk.Tk()
   
        label = tk.Label(window, text = "Little label:")
        label.pack()
   
        window.mainloop()
        ```

     3) Frame()
         - a non-clickable component used to group widgets and to separate them (visually) from other window components
             
         code:
          ```py
          import tkinter as tk
   
          window = tk.Tk()
   
          label = tk.Label(window, text="Little label:")
          label.pack()
   
          frame = tk.Frame(window, height=30, width=100, bg="#000099")
          frame.pack()
   
          window.mainloop()
          ```
      
     4) Button()

         code:
          ```py
          import tkinter as tk

          window = tk.Tk()

          label = tk.Label(window, text="Little label:")
          label.pack()

          frame = tk.Frame(window, height=30, width=100, bg="#000099")
          frame.pack()

          button = tk.Button(window, text="Button")
          button.pack(fill=tk.X)

          window.mainloop()
          ```
     5) IntVar() & set()
         - create an object of the class `IntVar` and use the class method `set` to store an integer value
     
         code:
          ```py
          import tkinter as tk

          window = tk.Tk()

          label = tk.Label(window, text="Little label:")
          label.pack()

          frame = tk.Frame(window, height=30, width=100, bg="#000099")
          frame.pack()

          button = tk.Button(window, text="Button")
          button.pack(fill=tk.X)

          switch = tk.IntVar()
          switch.set(1)

          window.mainloop()
          ```
     6) Checkbutton()
        
        code:
        ```py
        import tkinter as tk

         win = tk.Tk()
         
         label = tk.Label(win, text="Little label:")
         label.pack()
         
         frame = tk.Frame(win, height=30, width=100, bg="#000099")
         frame.pack()
         
         button = tk.Button(win, text="Button")
         button.pack(fill=tk.X)
         
         switch = tk.IntVar()
         switch.set(1)
         
         checkbutton = tk.Checkbutton(win, text="Check Button", variable=switch)
         checkbutton.pack()
         
         win.mainloop()
         ```
    7) Entry()
       code:
         ```py
         import tkinter as tk
      
         window = tk.Tk()
         
         label = tk.Label(window, text="Little label:")
         label.pack()
         
         frame = tk.Frame(window, height=30, width=100, bg="#000099")
         frame.pack()
         
         button = tk.Button(window, text="Button")
         button.pack(fill=tk.X)
         
         switch = tk.IntVar()
         switch.set(1)
         
         checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
         checkbutton.pack()
         
         entry = tk.Entry(window, width=10)
         entry.pack()
         
         window.mainloop()
         ```
  
    8) Radiobutton()
        - always work in groups and only one of the widgets inside the group can be checked
       code:
         ```py
         import tkinter as tk
         
         window = tk.Tk()
         
         label = tk.Label(window, text="Little label:")
         label.pack()
         
         frame = tk.Frame(window, height=30, width=100, bg="#000099")
         frame.pack()
         
         button = tk.Button(window, text ="Button")
         button.pack(fill=tk.X)
         
         switch = tk.IntVar()
         switch.set(1)
         
         checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
         checkbutton.pack()
         
         entry = tk.Entry(window, width=30)
         entry.pack()
         
         radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
         radiobutton_1.pack()
         radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
         radiobutton_2.pack()
         
         window.mainloop()
         ```
   
### 9. Event handling
   - `showinfo()` from the messagebox module
   - takes 2 arguments, `messagebox.showinfo(title, info)`
  
     code:
     ```py
     import tkinter
     from tkinter import messagebox
      
     def clicked():
         messagebox.showinfo("info", "some\ninfo")
      
     window = tkinter.Tk()
     button_1 = tkinter.Button(window, text="Show info", command=clicked)
     button_1.pack()
     button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
     button_2.pack()
     window.mainloop()
     ```
      ```py
      import tkinter as tk
      from tkinter import messagebox
      
      def click():
          tk.messagebox.showinfo("Click!","I love clicks!")
      
      window = tk.Tk()
      label = tk.Label(window, text="Label")
      label.pack()
      
      button = tk.Button(window, text="Button", command=click)
      button.pack(fill=tk.X)
      
      frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
      frame.pack()
      
      window.mainloop()
      ```

   - `bind()` takes 2 arguments
   - `widget.bind(event, callback)`
  
     <img width="1870" height="907" alt="image" src="https://github.com/user-attachments/assets/6bbda4d4-a9cb-4b5b-a3d3-5609e54468ef" />


     code:
      ```py
      import tkinter as tk
      from tkinter import messagebox
      
      def click(event=None):
          tk.messagebox.showinfo("Click!", "I love clicks!")
      
      window = tk.Tk()
      label = tk.Label(window, text="Label")
      label.bind("<Button-1>", click)   # Line I
      label.pack()
      
      button = tk.Button(window, text="Button", command=click)
      button.pack(fill=tk.X)
      
      frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
      frame.bind("<Button-1>", click)   # Line II
      frame.pack()
      
      window.mainloop()
      ```

   - To modify a property named `prop`, existing within a widget named `wid`, and setting its value to `val`, you can use the `config()` method, just like here:
   - `wid.config(prop=val)`
   - Clickable widgets (with `command`) → unbind by setting `command=lambda: None`.
   - Non-clickable widgets (with `.bind`) → unbind by using `.unbind(event)`.
   - Changing text or properties → use `.config(prop=value)`.
 
     code:
      ```py
      import tkinter as tk
      from tkinter import messagebox
      
      
      def click(event=None):
          if event is None:
              tk.messagebox.showinfo("Click!", "I love clicks!")
          else:
              string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                       ",num=" + str(event.num) + ",type=" + event.type
              tk.messagebox.showinfo("Click!", string)        
      
      
      window = tk.Tk()
      label = tk.Label(window, text="Label")
      label.bind("<Button-1>", click)
      label.pack()
      
      button = tk.Button(window, text="Button", command=click)
      button.pack(fill=tk.X)
      
      frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
      frame.bind("<Button-1>", click)
      frame.pack()
      
      window.mainloop()
      ```

      ```py
      import tkinter as tk
      from tkinter import messagebox
      
      
      def on_off():
          global switch
          if switch:
              button_2.config(command=lambda: None)
              button_2.config(text="Gee!")
          else:
              button_2.config(command=peekaboo)
              button_2.config(text="Peekaboo!")
          switch = not switch
      
      
      def peekaboo():
          messagebox.showinfo("", "PEEKABOO!")
      
      
      def do_nothing():
          pass
      
      
      switch = True
      window = tk.Tk()
      buton_1 = tk.Button(window, text="On/Off", command=on_off)
      buton_1.pack()
      button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
      button_2.pack()
      window.mainloop()
      ```

   - `.config()` = changing the channel (what’s displayed).
   - `.bind()`/`.unbind()` = plugging in or unplugging the remote (whether button presses do anything).
   
      code:
      ```py
      import tkinter as tk
         
      def on_off():
          global switch
          if switch:
              label.unbind("<Button-1>")
          else:
              label.bind("<Button-1>", rhyme)
          switch = not switch
      
      def rhyme(dummy):
          global word_no, words
          word_no += 1
          label.config(text=words[word_no % len(words)])
         
      switch = True
      words = ["Old", "McDonald", "Had", "A", "Farm"]
      word_no = 0
      window = tk.Tk()
      button = tk.Button(window, text="On/Off", command=on_off)
      button.pack()
      label = tk.Label(window, text=words[0])
      label.bind("<Button-1>", rhyme)
      label.pack()
      window.mainloop()
      ```

   - `bind_all()` and `unbind_all()`
   - `window.bind_all(event, callback)`
   - `window.unbind_all(event)`
     
      code:
      ```py
      import tkinter as tk
      from tkinter import messagebox
      
      def hello(dummy):
          messagebox.showinfo("", "Hello!")
      
      window = tk.Tk()
      button = tk.Button(window, text="On/Off")
      button.pack()
      label = tk.Label(window, text="Label")
      label.pack()
      frame = tk.Frame(window, bg="yellow", width=100, height=20)
      frame.pack()
      window.bind_all("<Button-1>", hello)
      window.mainloop()
      ```

### 10. Widget properties

   - Using dictionaries
   - Assuming that a widget named `Widget` has a property named `prop` and you want to read its value and then set it with a new value, you can do this in the following way:
   - `old_val = Widget["prop"]`
   - `Widget["prop"] = new_val`

     code:
      ```py
      import tkinter as tk

      def on_off():
          global button
          state = button["text"]
          if state == "ON":
              state = "OFF"
          else:
              state = "ON"
          button["text"] = state
      
      window = tk.Tk()
      button = tk.Button(window, text="OFF", command=on_off)
      button.place(x=50, y=100, width=100)
      window.mainloop()
      ```
   - Using `cget()` to read a propertys value and `config()` to set a value for one
     code:
      ```py
      import tkinter as tk
      
      def on_off():
          global button
          state = button.cget("text")
          if state == "ON":
              state = "OFF"
          else:
              state = "ON"
          button.config(text=state)
      
      window = tk.Tk()
      button = tk.Button(window, text="OFF", command=on_off)
      button.place(x=50, y=100, width=100)
      window.mainloop()
      ```
   - Fonts (`font`)
   - Any font can be described as two- or three-element tuples:
   - `("font_family_name", "font_size")`
   - `("font_family_name", "font_size", "font_style")`
   - Third parameter can be one of:
     - "bold"
     - "italic"
     - "underline"
     - "overstrike"

     code:
      ```py
      import tkinter as tk
      
      window = tk.Tk()
      label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
      label_1.grid(column=0, row=0)
      label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
      label_2.grid(column=0, row=1)
      label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
      label_3.grid(column=0, row=2)
      window.mainloop()
      ```


     <img width="964" height="477" alt="image" src="https://github.com/user-attachments/assets/4e6d60b2-4aab-4ac7-ab68-08fe57e462f7" />

     code:
      ```py
      import tkinter as tk

      window = tk.Tk()
      button_1 = tk.Button(window, text="Ordinary button");
      button_1.pack()
      button_2 = tk.Button(window, text="Exceptional button")
      button_2.pack()
      button_2["borderwidth"] = 10
      button_2["highlightthickness"] = 10
      button_2["padx"] = 10
      button_2["pady"] = 5
      button_2["underline"] = 1
      window.mainloop()
      ```

     <img width="742" height="374" alt="image" src="https://github.com/user-attachments/assets/b65936b8-02d7-4ec9-a454-678d58bb44bf" />

     code:
      ```py
      import tkinter as tk

      window = tk.Tk()
      button_1 = tk.Button(window, text="Ordinary button");
      button_1.pack()
      button_2 = tk.Button(window, text="Colorful button")
      button_2.pack()
      button_2.config(bg ="#000000")
      button_2.config(fg ="yellow")
      button_2.config(activeforeground ="#FF0000")
      button_2.config(activebackground ="green")
      window.mainloop()
      ```

   - Anchors (`anchor`), an imaginary (invisible) point inside the widget to which the text (if any) is anchored

     <img width="746" height="559" alt="image" src="https://github.com/user-attachments/assets/45ea3816-d50a-4004-9484-20beda85e065" />

     code:
      ```py
      import tkinter as tk

      window = tk.Tk()
      button_1 = tk.Button(window, text="Regular button");
      button_1["anchor"] = E
      button_1["width"] = 20  # pixels!
      button_1.pack()
      button_2 = tk.Button(window, text="Another button")
      button_2["anchor"] = SW
      button_2["width"] = 20
      button_2["height"] = 3  # rows
      button_2.pack()
      window.mainloop()
      ```

      Output (since the anchor chars like E or SW are not identified):
      <img width="275" height="201" alt="image" src="https://github.com/user-attachments/assets/484246fb-77f4-49ce-9acb-594ec70c1b5e" />

   - Cursors (the `cursor` property)
     code:
      ```py
      import tkinter as tk
      
      window = tk.Tk()
      label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
      label_1.pack()
      label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
      label_2.pack()
      label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
      label_3.pack()
      window.mainloop()
      ```

   - `after()` and `after_cancel()`
   - `Widget.after(time_ms, function)` takes 2 arguments, time interval and a function to call
   - `Widget.after_cancel(id)`  cancels the planned invocation identified by the `id` argument
     
     code:
      ```py
      import tkinter as tk
      
      def blink():
          global is_white
          if is_white:
              color = 'black'
          else:
              color = 'white'
          is_white = not is_white
          frame.config(bg=color)
          frame.after(500, blink)
      
      is_white = True
      window = tk.Tk()
      frame = tk.Frame(window, width=200, height=100, bg='white')
      frame.after(500, blink)
      frame.pack()
      window.mainloop()
      ```

   - The `destroy()` method
   - Works recursively destroying the widget, erasing it from the event manager and destroying the widgets children

     code:
      ```py
      import tkinter as tk
      
      def blink():
          global is_white
          if is_white:
              color = 'black'
          else:
              color = 'white'
          is_white = not is_white
          frame.config(bg=color)
          frame.after(500, blink)
      
      is_white = True
      window = tk.Tk()
      frame = tk.Frame(window, width=200, height=100, bg='white')
      frame.after(500, blink)
      frame.pack()
      window.mainloop()
      ```

   - Methods `focus_get()` and `focus_set()`
   - `focus_get()` returns a reference to the currently focused widget, or None when no widget owns the focus
   - `focus_set()` focuses the widget from the method which was invoked

     code:
      ```py
      import tkinter as tk
      
      def flip_focus():
          if window.focus_get() is button_1:
              button_2.focus_set()
          else:
              button_1.focus_set()
          window.after(1000, flip_focus)
      
      window = tk.Tk()
      button_1 = tk.Button(window, text="First")
      button_1.pack()
      button_2 = tk.Button(window, text="Second")
      button_2.pack()
      window.after(1000, flip_focus)
      window.mainloop()
      ```
      ```py
      import tkinter as tk

      def jumpthefocus():
          if window.focus_get() is button_1:
              button_2.focus_set()
          elif window.focus_get() is button_2:
              button_3.focus_set()
          else: button_1.focus_set()
          window.after(1000, jumpthefocus)
      
      window = tk.Tk()
      button_1 = tk.Button(window, text="First")
      button_1.pack()
      button_2 = tk.Button(window, text="Second")
      button_2.pack()
      button_3 = tk.Button(window, text="Third")
      button_3.pack()
      window.after(1000, jumpthefocus)
      window.mainloop()
      ```

### 11. Variables

   - Observable variables
      - such a var is an object of the container class
      - any change of the variable’s state can be observed by a number of external agents
      - typed variables, be aware of what type of value you want to store in them, and don’t change your mind during the variable’s life
      - you can only create an observable variable after the main window initialization
   - The 4 types of observable variables and they are initially set to:
      - `BooleanVar` --> Boolean `False`
      - `DoubleVar` --> Float `0.0`
      - `IntVar` --> Integer `0`
      - `StringVar` String `""`
   - Initializing variables, setting and getting values (`set()` & `get()` methods)
      - Initialize a string for example by: `s = StringVar()`
      - Set a value to it using the `set()` method: `s.set("I box and ball")`
      - Get the value using the `get()` method: `value = s.get()`
    
      code:
      ```py
      import tkinter as tk
      
      window = tk.Tk()
      a_string = tk.IntVar()
      a_string.set(4)
      print(a_string.get())
      ```
### 12. Variable Observers (trace)

- Tkinter variables (`StringVar`, `IntVar`, etc.) can have **observers** (callbacks) triggered on read, write, or delete.  
- Add observer using `trace()`:

    code:
    
    ```py
    obsid = var.trace(mode, callback)
    ```

- **Mode options:**  
    - `"r"` – read (`get()`)  
    - `"w"` – write (`set()`)  
    - `"u"` – delete (`del`)  

- **Callback function:**  

    code:
    ```py
    def callback(*args):
        print("Triggered")
    ```

- Remove observer using `trace_vdelete()`:

    code:
    ```py
    var.trace_vdelete(mode, obsid)
    ```

- **Example:**

    code:

    ```python
    import tkinter as tk


    def r_observer(*args):
        print("Reading")


    def w_observer(*args):
        print("Writing")


    dummy = tk.Tk()    # we need this although we won't display any windows
    variable = tk.StringVar()
    variable.set("abc")
    r_obsid = variable.trace("r", r_observer)
    w_obsid = variable.trace("w", w_observer)
    variable.set(variable.get() + 'd')  # read followed by write
    variable.trace_vdelete("r", r_obsid)
    variable.set(variable.get() + 'e')
    variable.trace_vdelete("w", w_obsid)
    variable.set(variable.get() + 'f')
    print(variable.get())
    ```

-  Observers monitor variable changes automatically.


## Module 2

### 1. Button

-  Properties
    | Property   | Meaning |
    | :--------- | :------ |
    | `command`  | The callback invoked when the button is clicked. |
    | `justify`  | How the text inside the button is justified: `LEFT`, `CENTER`, or `RIGHT`. |
    | `state`    | Button’s state: `DISABLED` → unclickable and gray, `NORMAL` → active, `ACTIVE` → when mouse hovers over it. |

-  Methods
    | Method     | Role |
    | :--------- | :--- |
    | `flash()`  | Makes the button flash a few times without changing its state. |
    | `invoke()` | Runs the callback assigned to the button and returns its value (the proper way to call it programmatically). |



### 2. Checkbutton

- Properties

    | Property    | Meaning |
    | :---------- | :------ |
    | `bd`        | Frame (border) width of the checkbutton (default: 2 pixels). |
    | `command`   | Callback invoked when the checkbutton changes state. |
    | `justify`   | Same as in `Button`. |
    | `state`     | Same as in `Button`. |
    | `variable`  | An observable `IntVar` reflecting the checkbutton’s state (`1` if checked, `0` otherwise). |
    | `offvalue`  | Value assigned to `variable` when unchecked (default: `0`). |
    | `onvalue`   | Value assigned to `variable` when checked (default: `1`). |

- Methods

    | Method       | Role |
    | :----------- | :--- |
    | `deselect()` | Unchecks the widget. |
    | `flash()`    | Same as in `Button`. |
    | `invoke()`   | Same as in `Button`. |
    | `select()`   | Checks the widget. |
    | `toggle()`   | Toggles the widget (switches its state to the opposite one). |


    code:

    ```py
    import tkinter as tk

    def switch():
        if button1.cget("state") == tk.NORMAL:
            button1.flash()
            button1.config(state = tk.DISABLED)
            button2["text"] = "Enable"
        else:
            button1.flash()
            button1.config(state = tk.NORMAL)
            button2["text"] = "Disable"


    def mousein(*args):
        button1["bg"] = "grey"

    def mouseout(*args):
        button1["bg"] = "white"

    main = tk.Tk()

    button1 = tk.Button(main, text = "hi", state = tk.NORMAL)
    button1.pack()
    button1.bind("<Enter>", mousein)
    button1.bind("<Leave>", mouseout)

    button2 = tk.Button(main, text = "Disable",
                        command = switch)
    button2.pack()
    main.mainloop()

    ```

    ```py
    import tkinter as tk
    from tkinter import messagebox

    window = tk.Tk()

    def show():
        messagebox.showinfo("Status", "First:" + str(count1.get()) + ", Second:" + str(count2.get()))
        

    def hit2():
        count2.set(count1.get())
        

    def hit1():
        count1.set(count2.get())
        

    count1 = tk.IntVar()
    count2 = tk.IntVar()

    pizza = tk.Radiobutton(window, text = "Pizza", variable=count1, value = 1, command = hit2)
    pizza.pack()

    pep = tk.Radiobutton(window, text = "Pepperoni", variable=count1, value = 1, command = hit2)
    pep.pack()

    water = tk.Radiobutton(window, text = "Water", variable=count2, value = 2, command = hit1)
    water.pack()

    juice = tk.Radiobutton(window, text = "Juice", variable=count2, value = 2, command = hit1)
    juice.pack()


    show_button = tk.Button(window, text = "Show status", command=show)
    show_button.pack()

    window.mainloop()
    ```

### 3. Non-clickable widgets
#### 1. `textvariable`

| Label property | Property meaning |
|----------------|------------------|
| `text`         | a string which will be **shown** within the `Label`; note: newline characters (`\n`) are interpreted in the usual way |
| `textvariable` | the same as for `text`, but makes use of an observable `StringVar` variable, so if you change the variable’s alteration, it will be immediately visible on the screen. |

code:

```py
import tkinter as tk
window = tk.Tk()

def changetext():
    global counter
    return f"Count = {count}"

def clicked():
    global count
    count += 1
    finalstring.set(changetext())

count = 0
finalstring = tk.StringVar()
finalstring.set("Count = 0")

click = tk.Button(window, text = "Click me", command = clicked)
click.pack()
text = tk.Label(window, textvariable= finalstring, height = 5)
text.pack()

window.mainloop()
```

#### 2. `Message`

- Very similar to the Label (among other things, it has the same properties) but is able to format the presented text by fitting it automatically to the widget’s size.

code:
```py
import tkinter as tk


def do_it_again():
    text.set(text.get() + "and again...")


window = tk.Tk()
button = tk.Button(window, text="Go ahead!", command=do_it_again)
button.pack()
text = tk.StringVar()
message = tk.Message(window, textvariable=text, width=400)
text.set("You did it again... ")
message.pack()
window.mainloop()
```

#### 3. `takefocus` & `labelanchour`frame propertes for `LabelFrame()`

- The `LabelFrame` widget is a Frame enriched with a visible border and a title (also visible).
- The `takefocus` property controls whether a widget can be focused using the **Tab** key during keyboard navigation.
- The `labelanchour` property puts labels on one of the 12 positions on the `LabelFrame` borders (e.g. n, ne, nw)

code

```py
import tkinter as tk

window = tk.Tk()

frame_1 = tk.Frame(window, width=200, height=100, bg='white')
frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')

label_frame_1 = tk.LabelFrame(window, text="Frame #1",
                              width=200, height=100, bg='white')
label_frame_2 = tk.LabelFrame(window, text="Frame #2",
                              labelanchor='se', width=200, height=100, bg='yellow')

# Buttons inside Frame 1
button_1_1 = tk.Button(label_frame_1, text="Button #1 (Focusable)", takefocus=True)
button_1_2 = tk.Button(label_frame_1, text="Button #2 (NOT Focusable)", takefocus=False)

# Buttons inside Frame 2
button_2_1 = tk.Button(label_frame_2, text="Button #1 (Focusable)", takefocus=True)
button_2_2 = tk.Button(label_frame_2, text="Button #2 (NOT Focusable)", takefocus=False)

# Place buttons in frames
button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

label_frame_1.pack()
label_frame_2.pack()
window.mainloop()
```

#### 4. `Entry` properties & methods
- Tkinter `Entry` Widget Properties

    | Entry property | Property meaning |
    | :--- | :--- |
    | **`command`** | Although **`Entry`** is obviously a clickable widget, it doesn't allow you to bind a callback through the **`command`** property. You can observe and control all occurring changes instead by setting the **tracer function** for the **observable variable** which cooperates with **`Entry`** (we'll show you this - be patient!) |
    | **`show`** | a string assigned to this property will be displayed instead of the **actual** characters entered into the input field; e.g., if you set `show='*'`, this will enable the widget to safely edit the user's password |
    | **`state`** | the same as for **`Button`** |
    | **`textvariable`** | an observable **`StringVar`** reflecting the current state of the input field |
    | **`width`** | the input field's **width** (in characters) |



- Tkinter `Entry` Widget Methods

    | Entry method | Method role |
    | :--- | :--- |
    | **`get()`** | returns the current input field's contents as a **string** |
    | **`set(s)`** | sets the whole input field's contents with the **`s`** string |
    | **`delete(first, last=None)`** | deletes a part of the input field's contents; **`first`** and **`last`** can be integers with values indexing the string; if the **`last`** argument is omitted, a single character is deleted; if **`last`** is specified as **`END`**, it points to the place after the last field's character |
    | **`insert(index, s)`** | inserts the **`s`** string at the field position pointed to by **`index`** |

- `focus_set` - to focus the widget automatically

code:

```py
import tkinter as tk

def digits_only(*args):
    global last_string
    string = text.get()
    if string == '' or string.isdigit():  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)

last_string = ''
window = tk.Tk()
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
text.set(last_string)
text.trace('w', digits_only)
entry.pack()
entry.focus_set()
window.mainloop()
```

### 4. Menus

- `Menu()` - create a tkinter menu
- `config()` - to embed the main menu in the window
- `add_cascade()` - add a submenu to a parent menu (or main menu initially)
- `add_command()` - bind a callback to the menu

    code:

    ```py
    import tkinter as tk
    from tkinter import messagebox


    def about_app():
        messagebox.showinfo("App", "The application\nthat does nothing")


    window = tk.Tk()

    # main menu creation
    main_menu = tk.Menu(window)
    window.config(menu=main_menu)

    # 1st main menu item: an empty (as far) submenu
    sub_menu_file = tk.Menu(main_menu)
    main_menu.add_cascade(label="File", menu=sub_menu_file)

    # 2nd main menu item: a simple callback
    sub_menu_help = tk.Menu(main_menu)
    main_menu.add_command(label="About...", command=about_app)

    window.mainloop()
    ```

- `underline`to set hot keys
    - `underline = 0` = ALT + F
    - `underline = 1` = ALT + B
    - all hot keys must be unique

        code:

        ```py
        import tkinter as tk
        from tkinter import messagebox


        def about_app():
            messagebox.showinfo("App", "The application\nthat does nothing")


        window = tk.Tk()

        main_menu = tk.Menu(window)
        window.config(menu=main_menu)
        sub_menu_file = tk.Menu(main_menu)
        # setting the hotkey to "Alt-F"
        main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
        sub_menu_help = tk.Menu(main_menu)
        # setting the hotkey to "Alt-B"
        main_menu.add_command(label="About...", command=about_app, underline=1)

        window.mainloop()
        ```
    - `messagebox.askyesno()` - returns True if Yes is chosen or False otherwise.

        code:

        ```py
        import tkinter as tk
        from tkinter import messagebox


        def about_app():
            messagebox.showinfo("App", "The application\nthat does nothing")


        def are_you_sure():
            if messagebox.askyesno("", "Are you sure you want to quit the App?"):
                window.destroy()


        window = tk.Tk()

        main_menu = tk.Menu(window)
        window.config(menu=main_menu)
        sub_menu_file = tk.Menu(main_menu)
        main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
        # add the QUIT action to the submenu
        sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
        sub_menu_help = tk.Menu(main_menu)
        main_menu.add_command(label="About...", command=about_app, underline=1)

        window.mainloop()
        ```

- `tearoff` to remove the dashed line off submenus
    - `tearoff = 0` to disable the dashed line as the submenu's first element, `1` to enable it

        code:

        ```py
        import tkinter as tk
        from tkinter import messagebox


        def about_app():
            messagebox.showinfo("App", "The application\nthat does nothing")


        def are_you_sure():
            if messagebox.askyesno("", "Are you sure you want to quit the App?"):
                window.destroy()


        window = tk.Tk()

        main_menu = tk.Menu(window)
        window.config(menu=main_menu)
        # we don't want the tear-off here  
        sub_menu_file = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
        sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
        sub_menu_help = tk.Menu(main_menu)
        main_menu.add_command(label="About...", command=about_app, underline=1)

        window.mainloop()
        ```

- `add_separator()` to seperate elements on a submenu

    code:

    ```py
    import tkinter as tk
    from tkinter import messagebox


    def about_app():
        messagebox.showinfo("App", "The application\nthat does nothing")


    def are_you_sure():
        if messagebox.askyesno("", "Are you sure you want to quit the App?"):
            window.destroy()


    def open_file():
        messagebox.showinfo("Open doc", "We'll open a file here...")


    window = tk.Tk()

    main_menu = tk.Menu(window)
    window.config(menu=main_menu)
    sub_menu_file = tk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
    sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
    # separator is here!
    sub_menu_file.add_separator()
    sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
    sub_menu_help = tk.Menu(main_menu)
    main_menu.add_command(label="About...", command=about_app, underline=1)

    window.mainloop()
    ```

- `add_cascade()` - to have a submenu's items unroll another cascade

    code:

    ```py
    import tkinter as tk
    from tkinter import messagebox


    def about_app():
        messagebox.showinfo("App", "The application\nthat does nothing")


    def are_you_sure():
        if messagebox.askyesno("", "Are you sure you want to quit the App?"):
            window.destroy()


    def open_file():
        messagebox.showinfo("Open doc", "We'll open a file here...")


    window = tk.Tk()

    main_menu = tk.Menu(window)
    window.config(menu=main_menu)
    sub_menu_file = tk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
    sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
    sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
    sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

    for i in range(8):
        number = str(i + 1)
        sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

    sub_menu_file.add_separator()
    sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
    sub_menu_help = tk.Menu(main_menu)
    main_menu.add_command(label="About...", command=about_app, underline=1)

    window.mainloop()
    ```

- `accelerator` - to display a keyboard shortcut (accelerator text) next to the menu item
- `bind`
    - to bind a key
    - attaches an event only to a specific widget
    - the event handler will run only if that widget has focus (or is directly interacted with).
    - e.g. `window.bind("<Control-q>", function)`
- `bind_all`
    - to bind a key
    - attaches an event handler to the entire application (all widgets).
    - the event will trigger no matter which widget has focus, as long as the event happens inside the Tkinter window.
    - e.g. `window.bind_all("<Control-a>", function)`

        code:

        ```py
        import tkinter as tk
        from tkinter import messagebox


        def about_app():
            messagebox.showinfo("App", "The application\nthat does nothing")


        def are_you_sure(event=None):
            if messagebox.askyesno("", "Are you sure you want to quit the App?"):
                window.destroy()


        def open_file():
            messagebox.showinfo("Open doc", "We'll open a file here...")


        window = tk.Tk()

        main_menu = tk.Menu(window)
        window.config(menu=main_menu)
        sub_menu_file = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
        sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
        sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
        sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

        for i in range(8):
            number = str(i + 1)
            sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

        sub_menu_file.add_separator()
        sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q",
                                underline=0, command=are_you_sure)
        sub_menu_help = tk.Menu(main_menu)
        main_menu.add_command(label="About...", command=about_app, underline=1)

        window.bind_all("<Control-q>", are_you_sure)
        window.mainloop()
        ```

- `entryconfigure()` to manipulate a menu’s item
    - takes 2 arguments, `item.entryconfigure(i, prop=value)`
    - the first is an integer index of the modified item (entry)
    - the second is a keyworded argument pointing to the modified property
    - e.g. `sub_menu.entryconfigure(1, state=accessible)`
    - | Property     | Property role                                                                 |
        |--------------|-------------------------------------------------------------------------------|
        | `postcommand`| a **callback** invoked every time a menu’s item is activated                  |
        | `tearoff`    | set to zero **removes** the tear-off decoration from the top of the cascade   |
        | `state`      | when set to **DISABLED**, the menu item is grayed and inaccessible; setting it to **ACTIVE** restores its normal functionality |
        | `accelerator`| a **string** describing a hot-key bound to the menu’s item                    |


        | Method                        | Method role                                                                 |
        |-------------------------------|------------------------------------------------------------------------------|
        | `add_cascade(prop=val, …)`    | adds a **cascade** to the menu’s item                                         |
        | `add_command(prop=val, …)`    | assigns an **action** to the menu’s item                                     |
        | `add_separator()`             | adds an **separator** line to the menu                                       |
        | `entryconfigure(i, prop=val,…)` | modifies the *i*-th menu item’s property named **prop**                    |


        code:

        ```py
        import tkinter as tk

        def on_off():
            global accessible
            if accessible == tk.DISABLED:
                accessible = tk.ACTIVE
            else:
                accessible = tk.DISABLED
            sub_menu.entryconfigure(0, state=accessible)

        accessible = tk.DISABLED
        window = tk.Tk()
        menu = tk.Menu(window)
        window.config(menu=menu)
        sub_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Menu", menu=sub_menu)
        sub_menu.add_command(label="On/Off", command=on_off)
        sub_menu.add_command(label="Switch", state=tk.DISABLED)
        window.mainloop()
        ```

### 5. Interacting with the Window & User

- A basic window title counter on click

    code:

    ```py
    import tkinter as tk

    def click(*args):
        global counter
        if counter > 0:
            counter -= 1
        window.title(str(counter))

    counter = 10
    window = tk.Tk()
    window.title(str(counter))
    window.bind("<Button-1>", click)
    window.mainloop()
    ```

- `.call` & `PhotoImage()`
    - `.call` to run raw Tcl/Tk commands as if you were writing Tcl code instead of Python
    - `PhotoImage()` creates a Tk image object and passes it along
    - Changing the main window’s icon
    - code:

        ```py
        import tkinter as tk

        window = tk.Tk()
        window.title('Icon?')
        window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))
        window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
        window.mainloop()
        ```

- `geometry()`
    - to resize the main window in a custom way
    - takes in a string for the dimensions; `width x height`
    
        code:

        ```py
        import tkinter as tk

        def click(*args):
            global size, grows
            if grows:
                size += 50
                if size >= 500:
                    grows = False
            else:
                size -= 50
                if size <= 100:
                    grows = True
            window.geometry(str(size) + "x" + str(size))

        size = 100
        grows = True
        window = tk.Tk()
        window.geometry("100x100")
        window.bind("<Button-1>", click)
        window.mainloop()
        ```

- `minsize()`
    - to specify the minimum dimensions of a window
    - takes 2 arguments, `width` & `height`

        code:

        ```py
        import tkinter as tk

        window = tk.Tk()
        window.minsize(width=250, height=200)
        window.geometry("500x500")
        window.mainloop()
        ```

- `maxsize()`
    - to specify the maximum dimensions of a window
    - takes 2 arguments, `width` & `height`

        code:
        ```py
        import tkinter as tk

        window = tk.Tk()
        window.maxsize(width=500, height=300)
        window.geometry("200x200")
        window.mainloop()
        ```

- `resizable`
    - to disable the user from changing the width, height or both of a window

        code:
        ```py
        import tkinter as tk

        window = tk.Tk()
        window.resizable(width=False, height=False)
        window.geometry("400x200")
        window.mainloop()
        ```

- `protocol()`
    - to intercept and handle window manager events (things the OS/desktop does to your window)
    - most common is `protocol("WM_DELETE_WINDOW", callback)`
        
        code:

        ```py
        import tkinter as tk
        from tkinter import messagebox

        def really():
            if messagebox.askyesno("?", "Wilt thou be gone?"):
                window.destroy()

        window = tk.Tk()
        window.protocol("WM_DELETE_WINDOW", really)
        window.mainloop()
        ```

- `messagebox`
    - `askyesno` - to get yes/no user responses, returns True if Yes or False otherwise
    - | Option     | Purpose                | Example                                |
        |------------|------------------------|----------------------------------------|
        | `title`    | Window title           | `title="Hello!"`                       |
        | `message`  | Dialog text            | `message="Be careful!\nLine 2"`        |
        | `options`  | Which buttons appear   | `askyesno`, `askretrycancel`, etc.     |
        | `default`  | Pre-selected button    | `default=messagebox.NO`                |
        | `icon`     | Icon type              | `icon="warning"`                       |
    - code:
        ```py
        import tkinter as tk
        from tkinter import messagebox


        def question():
            answer = messagebox.askyesno("?", "To be or not to be?")
            print(answer)


        window = tk.Tk()
        button = tk.Button(window, text="Ask the question!", command=question)
        button.pack()
        window.mainloop()
        ```

- `askokcancel()`
    -  creates a dialog equipped with two buttons titled `OK` and `Cancel` (it returns `True` for `OK` and `False` otherwise)

        code:
        ```py
        import tkinter as tk
        from tkinter import messagebox


        def question():
            answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
            print(answer)


        window = tk.Tk()
        button = tk.Button(window, text="What are your plans?", command=question)
        button.pack()
        window.mainloop()
        ```

- `askretrycancel()`
    -  creates a dialog containing a **warning** sign instead of a question mark and two buttons titled `Retry` and `Cancel` (it returns `True` for `Retry` and `False` otherwise).

        code:

        ```py
        import tkinter as tk
        from tkinter import messagebox


        def question():
            answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
            print(answer)


        window = tk.Tk()
        button = tk.Button(window, text="What are your plans?", command=question)
        button.pack()
        window.mainloop()
        ```

- `askquestion()`
    -  displays two buttons titled `Yes` and `No` along with a question mark icon, but **returns a string** `yes` when the user’s answer is positive and `no` otherwise

        code:

        ```py
        import tkinter as tk
        from tkinter import messagebox


        def question():
            answer = messagebox.askquestion("?", "I'm going to format your hard drive")
            print(answer)


        window = tk.Tk()
        button = tk.Button(window, text="What are your plans?", command=question)
        button.pack()
        window.mainloop()
        ```

- `showerror()`
    - displays a red warning icon and doesn’t ask any questions – its only button is titled `OK` and returns a **string** `ok` in every case

        code:

        ```py
        import tkinter as tk
        from tkinter import messagebox


        def question():
            answer = messagebox.showerror("!", "Your code does nothing!")
            print(answer)


        window = tk.Tk()
        button = tk.Button(window, text="Alarming message", command=question)
        button.pack()
        window.mainloop()
        ```

- `showwarning()`
    - presents a warning icon and always its only button is titled `OK` and returns a string `ok`.

        code:
        ```py
        import tkinter as tk
        from tkinter import messagebox


        def question():
            answer = messagebox.showwarning("Be careful!", "Pull up before its too late!")
            print(answer)


        window = tk.Tk()
        button = tk.Button(window, text="What's going on?", command=question)
        button.pack()
        window.mainloop()
        ```

### 6. Canvas

- `Canvas()` & `create_line()`
    - use the `Canvas` constructor to create a canvas
    - `create_line` takes a sequence of coordinates: `canvas.create_line(x1, y1, x2, y2, x3, y3, ..., options...)`
        - From (x1, y1) → (x2, y2)
        - Then (x2, y2) → (x3, y3)
        - And so on.
    - | Property name | Property role |
        |------------|------------------------------------------------------------|
        | `borderwidth`| canvas border's **width** in pixels (default: 2)           |
        | `background` (`bg`)| canvas border's **color** (default: the same as the underlying window's color)|
        | `height`    | canvas **height** (in pixels)                              |
        | `width`     | canvas **width** (in pixels)                               |

        code:

        ```py
        import tkinter as tk


        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
        canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

- `create_line()` options

    - | Option name         | Option meaning |
        |--------------------|------------------------------------------------------------|
        | `arrow`             | normally, the chain ends aren't marked in any special way, but you may want them to be finished with **arrowheads**; setting the arrow option to **FIRST** results in drawing an arrowhead at the chain's beginning, **LAST** at the chain's end, **BOTH** at both sides of the chain. |
        | `fill`              | chain **color** (setting the option to an empty string causes the line to be transparent) |
        | `smooth`            | setting it to **True** rounds the chain's corners using a set of connected parabolas |
        | `width`             | line **width** (default: 1 pixel) |

        code:

        ```py
        import tkinter as tk

        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
        canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380,
                        arrow=tk.BOTH, fill='red', smooth=True, width=3)
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

- `create_rectangle()`
    - the method draws a rectangle specified with two opposite vertices at the `(x0,y0)` and `(x1,y1)` points
    - | Option name | Option meaning |
        |------------|------------------------------------------------------------|
        | `outline`   | rectangle **edge color** (if specified as an empty string, the edge is transparent)|
        | `fill`      | rectangle **interior color** |
        | `width`     | rectangle **edge width** in pixels (default: 1)            |

        code:

        ```py
        import tkinter as tk

        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='black')
        canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

- `create_polygon()`
    - similar to `create_line()` but the last segment connects to the first automatically
        
        code:

        ```py
        import tkinter as tk

        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='black')
        canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

- `create_oval()`
    - draws an ellipse inscribed in a rectangle with vertices at the points `(x0,y0)` and `(x1,y1)`
    - if the rectangle is a square, the ellipse becomes a circle

        code:

        ```py
        import tkinter as tk

        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='blue')
        canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

- `create_arc()`
    - `canvas.create_arc(x0,y0,x1,y1,option...)`
    - options are the same as for `create_polygon()` except for the folllowing 3 new methods
    - the method draws the arc of an ellipse inscribed inside a rectangle with vertices at points `(x0,y0)` and `(x1,y1)`
    - | Option name | Option meaning |
        |------------|------------------------------------------------------------|
        | `style`     | can be set to one of the following: **PIESLICE** (default), **CHORD** and **ARC**|
        | `start`     | the **angle** (in degrees) of the arc's start relative to the X-axis (e.g., 90 means the highest point of the ellipse, while 0 is the right-most point. The default is 0)|
        | `extent`    | the arc's **span** (in degrees) relative to the start point; note: the span is calculated counter-clockwise. The default is 90 (a quarter of an ellipse)|
        
        code:

        ```py
        import tkinter as tk

        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
        canvas.create_arc(10, 100, 380, 300, outline='red', width=5)
        canvas.create_arc(10, 100, 380, 300, outline='blue', width=5,
                        style=tk.CHORD, start=90, fill='white')
        canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
                        style=tk.ARC, start=180, extent=180)
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

- `create_text()`
    - this method puts text on the `Canvas`, the text is placed inside a rectangle whose center is located at point `(x,y)`:
        - `c.create_text(x, y, option...)`

    - | Option name | Option meaning |
        |------------|------------------------------------------------------------|
        | `fill`      | text **color** |
        | `font`      | text **font** |
        | `justify`   | text **justification**: **LEFT** (default), **CENTER**, **RIGHT**|
        | `text`      | **text** to display (`\n` works as expected)               |
        | `width`     | normally, the rectangle is as wide as the **longest text line**; using the width option forces the text to be aligned to that size|

        code:

        ```py
        import tkinter as tk

        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='blue')
        canvas.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
                        font=("Arial","40","bold"),
                        justify=tk.CENTER,
                        fill='white')
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

- `create_image()`
    - this method draws an image (a bitmap) on the `Canvas`, The image is placed inside a rectangle whose center is located at point `(x, y)`:
        - `canvas.create_image(x, y, option...)`
    - `image` option:
        - an object of the `PhotoImage` class containing the image itself; the `PhotoImage` class constructor needs a keyword argument named `file` pointing to a **bitmap file** (note: only GIF and PNG formats are accepted); the argument should specify the file’s path
        
        code:
        
        ```py
        import tkinter as tk

        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
        image = tk.PhotoImage(file='logo.png')
        canvas.create_image(200, 200, image=image)
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

    - to use a `JPEG` bitmap:
        - import the `Image` and `ImageTk` classes from the PIL (Python Image Library) module
        - build an object of the `Image()` class and use its `open()` method to fetch the bitmap from the file (the argument should specify the file’s path)
        - convert this object into a `PhotoImage` class object using an `ImageTk` function of the same name;
        ` continue as usual

        code:

        ```py
        import tkinter as tk
        import PIL

        window = tk.Tk()
        canvas = tk.Canvas(window, width=400, height=400, bg='red')
        jpg = PIL.Image.open('logo.jpg')
        image = PIL.ImageTk.PhotoImage(jpg)
        canvas.create_image(200, 200, image=image)
        button = tk.Button(window, text="Quit", command=window.destroy)
        canvas.grid(row=0)
        button.grid(row=1)
        window.mainloop()
        ```

## Lab
