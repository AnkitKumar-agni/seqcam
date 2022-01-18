from tkinter import*
from PIL import Image, ImageTk
from record import record


window = Tk()
window.title("SEQCAM")
window.iconphoto(False, PhotoImage(file="cam1.png"))
window.geometry('1080x720')

mainFrame = Frame(window, bd=2)

labelTitle = Label(mainFrame, text='Security Camera', font=("garamond", 40, "bold"))
labelTitle.grid(pady=(10, 10), column=1)

#Button Record
btn_img = Image.open("icon1.png")
btn_img = btn_img.resize((50, 50), Image.ANTIALIAS)
btn_img = ImageTk.PhotoImage(btn_img)

btn = Button(mainFrame, text="Video Recording", font=("helvitica", 20, "bold"), height=90, width=270, fg="green", image=btn_img, compound="left", command=record)
btn.grid(row=2, pady=(20, 10), column=1)



#Button Exit
btn_img2 = Image.open("icon2.png")
btn_img2 = btn_img2.resize((50, 50), Image.ANTIALIAS)
btn_img2 = ImageTk.PhotoImage(btn_img2)

btn_exit = Button(mainFrame, text="Exit", font=("helvitica", 20, "bold"), height=90, width=270, fg="red", image=btn_img, compound="left", command=window.quit)
btn_exit.grid(row=4, pady=(20, 10), column=1)



mainFrame.pack()

window.mainloop()
