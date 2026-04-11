from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def handle_login():
    email = email_input.get()
    password= password_input.get()
    
    if email=='xyz@gmail.com' and password=='12345':
        messagebox.showinfo('success','Login Successfull')
    else:
        messagebox.showerror("Error","Login Failed")


root = Tk()

root.title('Login Form')

# root.iconbitman()

root.minsize(300,300)
root.maxsize(600,600)
root.geometry('350x500')
root.configure(background='#047BD5')


img = Image.open("basics/flipcart-logo.png")
resized_img = img.resize((100,100))
img = ImageTk.PhotoImage(resized_img)
img_lable = Label(root, image=img)
img_lable.pack(pady=(10,10))


text_label = Label(root, text='Flipkart', fg='white', bg='#047BD5')
text_label.pack()
text_label.config(font=('verdana',24))

email_label = Label(root,text='Enter Email', fg='white', bg='#047BD5')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root, width=50)
email_input.pack(ipady=4, pady=(1,15))


password_label = Label(root,text='Enter password', fg='white', bg='#047BD5')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root, width=50)
password_input.pack(ipady=4, pady=(1,15))


login_btn = Button(root, text='Login Here', bg='white', fg='black', width=12, height=1, command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdaan',10))





root.mainloop()
