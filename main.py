from Tkinter_MiniWorkEnvironment.src.GUI import GUI

if __name__ == "__main__":
    # initialize
    gui = GUI()

    # build the surface
    gui.display_time(1, 0, 0)
    gui.add_entry(40, 5, "dotbox", "#031a40", "white", 1, 0)

    # keep the window going
    gui.mainloop()
