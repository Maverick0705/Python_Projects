import customtkinter
from PIL import Image
from tkinter import filedialog
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Users\Ritesh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

app = customtkinter.CTk()
app.geometry('600x450')
app.title("Text Extaction from image")
app.maxsize(600,450)

#function for opening image
def openImage():
    progressbar.set(0)
    progress_txt.configure(text = '0%')
    
    filename = filedialog.askopenfilename(filetypes = [('png files', '*.png')])
    img1 = Image.open(filename)
    get_txt = tess.image_to_string(img1)
    
    progressbar.start()
    progressbar.set(1)
    
    txt_box.insert('0.0', get_txt) #at line 0 and character 0
    app.title(filename)
    
    progress_txt.configure(text = '100%')
    progressbar.stop()

#creating frame
frame = customtkinter.CTkFrame(app,corner_radius =20,border_color = '#2596be', border_width = 2)
frame.pack(padx = 20, pady = 20, fill = 'both')

#add text
txt = customtkinter.CTkLabel(frame, text = "Extract Text from Image", font = ('Arial', 20))
txt.pack(pady=10)


#add btn
btn = customtkinter.CTkButton(frame, text= 'Add Image',text_color = '#FFFFFF',corner_radius = 8,
                              width =200,height = 30,font = ('Arial',20),border_spacing = 10,
                              command = openImage, hover_color = '#900C3F')
btn.pack(padx = 20, pady = 20)

#add Progressbar
progressbar = customtkinter.CTkProgressBar(frame, progress_color = '#900C3F')
progressbar.pack(pady = 20)
progressbar.set(0)

#add text to progressbar
progress_txt = customtkinter.CTkLabel(frame, text="0%")
progress_txt.place(x= 390, y = 144)

#add textbox
txt_box = customtkinter.CTkTextbox(frame, font = ('Arial' ,18),width = 500, height = 500,
corner_radius = 8)
txt_box.pack(pady = 20)



app.mainloop()
 
