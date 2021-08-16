import tkinter
from gps import program

root = tkinter.Tk()
root.geometry('356x290')
root.title('WebGPS')
root.iconbitmap('img\icon.ico')
root['background'] = '#2c2f33'
root.resizable(False, False)

# images
websites = tkinter.PhotoImage(file="img/websites.png")
login = tkinter.PhotoImage(file="img/login.png")

youtube = tkinter.PhotoImage(file="img/youtube.png")
discord = tkinter.PhotoImage(file="img/discord.png")
facebook = tkinter.PhotoImage(file="img/facebook.png")
duck = tkinter.PhotoImage(file="img/duck.png")
password = tkinter.PhotoImage(file="img/password.png")


tkinter.Label(root, text='WEBSITES', font=('Bahnschrift Bold', 40), bg='#2c2f33').place(x=53, y=20)

tkinter.Button(root, image=youtube, bd=0, bg='#2c2f33', activebackground='#2c2f33', command=lambda: program.open_website('youtube')).place(x=20, y=110)
tkinter.Button(root, image=discord, bd=0, bg='#2c2f33', activebackground='#2c2f33', command=lambda: program.open_website('discord')).place(x=104, y=110)
tkinter.Button(root, image=facebook, bd=0, bg='#2c2f33', activebackground='#2c2f33', command=lambda: program.open_website('facebook')).place(x=188, y=110)
tkinter.Button(root, image=duck, bd=0, bg='#2c2f33', activebackground='#2c2f33', command=lambda: program.open_website('browser')).place(x=272, y=110)

tkinter.Label(root, text='LOGIN  >', font=('Bahnschrift Bold', 40), bg='#2c2f33').place(x=40, y=195)
tkinter.Button(root, image=password, bd=0, bg='#2c2f33', activebackground='#2c2f33', command=program.login).place(x=272, y=200)

root.mainloop()
