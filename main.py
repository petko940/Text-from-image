from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
from pytesseract import pytesseract

root = Tk()
root.geometry("700x550+500+200")
root.title("Text from image")
path_to_image = ""


def select_image():
    global path_to_image
    try:
        filename = askopenfilename(title='Open a picture',)
        path_to_image = filename
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        print(text, sep="\n")
        text_box.insert("end", text)

        def clear():
            text_box.delete('1.0', END)
            select_copy = Button(root, background="#6B8E23", foreground="white", text="Select and copy", font=10,
                                 width=20,
                                 height=2,
                                 command=lambda: select_and_copy())
            select_copy.place(x=410, y=10)

        button_clear = Button(root, background="#8f0000", foreground="#FFFFFF", text="Clear text", font=(10), width=20,
                              height=2, command=clear)
        button_clear.place(x=210, y=10)
        text_box.focus()

        def select_and_copy():
            text_box.tag_add("", "1.0", "end")
            text_box.tag_config("", foreground="white", background="blue")
            text_box.clipboard_append(text)
            text_box.update()
            select_copy = Button(root, background="#6B8E23", foreground="white", text="Clipboard updated", font=10,
                                 width=20,
                                 height=2,
                                 command=lambda: select_and_copy())
            select_copy.place(x=410, y=10)
            select_copy["state"] = DISABLED
            select_copy.config(disabledforeground="white", )

            def on_click(event):
                text_box.tag_add("", "1.0", "end")
                text_box.tag_config("", foreground="black", background="#C0C0C0")
                text_box.update()

            root.bind('<Button-1>', on_click)

        select_copy = Button(root, background="#6B8E23", foreground="white", text="Select and copy", font=10, width=20,
                             height=2,
                             command=lambda: select_and_copy())
        select_copy.place(x=410, y=10)


    except:
        pass


scroll = Scrollbar(root, orient='vertical')
scroll.pack(side=RIGHT, fill='y')

text_box = Text(root, background="#C0C0C0", font=("Georgia, 14"), yscrollcommand=scroll.set)
text_box.pack(padx=10, pady=65)

button = Button(root, background="#B0E0E6", text="Select Image", font=(10), width=20, height=2, command=select_image)
button.place(x=10, y=10)

scroll.config(command=text_box.yview)


root.mainloop()
