import tkinter as tk
#we work in file explorer so we import this
from tkinter import filedialog
import os
class ImageToPDFConverter:
    def __init__(self,root):#Analizing root
        self.root = root
        #varaible for image
        self.image_path = []#we are going to convert multiple image into pdf so its empty
        self.output_pdf_name= tk.StringVar# we donot know the name so just for abit we give this name
        self.selected_images_listbox = tk.Listbox(root,selectmode=tk.MULTIPLE)#we need to convert multiple item so we did this
        self.initialize_ui()
def initialize_ui(self):
    title_label = tk.Label(self.root,text="Image to PDF Converter", font=("Helvetice",16,"bold"))#Giving the font,and other stuff
    title_label.pack(pady=10)
def main():
    root = tk.Tk()
