# Course 1: GUI Programming

> ## Module 1

1) `Tk()` & `mainloop()`:
   - The main application window (which is often the only window being used by the application) is created by the tkinter method named `Tk()`.
   - To start the controller, you have to invoke the main window's method, named `mainloop()`.
  
      code:
            
      ```py
      import tkinter
   
      skylight = tkinter.Tk()
      skylight.mainloop()
      ```

2) `title()`
   - to name window's title bar
   
     code:
  
      ```py
      import tkinter
   
      skylight = tkinter.Tk()
      skylight.title("Skylight")
      skylight.mainloop()
      ```

3) `Button()` & `place()`
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

4) Event handler
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

5) `messagebox`, `askquestion()` & modal windows
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

6)  Gemoetry managers - place, grid & pack
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

7) Coloring widgets
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

8) A GUI application from scratch
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
   
9) Event handling
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





















    
