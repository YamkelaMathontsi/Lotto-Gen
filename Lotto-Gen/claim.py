from tkinter import *
from tkinter import messagebox
import tkinter

root = Tk()
root.title("images")
root.geometry("900x900")
root.config(bg="yellow")
photo = PhotoImage(file="bottom img.png")
pic_label = Label(root, image=photo)
pic_label.place(x=10, y=10)


def clear_text():
    Account_holder.delete(0, END)
    email.delete(0, END)
def destroy():
    msg_box = messagebox.askquestion("Closing Programing, Are You Sure")
    root.destroy()



# heading labels
bank = Label(root, text="")
bank.place()
claim = Label(root, text="")
claim.place()






# bank_type = "Select Bank: "
# bank_type = tkinter.StringVar(value=stock_txt)
# menu = OptionMenu(root, stock_var, "Capitec", "Standard Bank", "First National Bank", "ABSA", "BidVest", "Nedbank")
# # menu.config(bg="#212529", fg="#f0e68c", font=("Ariel", 15))
# menu.place(x=410, y=200)


# Labels

Account_holder = Label(root, text="Account holder:")
Account_holder.place(x=20, y=250)
email = Label(root, text="Account Type:")
email.place(x=20, y=300)
Bank = Label(root, text="Bank:")
Bank.place(x=20, y=350)

# id_num = Label(root, text="ID Number")
# id_num.place(x=20, y=350)

#Entries

Account_holder = Entry(root, text="")
Account_holder.place(x=130, y=250)
email = Entry(root, text="")
email.place(x=130, y=300)
# id_num = Entry(root, text="")
# id_num.place(x=130, y=350)


# def user_pass_search():
#
#     user_pass = {'Jayden': 'jaydenmay', 'Brent Lee': 'yourstepbro', 'Jason': 'faketaxi@17',
#              'Yamkela': '@merclife'}
#
#     if name.get() in user_pass:
#         if email.get() == user_pass[name.get()]:
#             root.destroy()
#             # import newwindow
#         else:
#             messagebox.showerror(message="Username and password does not match")
#     else:
#         messagebox.showerror(message="Username does not exist")

# verify = Button(root, text='Verify', bg="pink", command=user_pass_search )
# verify.place(x=20, y=400)
clear_btn = Button(root, text='Clear', bg="pink", command=clear_text)
exit = Button(root, text='Exit', bg="pink", command=destroy)
exit.place(x=220, y=400)
clear_btn.place(x=120, y=400)
submit = Button(root, text='submit', bg="pink",)
submit.place(x=220, y=450)



root.mainloop()



# numbers1 = [int(box.get()), int(box2.get()), int(box3.get()), int(box4.get()), int(box5.get()), int(box6.get())]
#     numbers2 = draw
#     comp = (set(numbers1).intersection(numbers2))
#     results = len(comp)
#     messagebox.showinfo("!!!! WINNINGS !!!!", "You Got " + str(results) + " Winning Balls")
#
#     if results <= 1:
#         playsound("alert.mp3")
#         messagebox.showinfo("Unlucky", "You Have Won R0.00")
#     elif results == 2:
#         messagebox.showinfo("LUCKY", "You Have Won R20.00")
#     elif results == 3:
#         messagebox.showinfo("LUCKY", "You Have Won R100.50")
#     elif results == 4:
#         messagebox.showinfo("LUCKY", "You Have Won R2384.00")
#     elif results == 5:
#         messagebox.showinfo("LUCKY", "You Have Won R8584.00")
#     else:
#         playsound("winner.mp3")
#         messagebox.showinfo("!!!! JACKPOT !!!!", "YOU HAVE WON THE JACKPOT")
