
import tkinter as tk
from tkinter import filedialog
import os

## Creamos una clase para la ventana interactiva
class WindowTK():
    def __init__(self):
        # Creating the tkinter Window
        self.root = tk.Tk()
        self.root.title("Transformación Archivos Activo Histórico")
        self.root.geometry("800x300")
        self.root.config(bg="dark gray")
        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_columnconfigure(0, weight = 1)

        self.current_dir = os.getcwd()
        
        # Variables
        self.filespath = None
        self.savepath = None

        # Label to display selected path
        self.show_pathfile = tk.Label(self.root, text="Path: ")
        self.show_pathsave = tk.Label(self.root, text="Path: ")

        # Buttons
        pathfile_b = tk.Button(self.root, text = 'Ruta Archivo', command = self.set_file)
        pathsave_b = tk.Button(self.root, text = 'Ruta Guardado', command = self.set_save)
        
        exit_button = tk.Button(self.root, text="Guardar y Salir", command=self.salir)
        

        pathfile_b.place(x = 30, y = 150)
        self.show_pathfile.place(x = 140, y = 150)

        pathsave_b.place(x = 30, y = 195)
        self.show_pathsave.place(x = 140, y = 195)


        exit_button.place(x = 350, y = 250)

        #Call Loop
        self.root.mainloop()

    def salir(self):
        self.root.destroy()
    
    # Files Folder
    # Set Path
    def set_file(self):
        self.filespath = filedialog.askopenfilename(initialdir=self.current_dir,
                                                    title="Select a PDF file",
                                                    filetypes=[("PDF files", "*.pdf")])
        
        self.show_pathfile.config(text="Path: " + self.filespath)

    def set_save(self):
        self.savepath = filedialog.askdirectory(initialdir=self.current_dir,
                                                        title = 'Set a path to save the output')
        self.show_pathsave.config(text="Path: " + self.savepath)

    # Getters
    def get_file(self):
        return self.filespath
    def get_save(self):
        return self.savepath