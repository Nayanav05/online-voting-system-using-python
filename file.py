from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import Button
import webbrowser

gui = Tk()
gui.geometry("1920x1080")
gui.config(background="white")
gui.title("Online Voting System")
lbl = Label(gui, text="VOTER ID PROJECT", font=("times", 30, "bold"), bg="white")
lbl.place(x=200, y=350)
voter_id = ["1", "2", "3","4","5","6","7","8"]
voted = []
num_of_voters = (len(voter_id))
password =["2022"]


def voterID():
    entry_value = entry.get()
    if entry_value in voter_id:
        messagebox.showinfo("voter ID", f" Voter ID {entry_value} is Valid")
        lbl["text"] = f" Voter ID {entry_value} is Valid"
        Nominee_1["stat"] = "normal"
        Nominee_2["stat"] = "normal"
        if entry_value in voted:
            lbl["text"] = f" Voter ID {entry_value} is Valid"
            messagebox.showinfo("error", f"{entry_value} already voted")
            Nominee_1["stat"] = "disabled"
            Nominee_2["stat"] = "disabled"
        else:
            voted.append(entry_value)


scoreA = 0
scoreB = 0


def Nominee1():
    global scoreA
    scoreA += 1
    Nominee_1["stat"] = "disabled"
    Nominee_2["stat"] = "disabled"


def Nominee2():
    global scoreB
    scoreB += 1
    Nominee_1["stat"] = "disabled"
    Nominee_2["stat"] = "disabled"


def results():
        entry_value = value.get()
        if entry_value in password:
            messagebox.showinfo("login", f" password {entry_value} is Valid")
            #password_lbl["text"] = f" password {entry_value} is Valid"
            if scoreA > scoreB:
                percent = (scoreA / num_of_voters) * 100
                result_lbl_A["text"] = f"Nominee_1 Has Won The Voting with", percent, "% of Votes"
                score_lbl_A["text"] = f"Nominee1 is: {scoreA}"
                score_lbl_B["text"] = f"Nominee2 is: {scoreB}"
            else:
                percent = (scoreB / num_of_voters) * 100
                result_lbl_B["text"] = "Nominee_2 Has Won The Voting with", percent, " % of Votes"
                score_lbl_A["text"] = f"Nominee1 is: {scoreA}"
                score_lbl_B["text"] = f"Nominee2 is: {scoreB}"
        else:
            messagebox.showinfo("login", f" password {entry_value} is InValid")
            password_lbl["text"] = f" password {entry_value} is InValid"

entry = Entry(gui, bg="white", font=("arial", 20, "bold"))
entry.place(x=150, y=450)
voterID_btn = Button(gui, text="Voter ID", bg="blue", fg="white", font=("times", 20, "bold"), command=voterID)
voterID_btn.place(x=250, y=500)
lbl = Label(gui, text="", fg="black", bg="white", font=("arial", 15, "bold"))
lbl.place(x=200, y=550)
Nominee_1 = Button(gui, text="NOMINEE1", stat="disabled", relief=RIDGE, font=("times", 20, "bold"), bg="blue",
                   fg="white", command=Nominee1)
Nominee_1.place(x=150, y=600)
Nominee_2 = Button(gui, text="NOMINEE2", stat="disabled", relief=RIDGE, font=("times", 20, "bold"), bg="blue",
                   fg="white", command=Nominee2)
Nominee_2.place(x=350, y=600)
score_lbl_A = Label(gui, text="", font=("times", 20), bg="white", fg="black")
score_lbl_A.place(x=150, y=700)
score_lbl_B = Label(gui, text="", font=("times", 20), bg="white", fg="black")
score_lbl_B.place(x=350, y=700)
Result = Button(gui, text="result", font=("", 20, "bold"), command=results, bg="blue", fg="white")
Result.place(x=650, y=550)
result_lbl_A = Label(gui, text="", font=("times", 20), bg="white", fg="black")
result_lbl_A.place(x=550, y=600)
result_lbl_B = Label(gui, text="", font=("times", 20), bg="white", fg="black")
result_lbl_B.place(x=550, y=600)
value = Entry(gui, bg="white", font=("arial", 20, "bold"))
value.place(x=550, y=500)
password_lbl=Label(gui, text="", font=("times", 20), bg="white", fg="black")
password_lbl.place(x=350, y=900)
abc = Label(gui, text="Guided by:", font=("times", 20), bg="white", fg="black")
abc.place(x=1100, y=250)
nay = Label(gui, text="Nayana V", font=("times", 20), bg="white", fg="black")
nay.place(x=300, y=250)
asf = Label(gui, text="Asfiya ", font=("times", 20), bg="white", fg="black")
asf.place(x=500, y=250)
gag = Label(gui, text="Gagan B S", font=("times", 20), bg="white", fg="black")
gag.place(x=700, y=250)
gagp = Label(gui, text="Gagan P K", font=("times", 20), bg="white", fg="black")
gagp.place(x=900, y=250)
guide = Label(gui, text="Mr. Niranjan Murthy C\nAssistant Professor", font=("times", 20), bg="white", fg="black")
guide.place(x=1250, y=600)
mem = Label(gui, text="Group Members:", font=("times", 20), bg="white", fg="black")
mem.place(x=50, y=95)
def photo1p():
    webbrowser.open_new("C:/Users/Nayana V Jannu/Documents/nayanap1[1].pdf")
photo1 = PhotoImage(file="C:/Users/Nayana V Jannu/Pictures/Saved Pictures/jannu.png")
P1 = Button(gui, text="photo", image=photo1 ,command=photo1p).place(x=300, y=80)
def photo2p():
    webbrowser.open_new("C:/Users/Nayana V Jannu/Documents/asfiyap1[2].pdf")
photo2 = PhotoImage(file="C:/Users/Nayana V Jannu/Pictures/Saved Pictures/asfi.png")
p2 = Button(gui, text="photo", image=photo2 ,command=photo2p).place(x=500, y=80)
def photo3p():
    webbrowser.open_new("C:/Users/Nayana V Jannu/Documents/bsp1[1].pdf")
photo3= PhotoImage(file="C:/Users/Nayana V Jannu/Pictures/Saved Pictures/bs.png")
p3 = Button(gui, text="photo", image=photo3,command=photo3p).place(x=700, y=70)
def photo4p():
    webbrowser.open_new("C:/Users/Nayana V Jannu/Documents/pkp1.pdf")
photo4= PhotoImage(file="C:/Users/Nayana V Jannu/Pictures/Saved Pictures/gaganp.png")
p4 = Button(gui, text="photo", image=photo4,command=photo4p).place(x=900, y=80)
def collegep():
    webbrowser.open_new("http://www.gmit.ac.in/")
college = PhotoImage(file="C:/Users/Nayana V Jannu/Pictures/Saved Pictures/college.png")
college1 = Button(gui, text="college", image=college,command=collegep).place(x=450, y=0)
sir = PhotoImage(file="C:/Users/Nayana V Jannu/Pictures/Saved Pictures/sir (2).png")
sirlbl = Label(gui,text="",image=sir)
sirlbl.place(x=1250,y=250)
logo=PhotoImage(file="C:/Users/Nayana V Jannu/Pictures/Saved Pictures/gmlogo1.png")
logolbl = Label(gui,image=logo)
logolbl.place(x=0,y=0)
gui.mainloop()
