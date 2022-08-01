from tkinter import *
from tkinter import messagebox
pg=Tk()
pg.title('FLAMES')
pg.iconbitmap('like2.ico')
pg.configure(bg='sky blue')
pg.geometry('540x450')

Label(pg,text='FLAMES',bg='sky blue',fg='black',font=('Forte 40 bold')).pack()



h1=StringVar()
h2=StringVar()

Label(pg,text=' ',bg='sky blue').pack()
Label(pg,text=' ',bg='sky blue').pack()

Label(pg,text='Player 1',bg='sky blue',font=('elephant 20 bold')).pack(anchor='sw')
p1=Entry(pg,textvariable=h1,bg='sky blue',font=('elephant 20 bold'))
p1.pack(anchor='se')
p1.focus()

Label(pg,text=' ',bg='sky blue',).pack()

Label(pg,text='Player 2',bg='sky blue',font=('elephant 20 bold')).pack(anchor='sw')
p2=Entry(pg,textvariable=h2,bg='sky blue',font=('elephant 20 bold'))
p2.pack(anchor='se')


def bm():
    n=h1.get()
    nm=h2.get()
    if ' ' in n :
        n=n.replace(' ','')
    else:
        n=n
    if ' ' in nm:
        nm=nm.replace(' ','')
    else:
        nm=nm





    n1=list(n)
    n2=list(nm)
    n3=[]

    ln1=len(n1)
    ln2=len(n2)

    if ln1>ln2:
        for i in range(ln2):
            if n2[0] in n1:
                n1.remove(n2[0])
                n2.remove(n2[0])
                continue

            else:
                p=n2[0]
                n3.append(p)
                n2.remove(p)

        nf=n1+n3

    else:
            for i in range(ln1):
                if n1[0] in n2:
                    n2.remove(n1[0])
                    n1.remove(n1[0])
                    continue

                else:
                    p=n1[0]
                    n3.append(p)
                    n1.remove(p)

            nf=n2+n3

    num=len(nf)
    f=['Friend','Lover','Affection','Marriage','Enemy','Sister',]
    fs=num*num


    while len(f) > 1 :
        val= (num % len(f) - 1)
        if val >= 0 :
            right = f[val + 1 : ]
            left = f[ : val]
            f = right + left
        else : 
            f = f[ : len(f) - 1] 
      
    rs=f[0]
    a1='RELATIONSHIP STATUS'
    messagebox.showinfo("RELATIONSHIP ",message=(a1,':',rs) ,icon='question')

    p1.delete(0,END)
    p2.delete(0,END)

Label(pg,text=' ',bg='sky blue').pack()
b1=Button(pg,command=bm,text='SUBMIT',fg='black',font=('GungsuhChe 30 bold'))
b1.pack()

def credit():
    messagebox.showinfo("CREDITS",message=('''PRASANTH ANAND.P
JOTHISHWAR.S''') ,icon='info')
b2=Button(pg,text='CREDITS',command=credit,fg='black',font=('GungsuhChe 30 bold'))
b2.pack()

pg.mainloop()
