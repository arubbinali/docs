# Course 1: GUI Programming

> ## Module 1

1) `Tk()` & `mainloop()`:
   - The main application window (which is often the only window being used by the application) is created by the tkinter method named `Tk()`.
   - To start the controller, you have to invoke the main window's method, named `mainloop()`.

   ```py
   import tkinter

   skylight = tkinter.Tk()
   skylight.mainloop()
