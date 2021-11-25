from Tkinter_MiniWorkEnvironment.src.GUI import GUI

if __name__ == "__main__":
    # initialize
    gui = GUI()

    # build the surface
    gui.add_label("Hello, it´s me!", 1, 0, 0)

    # keep the window going
    gui.mainloop()