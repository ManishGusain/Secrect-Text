from tkinter import *
import pyperclip

root = Tk()
root.title("Secret Text")
root.geometry('370x400+400+100')
root.configure(bg='blue')

def encrypt_window():
    # message encryption function
    def encryption():
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        text_input = mssg_box.get("1.0",END)
        shifts = 3
        encrypt_mssg = ''
        for i in range(len(text_input)):
            if text_input[i] not in alphabets:
                encrypt_mssg += text_input[i]
            for j in range(len(alphabets)):
                if text_input[i] in alphabets[j]:
                    #cipher_text = (plain_text+shift)%26
                    encrypt_mssg+=alphabets[(j + shifts)% 26]
        mssg_done_box.insert('1.0', encrypt_mssg)
        return encrypt_mssg

    def copy_btn():
        x = mssg_done_box.get('1.0', END)
        pyperclip.copy(x) #copies the encrypted text to clipboard

    encrypt_newWindow = Toplevel(root)
    encrypt_newWindow.title("Secret Text")
    encrypt_newWindow.geometry('370x600+400+100')
    encrypt_newWindow.configure(bg='blue')

    encrypt_heading = Label(encrypt_newWindow, text="ENCRYPT TEXT", font=("Arial Bold", 30))
    encrypt_heading.place(x=40, y=2)

    mssg_label = Label(encrypt_newWindow, text="Enter your message below:", font=("Arial", 14))
    mssg_label.place(x=10, y=100)

    mssg_box = Text(encrypt_newWindow, height = 10, width = 43)
    mssg_box.place(x=12, y=155)

    encrypt_mssg_btn = Button(encrypt_newWindow, text="ENCRYPT MESSAGE", font=("Arial", 12), command=encryption)
    encrypt_mssg_btn.place(x=100, y=350)

    mssg_done_box = Text(encrypt_newWindow, height=0, borderwidth=0, font=("Arial", 14), bg='blue')
    mssg_done_box.place(x=10, y=410)
    mssg_done_box.bind("<Key>", lambda e: "break")  #it makes the text field read-only

    copy_btn = Button(encrypt_newWindow, text="COPY ENCRYPTED MESSAGE", font=("Arial", 12), command=copy_btn)
    copy_btn.place(x=120, y=470)

def decrypt_window():
    #message decryption function
    def decryption():
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        d_text = mssg_decrypt_box.get("1.0", END)
        shifts = 3
        decrypt_mssg = ''
        for i in range(len(d_text)):
            if d_text[i] not in alphabets:
                decrypt_mssg += d_text[i]
            for j in range(len(alphabets)):
                if d_text[i] in alphabets[j]:
                    # encrypt_text = (excrypted_text-shift)mod26
                    decrypt_mssg += alphabets[(j - shifts) % 26]
        mssgdecrypt_done_box.insert('1.0', decrypt_mssg)
        return decrypt_mssg

    def paste_text():
        y = pyperclip.paste()
        mssg_decrypt_box.insert('1.0', y)

    decrypt_newWindow = Toplevel(root)
    decrypt_newWindow.title("Secret Text")
    decrypt_newWindow.geometry('370x600+400+100')
    decrypt_newWindow.configure(bg='blue')

    decrypt_heading = Label(decrypt_newWindow, text="DECRYPT TEXT", font=("Arial Bold", 30))
    decrypt_heading.place(x=40, y=2)

    mssg_label_decrypt = Label(decrypt_newWindow, text="Enter message to decrypt below:", font=("Arial", 14))
    mssg_label_decrypt.place(x=10, y=100)

    mssg_decrypt_box = Text(decrypt_newWindow, height=10, width=43)
    mssg_decrypt_box.place(x=12, y=155)

    decrypt_mssg_btn = Button(decrypt_newWindow, text="DECRYPT MESSAGE", font=("Arial", 12), command= decryption)
    decrypt_mssg_btn.place(x=170, y=350)

    paste_btn = Button(decrypt_newWindow, text="PASTE", font=("Arial", 12), command=paste_text)
    paste_btn.place(x=90, y=350)

    mssgdecrypt_done_box = Text(decrypt_newWindow, height=0, borderwidth=0, font=("Arial", 14), bg='blue')
    mssgdecrypt_done_box.place(x=10, y=410)
    mssgdecrypt_done_box.bind("<Key>", lambda e: "break")  #it makes the text field read-only

heading = Label(root, text="SECRET TEXT", font=("Arial Bold", 30))
heading.place(x=40, y=2)

what = Label(root, text="What you want to do:", font=("Arial", 18))
what.place(x=10, y=100)

encrypt_btn = Button(root, text="ENCRYPTION", font=("Arial", 18), command= encrypt_window)
encrypt_btn.place(x=100, y=155)

decrypt_btn = Button(root, text="DECRYPTION", font=("Arial", 18), command= decrypt_window)
decrypt_btn.place(x=100, y=230)

cpyrght = Label(root, text="copyright @ MG TECH", font=("Arial", 10))
cpyrght.place(x=10, y=370)

root.mainloop()