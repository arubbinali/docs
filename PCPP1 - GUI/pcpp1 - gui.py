"""
بسم الله الرحمان الرحيم


--------------------------------------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------------------------------
                                                        Module 1
--------------------------------------------------------------------------------------------------------------------------

1) Tk() & mainloop()
        The main application window (which is often the only window being used by the application) is created by the tkinter method named Tk()
        To start the controller, you have to invoke the main window's method, named mainloop()

        code:

            import tkinter

            skylight = tkinter.Tk()
            skylight.mainloop()

2) title()
        to name window's title bar

        code:

            import tkinter

            skylight = tkinter.Tk()
            skylight.title("Skylight")
            skylight.mainloop()


3) Button() & place()
        create a Button class object and place it inside the main window
        first argument is obligatory (a reference to the target window), others are optional
        the argument `text` displayts text on the button

        place() used to place the widget inside a window
        x & y coordinates are given, and the widget is placed having the x axis on the top & y axis on the left, unlike the cartesian system
        
        code:

            import tkinter

            skylight = tkinter.Tk()
            skylight.title("Skylight")
            button = tkinter.Button(skylight, text="Bye!")
            button.place(x=10, y=10)
            skylight.mainloop()

4) Event handler
        a piece of code responsible for responding to all clicks addressed to a button
        this will only be invoked by the controller
        
        a function designed to be invoked by someone/something else (not us)

        the argument `command` t's set with the name of a callback that will be invoked when the button is clicked
        there are no parentheses, as we don't want to invoke the callback here – we need its name to be passed to the Button object

        code:

            import tkinter

            def Click():
                skylight.destroy()
                
            skylight = tkinter.Tk()
            skylight.title("Skylight")
            button = tkinter.Button(skylight, text="Bye!", command=Click)
            button.place(x=10, y=10)
            skylight.mainloop()

5) messagebox, askquestion() & modal windows
        modal window --> a window which grabs the whole of the application's focus
        messagebox creates dialog boxes intended to ask questions, display messages, and to receive a user's reply
        the dialog box is an example of a modal window
        askquestion(), takes in 2 arguments, dialog window title & the text inside the window

        code:

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

6)  Gemoetry managers - place, grid & pack
        place - user decides where the widget goes by mentioning the x and y coordinates
        grid - gives you a chance to express your general wishes and tries to deploy the widgets according to them
                they aren't as precise as the ones used by place, but are far more detailed than those utilized by pack
        pack - tries and finds the best possible location for each widget

        these managers cannot be mixed. Only one of them can be used in one application

        place:

            parameters: h, w, x, y
                h & w - height and width, f the parameters are omitted, the widget's height & width will be determined automatically
                x - the widget's top-left pixel's horizontal coordinate measured relative to the home window's top-left corner
                y - the widget's top-left pixel's vertical coordinate measured relative to the home window's top-left corner

            code:

                import tkinter as tk

                window = tk.Tk()
                button_1 = tk.Button(window, text="Button #1")
                button_2 = tk.Button(window, text="Button #2")
                button_3 = tk.Button(window, text="Button #3")
                button_1.place(x=10, y=10)
                button_2.place(x=20, y=40)
                button_3.place(x=30, y=70)
                window.mainloop()

            code:

                import tkinter as tk

                window = tk.Tk()
                button_1 = tk.Button(window, text="Button #1")
                button_2 = tk.Button(window, text="Button #2")
                button_3 = tk.Button(window, text="Button #3")
                button_1.place(x=10, y=10, width=150)
                button_2.place(x=20, y=40)
                button_3.place(x=30, y=70, height=50)
                window.mainloop()

        grid:

            paramters: column, row, rowspan, columnspan
                column=c - deploys the widget in the column number c; note: the columns' numbers start from zero, and if you omit this argument, the manager will assume 0 (the left-most column)
                row=r - deploys the widget in the row number r; if you omit this argument, the manager will assume the first free row starting from the top
                columnspan=cs - determines how many neighboring columns the widget occupies; the parameter defaults to 1 (the widget won't cross a single grid's cell)
                rowspan=rs - works as columnspan but refers to rows
                
            code:
                
                import tkinter as tk

                window = tk.Tk()
                button_1 = tk.Button(window, text="Button #1")
                button_2 = tk.Button(window, text="Button #2")
                button_3 = tk.Button(window, text="Button #3")
                button_1.grid(row=0, column=0)
                button_2.grid(row=1, column=1)
                button_3.grid(row=2, column=2)
                window.mainloop()

            code:

                import tkinter as tk

                window = tk.Tk()
                button_1 = tk.Button(window, text="Button #1")
                button_2 = tk.Button(window, text="Button #2")
                button_3 = tk.Button(window, text="Button #3")
                button_1.grid(row=0, column=0)
                button_2.grid(row=1, column=1)
                button_3.grid(row=2, column=0, columnspan=2)
                window.mainloop()

        pack:

            parameters: (side: TOP, BOTTOM, LEFT, RIGHT), (fill: NONE, X, Y, BOTH)
                side=s - forces the manager to pack the widgets in a specified direction
                fill=f - suggests to the manager how to expand the widget if you want it to occupy more space than the default
                
            code:

                import tkinter as tk

                window = tk.Tk()
                button_1 = tk.Button(window, text="Button #1")
                button_2 = tk.Button(window, text="Button #2")
                button_3 = tk.Button(window, text="Button #3")
                button_1.pack()
                button_2.pack()
                button_3.pack()
                window.mainloop()

            code:

                import tkinter as tk

                window = tk.Tk()
                button_1 = tk.Button(window, text="Button #1")
                button_2 = tk.Button(window, text="Button #2")
                button_3 = tk.Button(window, text="Button #3")
                button_1.pack(side=tk.RIGHT)
                button_2.pack()
                button_3.pack()
                window.mainloop()

            code:

                import tkinter as tk

                window = tk.Tk()
                button_1 = tk.Button(window, text="Button #1")
                button_2 = tk.Button(window, text="Button #2")
                button_3 = tk.Button(window, text="Button #3")
                button_1.pack(side=tk.RIGHT, fill=tk.Y)
                button_2.pack()
                button_3.pack()
                window.mainloop()

7) Coloring widgets
        arguments: bg, fg, activeforeground, activebackground
            last 2 are for when the button is pressed and not yet released
                
        Hex codes
            #000000 is black
            #FFFFFF is white
            #FF0000 is red
            #00FF00 is green
            #0000FF is blue
            #00FFFF is turquoise
            #FF00FF is violet
            ...

        code:

            import tkinter as tk

            window = tk.Tk()
            button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
            button.pack()
            window.mainloop()

        code:

            import tkinter as tk

            window = tk.Tk()
            button = tk.Button(window, text="Button #1",
                            bg="MediumPurple",
                            fg="LightSalmon",
                            activeforeground="LavenderBlush",
                            activebackground="HotPink")
            button.pack()
            window.mainloop()

        code:

            import tkinter as tk

            window = tk.Tk()
            button = tk.Button(window, text="Button #1",
                            bg="#9370DB",
                            fg="#FFA07A",
                            activeforeground="#FFF0F5",
                            activebackground="#FF69B4")
            button.pack()
            window.mainloop()

8) A GUI application from scratch
        1) construct a window and launch an event controller

            code:

                import tkinter as tk

                window = tk.Tk()
                window.mainloop()

        2) Label()
            a non-clickable widget able to present short textual information, passed to the widget's constructor using a text argument
        
            code:

                    import tkinter as tk

                    window = tk.Tk()

                    label = tk.Label(window, text = "Little label:")
                    label.pack()

                    window.mainloop()

        3) Frame()
            a non-clickable component used to group widgets and to separate them (visually) from other window components
                
            code:

                import tkinter as tk

                window = tk.Tk()

                label = tk.Label(window, text="Little label:")
                label.pack()

                frame = tk.Frame(window, height=30, width=100, bg="#000099")
                frame.pack()

                window.mainloop()

        4) Button()

            code:

                import tkinter as tk

                window = tk.Tk()

                label = tk.Label(window, text="Little label:")
                label.pack()

                frame = tk.Frame(window, height=30, width=100, bg="#000099")
                frame.pack()

                button = tk.Button(window, text="Button")
                button.pack(fill=tk.X)

                window.mainloop()

        5) IntVar() & set()
            create an object of the class `IntVar` and use the class method `set` to store an integer value
        
            code:

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

        6) Checkbutton()
            
                
                
                
                
                
                
                
                
                
                
                
                
7) 

"""