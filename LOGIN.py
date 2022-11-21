from tkinter import*
from tkinter import messagebox
class Login:
    def __init__(self, root): 
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

        #Background Image
        self.bg=PhotoImage(file="C:\\Users\\DELL\\Desktop\\Carmeganda\\Carmeganda\\1.png")#photo file path
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #Login Frame
        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=400)

        #Title & Subtitle
        title= Label(Frame_login, text="WELCOME", font=("Impact", 35, "bold"), fg="#246669", bg="white").place(x=150,y=20)
        subtitle= Label(Frame_login, text="Login your Account", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=10,y=100)
        
        #Username
        lbl_user= Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=10,y=140)
        self.username = Entry(Frame_login, font=("Goudy old style",15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)

        #Password
        lbl_password= Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=10,y=210)
        self.password = Entry(Frame_login, font=("Goudy old style",15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        #Button
        forget= Button(Frame_login, text="Forget Password?",bd=0, cursor="hand2", font=("Goudy old style", 12, "bold"), fg="#616277", bg="white").place(x=165,y=288)
        submit= Button(Frame_login,command=self.check_function, cursor="hand2", text="Login?", font=("Goudy old style", 15, "bold"), bg="#246669", fg="white").place(x=150,y=328, width=180, height=40)
        
        # Creating Checkbox
    def check_function(self):
         if self.username.get()=="" or self.password.get()== "":
                messagebox.showerror("Error", "All fields are required",parent=self.root)
         elif self.username.get() !="luna12tech" or self.password.get() !="072103":
                messagebox.showerror("Error", "Invalid Username or Password",parent=self.root)
         else:
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")          

root = Tk()
object=Login(root)
root.mainloop()

