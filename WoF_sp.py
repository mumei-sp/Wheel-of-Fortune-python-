def clicked(alphabet):
    global amount
    amount = amounts[randint(0,(len(amounts) - 1))]
    global total
    txt="Spinning";
    label1.configure(text=txt)
    chance=amounts.index(amount)
    image_paths=['BankRupt.jpg','350.jpg','400.jpg','450.jpg','500.jpg','550.jpg','700.jpg','800.jpg','900.jpg','5000.jpg']
    img = Image.open(image_paths[chance])
    img = img.resize((300, 300), Image.ANTIALIAS)
    img= ImageTk.PhotoImage(img)
    panel = Label(window, image = img)
    panel.grid(column=11, row=10)
    answer= s;
    if amount=="BankRupt":
        total=0
        txt="BankRypt!!  u r UnFortunate";
        label1.configure(text=txt)
        image = Image.open("BankRupt.jpg")
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
    elif alphabet in vowels:
        image = Image.open(image_paths[chance])
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        if total >= 250:
            total-=250
            g=s.count(alphabet)
            if g>1:
                l=list(s)
                z=[x for x,y in enumerate(l) if y==alphabet]
                for i in z:
                    globals()["b0%s" %i]["text"]=alphabet
                
            for i in range(len(answer)):
                if alphabet ==s[i]:
                    globals()["b0%s" %i]["text"]=alphabet
                    total+=amount
                    txt="u gOT  $"+str(amount*g);
                    label1.configure(text=txt,bg="white")
                    xt="Total = $"+str(total);
                    label2.configure(text=xt,fg="white",bg="Black",font = "Helvetica 16 bold italic")
                    break
            else:
                txt="u lost chance of winning!!: $"+str(amount);
                label1.configure(text=txt)
                messagebox.showinfo("Not in Word!!!")
        else:
            txt='Not enough money';
            label1.configure(text=txt)
    else:
        g=s.count(alphabet)
        image = Image.open(image_paths[chance])
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        if g>1:
                l=list(s)
                z=[x for x,y in enumerate(l) if y==alphabet]
                for i in z:
                    globals()["b0%s" %i]["text"]=alphabet
                
        for i in range(len(answer)):
            if alphabet ==s[i]:
                globals()["b0%s" %i]["text"]=alphabet
                total+=amount
                txt="u gOT  $"+str(amount*g);
                label1.configure(text=txt,bg="white")
                xt="Total = $"+str(total);
                label2.configure(text=xt,fg="white",bg="Black",font = "Helvetica 16 bold italic")
                break
        else:
            txt="u lost chance of winning!! : $"+str(amount);
            label1.configure(text=txt)
            messagebox.showinfo("Not in Word!!!")    
    if (all([globals()["b0%s" %j]["text"]==s[j] for j in range(len(s))])):
        messagebox.showinfo("congratulations", "U R Fortunate!!!!\n You have: $" + str(total))
        window.destroy()
        
print('Guess one letter at a time. If you want to buy a vowel, you must have at least $250, otherwise, you cannot buy a vowel.\nIf spin stops at "Bankrupt",the player losses all the money ')
print("Solve the puzzle!!\nHave Fun")
import time
from random import randint
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
amounts = ["BankRupt",350,400,450,500,550,700,800,900,5000]
total=0
categories = {'color': ['red', 'green' ,'blue','yellow','turqouise','purple','indigo','white','black'], "Animal":["cat","dog","Tiger","Lion"]}
category = randint(0, (len(categories) - 1))
xx='Category:', list(categories.keys())[category]
word_wof=randint(0,len(categories["color"])-1)
kk=list(categories.keys())[category]
s=categories[kk][word_wof].upper()
vowels = ['A', 'E', 'I', 'O', 'U']
window = Tk()
window.title("WHEEL OF FORTUNE  #WOF...")
window.geometry("950x700")
answer_arr=[]
for b in range(len(s)):
    globals()["b0%s" %b]=Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
    globals()["b0%s" %b].grid(column=b+2, row=0)
label2=Label(window,text="Total = $0",fg="white",bg="Black",font = "Helvetica 16 bold italic")
label2.grid(row=40,column=0)
label3=Label(window,text=xx,font = "Helvetica 16 bold italic")
label3.grid(row=200,column=0)
img = Image.open('ini.jpg')
img = img.resize((300, 300), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.grid(column=11, row=10)
    
a1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
a1.grid(column=1, row=1)
a2 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
a2.grid(column=2, row=1)
a3 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
a3.grid(column=3, row=1)
a4 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
a4.grid(column=4, row=1)
a5 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
a5.grid(column=5, row=1)
a6 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
a6.grid(column=6, row=1)
a7 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
a7.grid(column=7, row=1)
a8 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
a8.grid(column=8, row=1)
a9 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
a9.grid(column=9, row=1)
a10 = Button(window, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
a10.grid(column=3, row=2)
a11= Button(window, text="K",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
a11.grid(column=4, row=2)
a12 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
a12.grid(column=5, row=2)
a13 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
a13.grid(column=6, row=2)
a14 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
a14.grid(column=7, row=2)
a15= Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
a15.grid(column=1, row=3)
a16 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
a16.grid(column=2, row=3)
a17 = Button(window, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
a17.grid(column=3, row=3)
a18 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
a18.grid(column=4, row=3)
a19 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
a19.grid(column=5, row=3)
a20 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
a20.grid(column=6, row=3)
a21= Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
a21.grid(column=7, row=3)
a22 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
a22.grid(column=8, row=3)
a23 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
a23.grid(column=9, row=3)
a24 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
a24.grid(column=4, row=5)
a25 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
a25.grid(column=5, row=5)
a26= Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
a26.grid(column=6, row=5)
label1=Label(window,text="Spinning...",fg = "red",font = "Times 12 italic")
label1.grid(row=20,column=0)
window.mainloop()

        
        
        
