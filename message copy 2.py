from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector
import datetime
import csv
from tkinter.filedialog import asksaveasfile

mydb=mysql.connector.connect(host='localhost',user='root',passwd='kingfisher',database='test')
cursor=mydb.cursor()
fn='times new roman'

while(1):
    try:
        sql=('''CREATE TABLE MEDICAL_RECORDS(
        ADMN_NUMBER INT(200) PRIMARY KEY,
        NAME CHAR(130) NOT NULL,
        AGE INT(3),
        GENDER CHAR(50),
        DATE_OF_BIRTH VARCHAR(200),
        HEIGHT INT(10),
        WEIGHT INT(10),
        BLOOD_GROUP CHAR(10),
        COVID_STATUS CHAR(5),
        COVID_VACCINATION_STATUS CHAR(15),
        PAST_HISTORY CHAR(150),
        MAJOR_ILLNESS CHAR(150),
        IMPLANTS char(150))''')
        cursor.execute(sql)
    except mysql.connector.errors.ProgrammingError:
        break

def dob():
    a=c3.get()
    b=c4.get()
    c=c5.get()
    val=a+'  '+b+' '+c
    return val

def vaccine():
    return f.get()

def COVID():
    return r.get()

def blood_GROUP():
    return c1.get()

def gender():
    return c2.get()

def viewlay_input():
   a=var1.get()
   b=var2.get()
   c=var3.get()
   values=a+' '+b+' '+c 
   return values

def viewlay1():
    h=ent12.get()
    return h

def viewlay2():
    d=var4.get()
    e=var5.get()
    f=var6.get()
    g=ent14.get()
    val=d+' '+e+' '+f+' '+g
    return val

def BMI():
    try:
        a=int(ent6.get())/100
        b=a*a
        BMI=int(ent7.get())/float(b)
        print('Your BMI is:',BMI)
        BMI=round(BMI,1)
        bmi_index(BMI)
    except:
        messagebox.showerror('SORRY',"Couldn't find BMI")

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi-BMI_CALCULATOR',f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-BMI_CALCULATOR', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-BMI_CALCULATOR', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('bmi-BMI_CALCULATOR', 'something went wrong!')

def close():
    new_window.destroy()
    
def savedata():
    admn_number=ent1.get()
    name=ent2.get()
    Name=name.title()
    age=ent3.get()
    Gender=gender()
    Dob=dob()
    height=ent6.get()
    weight=ent7.get()
    blood_group=blood_GROUP()
    covid_status=vaccine()
    covid_vaccination_status=COVID()
    past_history=viewlay_input()
    illness=viewlay1()
    implant=viewlay2()
    
    try:
        cursor.execute('''insert into medical_records
         (admn_number,name,age,gender,date_of_birth,height,weight,blood_group,covid_status,
         covid_vaccination_status,past_history,major_illness,implants)'''
         "values('"+admn_number+"','"+Name+"','"+age+"','"+Gender+"','"+Dob+"','"+height+"','"+weight+"','"+blood_group+"','"+covid_status+"','"+covid_vaccination_status+"','"+past_history+"','"+illness+"','"+implant+"')")
        mydb.commit()
        messagebox.showinfo('Success','Record inserted')
    except:
        messagebox.showerror('duplicate error','Record already exists')

def close1():
    main_window.destroy()

def INSERT():
    global new_window,ent1,ent2,ent3,ent6,ent7,ent12,ent14,c1,c2,c3,c4,c5,f,r
    new_window=Toplevel(main_window)
    new_window.title('ENTER RECORD')
    l=['ADMN NUMBER','NAME','AGE','GENDER','DOB','HEIGHT(cm)','WEIGHT(kg)','BLOOD GROUP',
       'COVID STATUS','COVID VACCINATION STATUS','Past History','Any major illness/operations in past',
       'Using any implant/accessories']

    lab1=Label(new_window,text=l[0],font=(fn,13)).grid(row=0,column=0)
    lab2=Label(new_window,text=l[1],font=(fn,13)).grid(row=1,column=0)
    lab3=Label(new_window,text=l[2],font=(fn,13)).grid(row=2,column=0)
    lab4=Label(new_window,text=l[3],font=(fn,13)).grid(row=3,column=0)
    lab5=Label(new_window,text=l[4],font=(fn,13)).grid(row=4,column=0)
    lab6=Label(new_window,text=l[5],font=(fn,13)).grid(row=5,column=0)
    lab7=Label(new_window,text=l[6],font=(fn,13)).grid(row=6,column=0)
    lab8=Label(new_window,text=l[7],font=(fn,13)).grid(row=7,column=0)
    lab9=Label(new_window,text=l[8],font=(fn,13)).grid(row=8,column=0)
    lab10=Label(new_window,text=l[9],font=(fn,13)).grid(row=9,column=0)
    lab11=Label(new_window,text=l[10],font=(fn,13)).grid(row=10,column=0)
    lab12=Label(new_window,text='').grid(row=11,column=0)
    lab13=Label(new_window,text=l[11],font=(fn,13)).grid(row=12,column=0)
    lab14=Label(new_window,text=l[12],font=(fn,13)).grid(row=13,column=0)

    ent1=Entry(new_window)
    ent1.grid(row=0,column=1)
    ent2=Entry(new_window)
    ent2.grid(row=1,column=1)
    ent3=Entry(new_window)
    ent3.grid(row=2,column=1)
    ent6=Entry(new_window)
    ent6.grid(row=5,column=1)
    ent7=Entry(new_window)
    ent7.grid(row=6,column=1)
    ent12=Entry(new_window)
    ent12.grid(row=12,column=1)
    ent14=Entry(new_window)
    ent14.grid(row=16,column=1)

    t1 = Checkbutton(new_window, text="Jaundice", variable=var1, onvalue='Jaundice', offvalue='')
    t1.grid(sticky='W',row=10,column=1)
    t2 = Checkbutton(new_window, text="Allergies", variable=var2, onvalue='Allergies', offvalue='')
    t2.grid(sticky='W',row=10,column=2)
    t3 = Checkbutton(new_window, text="Blood Transfusion", variable=var3, onvalue='Blood Transfusion', offvalue='')
    t3.grid(sticky='W',row=11,column=1)
    t4 = Checkbutton(new_window, text="NIL", variable=var3, onvalue='NIL', offvalue='')
    t4.grid(sticky='W',row=11,column=2)
    t5 = Checkbutton(new_window, text="Dental implant", variable=var4, onvalue='Dental implant', offvalue='')
    t5.grid(sticky='W',row=13,column=1)
    t6 = Checkbutton(new_window, text='Braces', variable=var5, onvalue='Braces', offvalue='')
    t6.grid(sticky='W',row=13,column=2)
    t7 = Checkbutton(new_window, text="Spectacles", variable=var6, onvalue='Spectacles', offvalue='')
    t7.grid(sticky='W',row=14,column=1)
    t8 = Checkbutton(new_window, text="NIL", variable=var6, onvalue='NIL', offvalue='')
    t8.grid(sticky='W',row=14,column=2)

    blood=['O -ve','O +ve','A -ve','A +ve','B -ve','B +ve','AB -ve','AB +ve']
    gender=['Male','Female','Other']
    date=[]
    for i in range(1,32):
        date.append(i)
    months=['January','February','March','April','May','June','July','August','September','October',
    'Novermber','December']
    year=[]
    for i in range(1940,2050):
        year.append(i)

    c1=StringVar()
    c1.set('BLOOD GROUP')
    c2=StringVar()
    c2.set('M/F/O')
    c3=StringVar()
    c3.set('Date')
    c4=StringVar()
    c4.set('Month')
    c5=StringVar()
    c5.set('Year')
    d1=OptionMenu(new_window,c1,*blood)
    d2=OptionMenu(new_window,c2,*gender)
    d3=OptionMenu(new_window,c3,*date)
    d4=OptionMenu(new_window,c4,*months)
    d5=OptionMenu(new_window,c5,*year)
    d1.grid(row=7,column=1)
    d2.grid(row=3,column=1)
    d3.grid(sticky='W',row=4,column=1)
    d4.grid(sticky='E',row=4,column=1)
    d5.grid(sticky='W',row=4,column=2)

    def dell():
        msg_box=tk.messagebox.askquestion('Enter Record','Click yes to save')
        if msg_box=='yes':
            savedata()

    b1=Button(new_window,text="Enter",command=dell,bg='light grey')
    b2=Button(new_window,text='Find BMI',command=BMI,bg='light grey')
    b3=Button(new_window,text='Exit',command=close,bg='light grey')
    b1.grid(sticky='E',row=20,column=2)
    b2.grid(row=6,column=2)
    b3.grid(sticky='W',row=20,column=3)

    f=StringVar()
    YES = Radiobutton(new_window,text="YES",variable=f,value='Yes',command=vaccine())
    YES.grid(row=8,column=1,sticky="W")
    NO = Radiobutton(new_window,text="NO",variable=f,value='No',command=vaccine())
    NO.grid(row=8,column=2,sticky="N")

    r=StringVar()
    YES = Radiobutton(new_window,text="YES",variable=r,value='Yes',command=vaccine())
    YES.grid(row=9,column=1,sticky="W")
    NO = Radiobutton(new_window,text="NO",variable=r,value='No',command=vaccine())
    NO.grid(row=9,column=2,sticky="N")

def dlt():
    admn=IntVar()
    import tkinter as tk
    cursor=mydb.cursor()
    dlte=tk.Tk()
    dlte.title('Delete')
    dlte.geometry('520x350')

    lab1=Label(dlte,text='ADMN NUMBER:',font=(fn,13))
    lab1.grid(row=1,column=0)
    e1=Entry(dlte,textvariable=admn)
    e1.grid(row=1,column=1)

    btnn=Button(dlte,text='FIND',command=lambda:[disp(),butnboom()],bg='light grey')
    btnn.grid(row=1,column=2)
    
    def butnboom():
        try:
            btnn.destroy()
        except:
            pass

    def disp():
        nonlocal admn
        a=e1.get()
        query='SELECT * FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format(a)
        try:
            cursor.execute(query)
        except:
            dlte.destroy()
            messagebox.showerror('OOPS','NO RECORD')
        data=cursor.fetchall()
        mydb.commit()
        
        if data!=[]:
            lab2=Label(dlte,text='NAME :',font=(fn, 13)).grid(row=2,column=0)
            lab3=Label(dlte,text='AGE :',font=(fn, 13)).grid(row=3,column=0)
            lab4=Label(dlte,text='GENDER :',font=(fn, 13)).grid(row=4,column=0)
            lab4=Label(dlte,text='DATE OF BIRTH :',font=(fn, 13)).grid(row=5,column=0)
            lab5=Label(dlte,text='HEIGHT(cm) :',font=(fn, 13)).grid(row=6,column=0)
            lab6=Label(dlte,text='WEIGHT(kg) :',font=(fn, 13)).grid(row=7,column=0)
            lab7=Label(dlte,text='BLOOD GROUP :',font=(fn, 13)).grid(row=8,column=0)
            lab8=Label(dlte,text='COVID STATUS :',font=(fn, 13)).grid(row=9,column=0)
            lab9=Label(dlte,text='COVID VACCINATION STATUS :',font=(fn, 13)).grid(row=10,column=0)
            lab10=Label(dlte,text='PAST HISTORY :',font=(fn, 13)).grid(row=11,column=0)
            lab11=Label(dlte,text='Any major illness/operations in past :',font=('times new roman',13)).grid(row=12,column=0)
            lab12=Label(dlte,text='Using any implant/accessories :',font=('times new roman',13)).grid(row=13,column=0)
            
            for i in range(1):
                p=list(data[i])
                name=(p[1])
                age=(p[2])
                gender=(p[3])
                date_of_birth=(p[4])
                height=(p[5])
                weight=(p[6])
                blood_group=(p[7])
                covid_status=(p[8])
                covid_vaccination_status=(p[9])
                past_history=(p[10])
                illness=(p[11])
                implant=(p[12])

            e2=Label(dlte,text=name,font=(fn,13)).grid(row=2,column=1)
            e3=Label(dlte,text=age,font=(fn,13)).grid(row=3,column=1)
            e4=Label(dlte,text=gender,font=(fn,13)).grid(row=4,column=1)
            e5=Label(dlte,text=date_of_birth,font=(fn,13)).grid(row=5,column=1)
            e6=Label(dlte,text=height,font=(fn,13)).grid(row=6,column=1)
            e7=Label(dlte,text=weight,font=(fn,13)).grid(row=7,column=1)
            e8=Label(dlte,text=blood_group,font=(fn,13)).grid(row=8,column=1)
            e9=Label(dlte,text=covid_status,font=(fn,13)).grid(row=9,column=1)
            e10=Label(dlte,text=covid_vaccination_status,font=(fn,13)).grid(row=10,column=1)
            e11=Label(dlte,text=past_history,font=(fn,13)).grid(row=11,column=1)
            e12=Label(dlte,text=illness,font=(fn,13)).grid(row=12,column=1)
            e13=Label(dlte,text=implant,font=(fn,13)).grid(row=13,column=1)
            butn=Button(dlte,text='DELETE',command=dell,bg='light grey').grid(row=13,column=3)
        else:
            try:
                dlte.destroy()
                messagebox.showerror('OOPS','NO RECORD')
            except:
                pass
            
    def boom():
        dlte.destroy()
        
    btn=Button(dlte,text='EXIT',command=boom,bg='light grey').grid(row=13,column=2)

    def yo():
        try:
            a=e1.get()
            cursor.execute('Use test;')
            query='DELETE FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format(a)
            cursor.execute(query)
            data=cursor.fetchall()
            mydb.commit()
            dlte.destroy()
            messagebox.showinfo('SUCCESS','RECORD DELETED')
        except:
            messagebox.showerror('OOPS','NO RECORD')
            
    def dell():
        msg_box=tk.messagebox.askquestion('Delete Record','Are you sure you want to delete this record?',icon='warning')
        if msg_box=='yes':
            yo()
            try:
                dlte.destroy()
            except:
                pass

def modify():
    def COVID():
        return r.get()

    def blood_GROUP():
        return c1.get()

    def gender():
        return c2.get()

    def dob():
        a=c3.get()
        b=c4.get()
        c=c5.get()
        val=a+'  '+b+' '+c
        return val

    def viewlay_input():
       a=var1.get()
       b=var2.get()
       c=var3.get()
       values=a+' '+b+' '+c
       return values

    def viewlay1():
        h=ent6.get()
        return h 

    def viewlay2():
        d=var4.get()
        e=var5.get()
        f=var6.get()
        g=ent7.get()
        val=d+' '+e+' '+f+' '+g
        return val
        
    admn=IntVar()
    cursor=mydb.cursor()
    modf=Toplevel(main_window)
    modf.title('Edit')
    modf.geometry('900x500')

    lab1=Label(modf,text='ADMN NUMBER :',font=(fn, 13)).grid(row=1,column=0)
    e1=Entry(modf,textvariable=admn)
    e1.grid(row=1,column=1)
    try:
        btn9=Button(modf,text='FIND',command=lambda:[displ(),bt0()],bg='light grey')
        btn9.grid(row=1,column=2)
    except:
        pass

    var1=StringVar()
    var2=StringVar()
    var3=StringVar()
    var4=StringVar()
    var5=StringVar()
    var6=StringVar()
    var7=StringVar()

    def displ():
        global ent2,ent3,ent4,ent5,ent6,ent7,c1,c2,c3,c4,c5,f,r,g,a
        a=e1.get()
        cursor.execute('Use test;')
        query='SELECT * FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format(a)
        try:
            cursor.execute(query)
        except:
            modf.destroy()
            messagebox.showerror('OOPS','NO RECORD')
        data=cursor.fetchall()
        mydb.commit()

        if data!=[]:
            fo='times new roman'
            lab=Label(modf,text='EXISTING RECORD',font=('eras demi ITC',16)).grid(row=0,column=0)
            lab2=Label(modf,text='NAME :',font=(fo,13)).grid(row=2,column=0)
            lab3=Label(modf,text='AGE :',font=(fo,13)).grid(row=3,column=0)
            lab4=Label(modf,text='GENDER :',font=(fo,13)).grid(row=4,column=0)
            lab4=Label(modf,text='DATE OF BIRTH :',font=(fo,13)).grid(row=5,column=0)
            lab5=Label(modf,text='HEIGHT(cm) :',font=(fo,13)).grid(row=6,column=0)
            lab6=Label(modf,text='WEIGHT(kg) :',font=(fo,13)).grid(row=7,column=0)
            lab7=Label(modf,text='BLOOD GROUP :',font=(fo,13)).grid(row=8,column=0)
            lab8=Label(modf,text='COVID STATUS :',font=(fo,13)).grid(row=9,column=0)
            lab9=Label(modf,text='COVID VACCINATION STATUS :',font=(fo,13)).grid(row=10,column=0)
            lab10=Label(modf,text='PAST HISTORY :',font=(fo,13)).grid(row=11,column=0)
            lab11=Label(modf,text='Any major illness/operations in past :',font=(fo,13)).grid(row=12,column=0)
            lab12=Label(modf,text='Using any implant/accessories :',font=(fo,13)).grid(row=13,column=0)
            
            for i in range(1):
                p=list(data[i])
                name=(p[1])
                age=(p[2])
                gender=(p[3])
                date_of_birth=(p[4])
                height=(p[5])
                weight=(p[6])
                blood_group=(p[7])
                covid_status=(p[8])
                covid_vaccination_status=(p[9])
                past_history=(p[10])
                illness=(p[11])
                implant=(p[12])

            e2=Label(modf,text=name,font=(fn,13)).grid(row=2,column=1)
            e3=Label(modf,text=age,font=(fn,13)).grid(row=3,column=1)
            e4=Label(modf,text=gender,font=(fn,13)).grid(row=4,column=1)
            e5=Label(modf,text=date_of_birth,font=(fn,13)).grid(row=5,column=1)
            e6=Label(modf,text=height,font=(fn,13)).grid(row=6,column=1)
            e7=Label(modf,text=weight,font=(fn,13)).grid(row=7,column=1)
            e8=Label(modf,text=blood_group,font=(fn,13)).grid(row=8,column=1)
            e9=Label(modf,text=covid_status,font=(fn,13)).grid(row=9,column=1)
            e10=Label(modf,text=covid_vaccination_status,font=(fn,13)).grid(row=10,column=1)
            e11=Label(modf,text=past_history,font=(fn,13)).grid(row=11,column=1)
            e12=Label(modf,text=illness,font=(fn,13)).grid(row=12,column=1)
            e13=Label(modf,text=implant,font=(fn,13)).grid(row=13,column=1)
            
        else:
            modf.destroy()
            messagebox.showerror('OOPS','NO RECORD')
            

        f='times new roman'
    
        l=['ADMN NUMBER','NAME','AGE','GENDER','DOB','HEIGHT(cm)','WEIGHT(kg)','BLOOD GROUP',
           'COVID STATUS','COVID VACCINATION STATUS','Past History','Any major illness/operations in past',
           'Using any implant/accessories']

        try:
            L=Label(modf,text='EDIT RECORD',font=('eras demi ITC',16)).grid(row=0,column=2)
            lab1=Label(modf,text=l[0],font=(f,13)).grid(row=1,column=2)
            lab2=Label(modf,text=l[1],font=(f,13)).grid(row=2,column=2)
            lab3=Label(modf,text=l[2],font=(f,13)).grid(row=3,column=2)
            lab4=Label(modf,text=l[3],font=(f,13)).grid(row=4,column=2)
            lab5=Label(modf,text=l[4],font=(f,13)).grid(row=5,column=2)
            lab6=Label(modf,text=l[5],font=(f,13)).grid(row=6,column=2)
            lab7=Label(modf,text=l[6],font=(f,13)).grid(row=7,column=2)
            lab8=Label(modf,text=l[7],font=(f,13)).grid(row=8,column=2)
            lab9=Label(modf,text=l[8],font=(f,13)).grid(row=9,column=2)
            lab10=Label(modf,text=l[9],font=(f,13)).grid(row=10,column=2)
            lab11=Label(modf,text=l[10],font=(f,13)).grid(row=11,column=2)
            lab12=Label(modf,text='').grid(row=12,column=2)
            lab13=Label(modf,text=l[11],font=(f,13)).grid(row=13,column=2)
            lab14=Label(modf,text=l[12],font=(f,13)).grid(row=14,column=2)
            lab15=Label(modf,text=a,font=(f,13)).grid(row=1,column=3)

            ent2=Entry(modf)
            ent2.grid(row=2,column=3)
            ent3=Entry(modf)
            ent3.grid(row=3,column=3)
            ent4=Entry(modf)
            ent4.grid(row=6,column=3)
            ent5=Entry(modf)
            ent5.grid(row=7,column=3)
            ent6=Entry(modf)
            ent6.grid(row=13,column=3)
            ent7=Entry(modf)
            ent7.grid(row=16,column=3)

            t1 = Checkbutton(modf, text="Jaundice",variable=var1,onvalue='Jaundice',offvalue='')
            t1.grid(sticky='W',row=11,column=3)
            t2 = Checkbutton(modf, text="Allergies",variable=var2,onvalue='Allergies',offvalue='')
            t2.grid(sticky='W',row=11,column=4)
            t3 = Checkbutton(modf, text="Blood Transfusion",variable=var3,onvalue='Blood Transfusion',offvalue='')
            t3.grid(sticky='W',row=12,column=3)
            t4 = Checkbutton(modf, text="NIL",variable=var3,onvalue='NIL',offvalue='')
            t4.grid(sticky='W',row=12,column=4)
            t5 = Checkbutton(modf, text="Dental implant",variable=var4,onvalue='Dental implant',offvalue='')
            t5.grid(sticky='W',row=14,column=3)
            t6 = Checkbutton(modf, text='Braces',variable=var5,onvalue='Braces',offvalue='')
            t6.grid(sticky='W',row=14,column=4)
            t7 = Checkbutton(modf, text="Spectacles",variable=var6,onvalue='Spectacles',offvalue='')
            t7.grid(sticky='W',row=15,column=3)
            t8 = Checkbutton(modf, text="NIL", variable=var6,onvalue='NIL',offvalue='')
            t8.grid(sticky='W',row=15,column=4)

            blood=['O -ve','O +ve','A -ve','A +ve','B -ve','B +ve','AB -ve','AB +ve']
            gender=['Male','Female','Other']
            date=[]
            for i in range(1,32):
                date.append(i)
            months=['January','February','March','April','May','June','July','August','September','October',
            'Novermber','December']
            year=[]
            for i in range(1940,2050):
                year.append(i)

            c1=StringVar()
            c1.set('BLOOD GROUP')
            c2=StringVar()
            c2.set('M/F/O')
            c3=StringVar()
            c3.set('Date')
            c4=StringVar()
            c4.set('Month')
            c5=StringVar()
            c5.set('Year')
            d1=OptionMenu(modf,c1,*blood)
            d2=OptionMenu(modf,c2,*gender)
            d3=OptionMenu(modf,c3,*date)
            d4=OptionMenu(modf,c4,*months)
            d5=OptionMenu(modf,c5,*year)
            d1.grid(row=8,column=3)
            d2.grid(row=4,column=3)
            d3.grid(sticky='W',row=5,column=3)
            d4.grid(sticky='E',row=5,column=3)
            d5.grid(sticky='W',row=5,column=4)
        except:
            pass

        def dell():
            msg_box=tk.messagebox.askquestion('Enter Record','Click yes to save')
            if msg_box=='yes':
                sd()

        try:
            b1=Button(modf,text="Enter",command=dell,bg='light grey')
            b3=Button(modf,text='Exit',command=close2,bg='light grey')
            b1.grid(sticky='E',row=20,column=4)
            b3.grid(sticky='W',row=20,column=5)
        
            g=StringVar()
            YES = Radiobutton(modf,text="YES",variable=g,value='Yes',command=vaccin())
            YES.grid(row=9,column=3,sticky="W")
            NO = Radiobutton(modf,text="NO",variable=g,value='No',command=vaccin())
            NO.grid(row=9,column=4,sticky="N")

            r=StringVar()
            YES = Radiobutton(modf,text="YES",variable=r,value='Yes',command=vaccin())
            YES.grid(row=10,column=3,sticky="W")
            NO = Radiobutton(modf,text="NO",variable=r,value='No',command=vaccin())
            NO.grid(row=10,column=4,sticky="N")
        except:
            pass

    def vaccin():
            return g.get()
    def close2():
            modf.destroy()
    def bt0():
        try:
            btn9.destroy()
        except:
            pass
    btn1=Button(modf,text='EXIT',command=close2,bg='light grey').grid(row=11,column=2)

    def sd():
        name=ent2.get()
        Name=name.title()
        age=ent3.get()
        Gender=gender()
        Dob=dob()
        height=ent4.get()
        weight=ent5.get()
        blood_group=blood_GROUP()
        covid_status=vaccin()
        covid_vaccination_status=COVID()
        past_history=viewlay_input()
        illness=viewlay1()
        implant=viewlay2()

        try:
            cursor.execute('USE TEST')
            cursor.execute('UPDATE MEDICAL_RECORDS SET NAME="{}" WHERE ADMN_NUMBER={};'.format(Name,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET AGE={} WHERE ADMN_NUMBER={};'.format(age,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET GENDER="{}" WHERE ADMN_NUMBER={};'.format(Gender,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET DATE_OF_BIRTH="{}" WHERE ADMN_NUMBER={};'.format(Dob,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET HEIGHT={} WHERE ADMN_NUMBER={};'.format(height,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET WEIGHT={} WHERE ADMN_NUMBER={};'.format(weight,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET BLOOD_GROUP="{}" WHERE ADMN_NUMBER={};'.format(blood_group,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET COVID_STATUS="{}" WHERE ADMN_NUMBER={};'.format(covid_status,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET COVID_VACCINATION_STATUS="{}" WHERE ADMN_NUMBER={};'.format(covid_vaccination_status,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET PAST_HISTORY="{}" WHERE ADMN_NUMBER={};'.format(past_history,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET MAJOR_ILLNESS="{}" WHERE ADMN_NUMBER={};'.format(illness,a))
            cursor.execute('UPDATE MEDICAL_RECORDS SET IMPLANTS="{}" WHERE ADMN_NUMBER={};'.format(implant,a))
            mydb.commit()
            messagebox.showinfo('Success','Record Edited')
        except:
            messagebox.showerror('Error',"Record couldn't be edited , Recheck entry")

def view():
    admn=IntVar()
    import tkinter as tk
    cursor = mydb.cursor()
    view=tk.Tk()
    view.title('Details')
    view.geometry('500x350')
    lab1=Label(view,text='ADMN NUMBER :',font=(fn, 13)).grid(row=1,column=0)
    e1=Entry(view,textvariable=admn)
    e1.grid(row=1,column=1)
    btn9=Button(view,text='VIEW',command=lambda:[disp(),bt0()],bg='light grey')
    btn9.grid(row=1,column=2)
    
    def disp():
        nonlocal admn
        a=e1.get()
        query='SELECT * FROM MEDICAL_RECORDS WHERE ADMN_NUMBER={}'.format(a)
        try:
            cursor.execute(query)
        except:
            view.destroy()
            messagebox.showerror('OOPS','NO RECORD')
        data=cursor.fetchall()
        mydb.commit()

        if data!=[]:
            lab2=Label(view,text='NAME :',font=(fn,13)).grid(row=2,column=0)
            lab3=Label(view,text='AGE :',font=(fn,13)).grid(row=3,column=0)
            lab4=Label(view,text='GENDER :',font=(fn,13)).grid(row=4,column=0)
            lab4=Label(view,text='DATE OF BIRTH :',font=(fn,13)).grid(row=5,column=0)
            lab5=Label(view,text='HEIGHT(cm) :',font=(fn,13)).grid(row=6,column=0)
            lab6=Label(view,text='WEIGHT(kg) :',font=(fn,13)).grid(row=7,column=0)
            lab7=Label(view,text='BLOOD GROUP :',font=(fn,13)).grid(row=8,column=0)
            lab8=Label(view,text='COVID STATUS :',font=(fn,13)).grid(row=9,column=0)
            lab9=Label(view,text='COVID VACCINATION STATUS :',font=(fn,13)).grid(row=10,column=0)
            lab10=Label(view,text='PAST HISTORY :',font=(fn,13)).grid(row=11,column=0)
            lab11=Label(view,text='Any major illness/operations in past :',font=(fn,13)).grid(row=12,column=0)
            lab12=Label(view,text='Using any implants/accessories :',font=(fn,13)).grid(row=13,column=0)

            for i in range(1):
                p=list(data[i])
                name=(p[1])
                age=(p[2])
                gender=(p[3])
                date_of_birth=(p[4])
                height=(p[5])
                weight=(p[6])
                blood_group=(p[7])
                covid_status=(p[8])
                covid_vaccination_status=(p[9])
                past_history=(p[10])
                illness=(p[11])
                implants=(p[12])

            e2=Label(view,text=name,font=(fn,13)).grid(row=2,column=1)
            e3=Label(view,text=age,font=(fn,13)).grid(row=3,column=1)
            e4=Label(view,text=gender,font=(fn,13)).grid(row=4,column=1)
            e5=Label(view,text=date_of_birth,font=(fn,13)).grid(row=5,column=1)
            e6=Label(view,text=height,font=(fn,13)).grid(row=6,column=1)
            e7=Label(view,text=weight,font=(fn,13)).grid(row=7,column=1)
            e8=Label(view,text=blood_group,font=(fn,13)).grid(row=8,column=1)
            e9=Label(view,text=covid_status,font=(fn,13)).grid(row=9,column=1)
            e10=Label(view,text=covid_vaccination_status,font=(fn,13)).grid(row=10,column=1)
            e11=Label(view,text=past_history,font=(fn,13)).grid(row=11,column=1)
            e12=Label(view,text=illness,font=(fn,13)).grid(row=12,column=1)
            e13=Label(view,text=implants,font=(fn,13)).grid(row=13,column=1)

        else:
            try:
                view.destroy()
                messagebox.showerror('OOPS','NO RECORD')
            except:
                pass
            
    def close2():
            view.destroy()
    def bt0():
        try:
            btn9.destroy()
        except:
            pass
    btn1=Button(view,text='EXIT',command=close2,bg='light grey').grid(row=13,column=2)

def main():
    global main_window
    main_window=Toplevel(root)
    main_window.geometry('240x200')
    main_window.title('Medical Records Maintenance')

    btn1=Button(main_window,text='ADD NEW RECORD',command=INSERT,bg='lavender').pack(padx=10,pady=5,ipadx=50)
    btn2=Button(main_window,text='DISPLAY RECORD',command=view,bg='lavender').pack(padx=10,pady=5,ipadx=50)
    btn3=Button(main_window,text='MODIFY RECORD',command=modify,bg='lavender').pack(padx=10,pady=5,ipadx=50)
    btn4=Button(main_window,text='DELETE RECORD',command=dlt,bg='lavender').pack(padx=10,pady=5,ipadx=50)
    btn5=Button(main_window,text='EXIT',command=lambda:[close1(),root.destroy()],bg='light grey').pack(pady=5,ipadx=25)

def login():
    global ent1,ent2,admin
    admin=tk.Tk()
    admin.title('LOGIN')
    admin.geometry('300x150')
    #admin.iconphoto(False,icoon)
    l=Label(admin,text='').grid(row=0,column=0)
    lab1=Label(admin,text='   USERNAME :',font=(fn,15)).grid(row=1,column=0)
    lab2=Label(admin,text='   PASSWORD :',font=(fn,15)).grid(row=2,column=0)
    ent1=Entry(admin)
    ent1.grid(row=1,column=1)
    ent2=Entry(admin,show='•')#•●
    ent2.grid(row=2,column=1)
    l=Label(admin,text='').grid(row=3,column=0)
    b1=Button(admin,text='LOGIN',command=log,bg='light grey')
    b1.grid(row=4,column=1)

def log():
    a=ent1.get()
    b=ent2.get()
    if a=='admin' and b=='admin':
        main()
        admin.destroy()
    else:
        messagebox.showerror('OOPS','INCORRECT USERNAME OR PASSWORD')
    
root=Tk()
root.geometry('600x400')
bg=PhotoImage(file='medi4.png')
#root.configure(bg='light grey')
root.title('MEDICAL RECORDS')
icoon=PhotoImage(file='cross.png')
root.iconphoto(False,icoon)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()

lab2=Label(root,text='M E D I C A L   R E C O R D S   M A I N T E N A N C E',font=('Agency FB bold',19),bg='light grey')
lab2.pack(padx=20,pady=20)
lab1=Label(root,image=bg)
lab1.pack(padx=20)
f1=Frame(root)
f1.pack(pady=20)
b1=Button(f1,text='ENTER',command=login,bg='light grey')
b1.pack()
b2=Button(f1,text='EXIT',command=lambda:[root.destroy()],bg='light grey')
b2.pack()

root.mainloop()







            
