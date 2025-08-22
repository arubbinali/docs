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

6) `messagebox`, `askquestion()` & modal windows
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

.
7)
