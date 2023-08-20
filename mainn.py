from tkinter import *
from csv import *
import reg
import loginscreen
import allocation
import report
from PIL import ImageTk, Image



class mainscr:
 
    def screen(self):
        self.mainscreen = Tk()
        self.mainscreen.geometry('500x500')
        self.mainscreen.resizable(0, 0)
        self.mainscreen.title("MAIN")
        
        bg_frame = Image.open(r'C:\Users\Padhmapriya\Downloads\project\project\oops.jpeg')
        bg_photo = ImageTk.PhotoImage(bg_frame)
        self.bg_panel = Label(self.mainscreen, image=bg_photo)
        self.bg_panel.image = bg_photo
        self.bg_panel.place(width=500, height=500)
        #img1 = ImageTk.PhotoImage(Image.open("/Users/mac/Downloads/ssn laundry.jpeg"))
        #labelssn = Label(mainscreen, image = img1)
        #labelssn.pack()
        def registrationscr():
            self.mainscreen.destroy()
            rs=reg.registerscrn()
            rs.register()
            
        def lgscr():
            self.mainscreen.destroy()
            rs=loginscreen.login_screen()
            rs.login()
            
        def allocationscreen():
            a=allocation.Allocation()
            a.allocate()

        def reportscreen():
            r=report.Report()
            r.reportt()
            
        self.registerbutton= Button(self.mainscreen, text='REGISTER', font=("gotham", 16, "bold"), width=10,height=1, bd=0,fg='red',bg='black',highlightbackground="black",command=registrationscr)
        self.registerbutton.place(x=57,y=272)

        self.loginbutton= Button(self.mainscreen, text='ORDER', font=("gotham", 16, "bold"), width=10,height=1, bd=0,fg='red',bg='black',command=lgscr)
        self.loginbutton.place(x=290,y=272)

        self.servicepointbutton= Button(self.mainscreen, text='SERVICE POINT', font=("gotham", 16, "bold"), width=12,height=1, bd=0,fg='red',bg='black',command=allocationscreen)
        self.servicepointbutton.place(x=45,y=370)

        self.reportbutton= Button(self.mainscreen, text='REPORT', font=("gotham", 16, "bold"), width=10,height=1, bd=0,fg='red',bg='black',command=reportscreen)
        self.reportbutton.place(x=290,y=370)

        self.mainscreen.mainloop()
        '''self.orderbutton= Button(self.mainscreen, text='ORDER', font=("gotham", 16, "bold"), width=22,height=2, bd=0,fg='red',bg='black')
        self.orderbutton.place(x=120,y=300)'''
    

ms=mainscr()
ms.screen()
