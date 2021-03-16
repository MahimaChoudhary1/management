def addname():
    def submitadd():
        id =idvalue.get()
        name =namevalue.get()
        mobile =mobilevalue.get()
        email =emailvalue.get()
        address =addressvalue.get()
        gender =gendervalue.get()
        dob =dobvalue.get()
        addeddate = time.strftime("%d/%m/%Y")
        addedtime =time.strftime("%H:%M:%Y")
        try:
            strr='insert into details value(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res=messagebox.askyesnocancel('notification','Id{} Name{} added successfully. If you want to clean '.format(id,name),parent=addroot)
            if(res==True):
                idvalue.set('')
                namevalue.set('')
                mobilevalue.set('')
                emailvalue.set('')
                addressvalue.set('')
                gendervalue.set('')
                dobvalue.set('')

        except:
            messagebox.showerror('notification','Id already exist try with another Id',parent=addroot)
        strr='select * from details'
        mycursor.execute(strr)
        datas= mycursor.fetchall()
        table.delete(*table.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            table.insert('',END,value=vv)

    addroot= Toplevel(master=frame1)
    addroot.grab_set()
    addroot.geometry('900x490+200+200')
    addroot.title('Add Name')
    addroot.config(bg='powderblue')
    addroot.iconbitmap('mini.ico')
    addroot.resizable(False,False)
    #------------------------------------------------------ added option
    idlabel=Label(addroot,text='Enter Id:',bg='skyblue',font=('Codec',20,'bold'),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text='Enter Name:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=14,anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=14,anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=14,anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=14,anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=14,anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=14,anchor='w')
    doblabel.place(x=10, y=370)
    #------------------------------------------------------------------------- add entry
    idvalue=StringVar()
    namevalue=StringVar()
    mobilevalue=StringVar()
    emailvalue=StringVar()
    addressvalue=StringVar()
    gendervalue=StringVar()
    dobvalue=StringVar()
    identry=Entry(addroot,font=('Ruluko',20),bd=2,textvariable=idvalue)
    identry.place(x=300,y=10,width=570,height=39)

    nameentry = Entry(addroot, font=('Ruluko', 20), bd=2, textvariable=namevalue)
    nameentry.place(x=300, y=70, width=570, height=39)

    mobileentry = Entry(addroot, font=('Ruluko', 20), bd=2, textvariable=mobilevalue)
    mobileentry.place(x=300, y=130, width=570, height=39)

    emailentry = Entry(addroot, font=('Ruluko', 20), bd=2, textvariable=emailvalue)
    emailentry.place(x=300, y=190, width=570, height=39)

    addressentry = Entry(addroot, font=('Ruluko', 20), bd=2, textvariable=addressvalue)
    addressentry.place(x=300, y=250, width=570, height=39)

    genderentry = Entry(addroot, font=('Ruluko', 20), bd=2, textvariable=gendervalue)
    genderentry.place(x=300, y=310, width=570, height=39)

    dobentry = Entry(addroot, font=('Ruluko', 20), bd=2, textvariable=dobvalue)
    dobentry.place(x=300, y=370, width=570, height=39)
    #------------------------------------------------------ button
    submitbutton = Button(addroot, text='Submit', font=('Ruluko', 15, 'bold'), bd=4, width=20,
                          activebackground='lavender'
                          , activeforeground='black',command=submitadd)
    submitbutton.place(x=200,y=430)


    addroot.mainloop()

def searchname():
        def search():
            id = idvalue.get()
            name = namevalue.get()
            mobile = mobilevalue.get()
            email = emailvalue.get()
            address = addressvalue.get()
            gender = gendervalue.get()
            dob = dobvalue.get()
            addeddate = time.strftime("%d/%m/%Y")
            if(id != ''):
                strr='select * from details where id=%s'
                mycursor.execute(strr,(id))
                datas=mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)
            elif (id != ''):
                strr = 'select * from details where id=%s'
                mycursor.execute(strr, (id))
                datas = mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)
            elif (name != ''):
                strr = 'select * from details where name=%s'
                mycursor.execute(strr, (name))
                datas = mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)
            elif (mobile != ''):
                strr = 'select * from details where mobile=%s'
                mycursor.execute(strr, (mobile))
                datas = mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)
            elif (email != ''):
                strr = 'select * from details where email=%s'
                mycursor.execute(strr, (email))
                datas = mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)
            elif (address != ''):
                strr = 'select * from details where address=%s'
                mycursor.execute(strr, (address))
                datas = mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)
            elif (gender != ''):
                strr = 'select * from details where gender=%s'
                mycursor.execute(strr, (gender))
                datas = mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)
            elif (dob != ''):
                strr = 'select * from details where dob=%s'
                mycursor.execute(strr, (dob))
                datas = mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)
            elif (addeddate != ''):
                strr = 'select * from details where addeddate=%s'
                mycursor.execute(strr, (addeddate))
                datas = mycursor.fetchall()
                table.delete(*table.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                    table.insert('', END, value=vv)

        searchroot = Toplevel(master=frame1)
        searchroot.grab_set()
        searchroot.geometry('900x550+200+200')
        searchroot.title('Search from')
        searchroot.config(bg='powderblue')
        searchroot.iconbitmap('mini.ico')
        searchroot.resizable(False, False)
        # ------------------------------------------------------ added option
        idlabel = Label(searchroot, text='Enter Id:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=14, anchor='w')
        idlabel.place(x=10, y=10)

        namelabel = Label(searchroot, text='Enter Name:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                          borderwidth=3,
                          width=14, anchor='w')
        namelabel.place(x=10, y=70)

        mobilelabel = Label(searchroot, text='Enter Mobile:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                            borderwidth=3,
                            width=14, anchor='w')
        mobilelabel.place(x=10, y=130)

        emaillabel = Label(searchroot, text='Enter Email:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                           borderwidth=3,
                           width=14, anchor='w')
        emaillabel.place(x=10, y=190)

        addresslabel = Label(searchroot, text='Enter Address:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                             borderwidth=3,
                             width=14, anchor='w')
        addresslabel.place(x=10, y=250)

        genderlabel = Label(searchroot, text='Enter Gender:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                            borderwidth=3,
                            width=14, anchor='w')
        genderlabel.place(x=10, y=310)

        doblabel = Label(searchroot, text='Enter D.O.B:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                         borderwidth=3,
                         width=14, anchor='w')
        doblabel.place(x=10, y=370)

        datelabel = Label(searchroot, text='Enter Date:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                         borderwidth=3,
                         width=14, anchor='w')
        datelabel.place(x=10, y=430)
        # ------------------------------------------------------------------------- add entry
        idvalue = StringVar()
        namevalue = StringVar()
        mobilevalue = StringVar()
        emailvalue = StringVar()
        addressvalue = StringVar()
        gendervalue = StringVar()
        dobvalue = StringVar()
        datevalue=StringVar()
        identry = Entry(searchroot, font=('Ruluko', 20), bd=2, textvariable=idvalue)
        identry.place(x=300, y=10, width=570, height=39)

        nameentry = Entry(searchroot, font=('Ruluko', 20), bd=2, textvariable=namevalue)
        nameentry.place(x=300, y=70, width=570, height=39)

        mobileentry = Entry(searchroot, font=('Ruluko', 20), bd=2, textvariable=mobilevalue)
        mobileentry.place(x=300, y=130, width=570, height=39)

        emailentry = Entry(searchroot, font=('Ruluko', 20), bd=2, textvariable=emailvalue)
        emailentry.place(x=300, y=190, width=570, height=39)

        addressentry = Entry(searchroot, font=('Ruluko', 20), bd=2, textvariable=addressvalue)
        addressentry.place(x=300, y=250, width=570, height=39)

        genderentry = Entry(searchroot, font=('Ruluko', 20), bd=2, textvariable=gendervalue)
        genderentry.place(x=300, y=310, width=570, height=39)

        dobentry = Entry(searchroot, font=('Ruluko', 20), bd=2, textvariable=dobvalue)
        dobentry.place(x=300, y=370, width=570, height=39)

        dateentry = Entry(searchroot, font=('Ruluko', 20), bd=2, textvariable=datevalue)
        dateentry.place(x=300, y=430, width=570, height=39)
        # ------------------------------------------------------ button
        submitbutton = Button(searchroot, text='Submit', font=('Ruluko', 15, 'bold'), bd=4, width=20,
                              activebackground='lavender'
                              , activeforeground='black', command=search)
        submitbutton.place(x=220, y=490)

        searchroot.mainloop()

def updatename():
    def update():
        id = idvalue.get()
        name = namevalue.get()
        mobile = mobilevalue.get()
        email = emailvalue.get()
        address = addressvalue.get()
        gender = gendervalue.get()
        dob = dobvalue.get()
        date = datevalue.get()
        time = timevalue.get()
        strr='update details set name = %s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('notification', 'Id{} modified sucessfully'.format(id),parent=updateroot)
        strr = 'select * from details'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        table.delete(*table.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            table.insert('', END, value=vv)


    updateroot = Toplevel(master=frame1)
    updateroot.grab_set()
    updateroot.geometry('900x600+200+170')
    updateroot.title('Update')
    updateroot.config(bg='powderblue')
    updateroot.iconbitmap('mini.ico')
    updateroot.resizable(False, False)
    # ------------------------------------------------------ added option
    idlabel = Label(updateroot, text='Update Id:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=14, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Update Name:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,
                      width=14, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Update Mobile:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                        borderwidth=3,
                        width=14, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Update Email:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                       borderwidth=3,
                       width=14, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Update Address:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                         borderwidth=3,
                         width=14, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Update Gender:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                        borderwidth=3,
                        width=14, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Update D.O.B:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                     borderwidth=3,
                     width=14, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Update Date:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,
                      width=14, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Update Time:', bg='skyblue', font=('Codec', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,
                      width=14, anchor='w')
    timelabel.place(x=10, y=490)
    # ------------------------------------------------------------------------- add entry
    idvalue = StringVar()
    namevalue = StringVar()
    mobilevalue = StringVar()
    emailvalue = StringVar()
    addressvalue = StringVar()
    gendervalue = StringVar()
    dobvalue = StringVar()
    datevalue = StringVar()
    timevalue=StringVar()
    identry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=idvalue)
    identry.place(x=300, y=10, width=570, height=39)

    nameentry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=namevalue)
    nameentry.place(x=300, y=70, width=570, height=39)

    mobileentry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=mobilevalue)
    mobileentry.place(x=300, y=130, width=570, height=39)

    emailentry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=emailvalue)
    emailentry.place(x=300, y=190, width=570, height=39)

    addressentry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=addressvalue)
    addressentry.place(x=300, y=250, width=570, height=39)

    genderentry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=gendervalue)
    genderentry.place(x=300, y=310, width=570, height=39)

    dobentry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=dobvalue)
    dobentry.place(x=300, y=370, width=570, height=39)

    dateentry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=datevalue)
    dateentry.place(x=300, y=430, width=570, height=39)

    timeentry = Entry(updateroot, font=('Ruluko', 20), bd=2, textvariable=timevalue)
    timeentry.place(x=300, y=490, width=570, height=39)
    # ------------------------------------------------------ button
    submitbutton = Button(updateroot, text='Submit', font=('Ruluko', 15, 'bold'), bd=4, width=20,
                          activebackground='lavender'
                          , activeforeground='black', command=update)
    submitbutton.place(x=220, y=545)
    cc=table.focus()
    content=table.item(cc)
    pp=content['values']
    if(len(pp) !=0):
        idvalue.set(pp[0])
        namevalue.set(pp[1])
        mobilevalue.set(pp[2])
        emailvalue.set(pp[3])
        addressvalue.set(pp[4])
        gendervalue.set(pp[5])
        dobvalue.set(pp[6])
        datevalue.set(pp[7])
        timevalue.set(pp[8])

    updateroot.mainloop()

def deletename():
    cc=table.focus()
    content = table.item(cc)
    pp = content ['values'] [0]
    strr='delete from details where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('notification','Id{} deleted sucessfully'.format(pp))
    strr = 'select * from details'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    table.delete(*table.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        table.insert('', END, value=vv)
def showname():
    global con,mycursor
    strr = 'select * from details'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    table.delete(*table.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        table.insert('', END, value=vv)

def exportname():
    ff=filedialog.asksaveasfilename()
    gg=table.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=table.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),
        gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Addeddate','Addedtime']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('notification', 'your data is saved'.format(paths))

def exitname():
    res = messagebox.askyesnocancel('Notification', 'Do you want to Exit?')
    if (res == True):
        root.destroy()


##########################################################################################  CONNECTION DB
def connectdb():
    def submitdb():
        global con,mycursor
        host = hostvalue.get()
        user = uservalue.get()
        password = passwordvalue.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()

        except:
            messagebox.showerror('notification', 'data is incorrect',parent=dbroot)
            return
        try:
            strr = 'create database msystemdb'
            mycursor.execute(strr)
            strr = 'use msystemdb'
            mycursor.execute(strr)
            strr = 'create table details(id int,name varchar(25),mobile varchar(12),email varchar(45),address varchar(100),gender varchar(15),dob varchar(45),date varchar(20),time yarchar(20))'
            mycursor.execute(strr)
            messagebox.showinfo('notification', 'database is created and now you are connected to the database', parent=dbroot)
        except:
            strr = 'use msystemdb'
            mycursor.execute(strr)
            messagebox.showinfo('notification','now you are connected to the database',parent=dbroot)
        dbroot.destroy()

    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.resizable(False,False)
    dbroot.geometry('500x300+800+230')
    dbroot.iconbitmap('mini.ico')
    dbroot.config(bg='floralwhite')
    #  --------------------------------------------lables
    hostlable = Label(dbroot,text='Enter Host:',font=('CafeFrancoise',18),relief=GROOVE,borderwidth=4,bg='white',width=12)
    hostlable.place(x=10,y=10)

    userlable = Label(dbroot, text='Enter User:', font=('CafeFrancoise',18), relief=GROOVE, borderwidth=4,
                    bg='white', width=12)
    userlable.place(x=10, y=100)

    passwordlable = Label(dbroot, text='Enter Password:', font=('CafeFrancoise', 18), relief=GROOVE, borderwidth=4,
                    bg='white', width=14)
    passwordlable.place(x=10, y=200)
    #---------------------------------------------  entry
    hostvalue=StringVar()
    uservalue = StringVar()
    passwordvalue = StringVar()

    hostentry=Entry(dbroot,font=('Ruluko',18),bd=3,textvariable=hostvalue)
    hostentry.place(x=230,y=10)

    userentry = Entry(dbroot, font=('Ruluko', 18), bd=3, textvariable=uservalue)
    userentry.place(x=230, y=100)

    passwordentry = Entry(dbroot, font=('Ruluko', 18), bd=3, textvariable=passwordvalue)
    passwordentry.place(x=230, y=200)

    #-----------------------------------------------submit button
    submitbutton=Button(dbroot,text='Submit',font=('Ruluko',15,'bold'),bd=4,width=14,activebackground='lavender'
                        ,activeforeground='black',command=submitdb)
    submitbutton.place(x=145,y=250)

    dbroot.mainloop()
def tick():
    time_string= time.strftime('%H:%M:%S')
    date_string= time.strftime('%d/%m/%Y')
    clock.config(text='DATE:'+date_string+"\n"+"TIME:"+time_string,font=('BeautyDream',14,'bold'),relief=RIDGE)
    clock.after(200,tick)

##########################################################################################   INTRO
import random
colors=['blue','red','yellow']
def Introlablecolortick():
    fg=random.choice(colors)
    sliderlable.config(fg=fg)
    sliderlable.after(200,Introlablecolortick)
def Introlabletick():
    global count,text
    if(count>=len(ss)):
        count= 0
        text = ''
        sliderlable.config(text=text)
    else:
        text=text+ss[count]
        sliderlable.config(text=text)
        count+=1
    sliderlable.after(200,Introlabletick)

##############################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas
import time
global con,mycursor
root = Tk()
root.title('management system')
root.configure(bg='aqua')
root.geometry('1540x780+0+0')
root.iconbitmap('mini.ico')
root.resizable(False,False)
#############################################################################################  FRAMES
#--------------------------------------------------------------------------- option
frame1 = Frame(root,bg='powderblue',relief=RIDGE,borderwidth=4)
frame1.place(x=10,y=80,width=700,height=700)
frontlabel=Label(frame1,text='---------------What You Want To Do----------------',width='50',font=('Bistecca',20,'bold'),
                 bg='powderblue')
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(frame1,text='Add Name',width=25,font=('Codec Cold Italic',20,'bold'),bd=6,activebackground='white'
              ,activeforeground='black',command=addname)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(frame1,text='Search Name',width=25,font=('Codec Cold Italic',20,'bold'),bd=6,activebackground='white'
              ,activeforeground='black',command=searchname)
searchbtn.pack(side=TOP,expand=True)

updatebtn=Button(frame1,text='Update Name',width=25,font=('Codec Cold Italic',20,'bold'),bd=6,activebackground='white'
              ,activeforeground='black',command=updatename)
updatebtn.pack(side=TOP,expand=True)

deletebtn=Button(frame1,text='Delete Name',width=25,font=('Codec Cold Italic',20,'bold'),bd=6,activebackground='white'
              ,activeforeground='black',command=deletename)
deletebtn.pack(side=TOP,expand=True)

showbtn=Button(frame1,text='Show all Name',width=25,font=('Codec Cold Italic',20,'bold'),bd=6,activebackground='white'
              ,activeforeground='black',command=showname)
showbtn.pack(side=TOP,expand=True)

exportbtn=Button(frame1,text='Export Data',width=25,font=('Codec Cold Italic',20,'bold'),bd=6,activebackground='white'
              ,activeforeground='black',command=exportname)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(frame1,text='Exit',width=25,font=('Codec Cold Italic',20,'bold'),bd=6,activebackground='white'
              ,activeforeground='black',command=exitname)
exitbtn.pack(side=TOP,expand=True)
#-------------------------------------------------------------------------  seen
dataframe = Frame(root,bg='powderblue',relief=RIDGE,borderwidth=4)
dataframe.place(x=760,y=80,width=750,height=700)
#----------------------------------------------------    data frame
style=ttk.Style()
style.configure('Treeview.Heading',font=('Ruluko',15,'bold'),foreground='black',)
style.configure('Treeview',font=('Ruluko',15,'bold'),foreground='black',background='lavender')
scrollx=Scrollbar(dataframe,orient=HORIZONTAL)
scrolly=Scrollbar(dataframe,orient=VERTICAL)
table=Treeview(dataframe,columns=('Id','Name','Mobile no.','Email','Address','Gender','D.O.B','Added Date','Added Time'),
               yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=table.xview)
scrolly.config(command=table.yview)
table.heading('Id',text='Id')
table.heading('Name',text='Name')
table.heading('Mobile no.',text='Mobile no.')
table.heading('Email',text='Email')
table.heading('Address',text='Address')
table.heading('Gender',text='Gender')
table.heading('D.O.B',text='D.O.B')
table.heading('Added Date',text='Date')
table.heading('Added Time',text='Time')
table['show']='headings'
table.column('Id',width=200)
table.pack(fill=BOTH,expand=1)
#############################################################################################  SLIDER
ss= 'Welcome To Your Management System'
count=0
text=''
###############################################################################################
sliderlable = Label(root,text=ss,font=('CafeFrancoise',20,'bold'),relief=RIDGE,borderwidth=4,bg='lightskyblue')
sliderlable.place(x=500,y=10,width=570,height=50)
Introlabletick()
Introlablecolortick()
###############################################################################################  CLOCK
clock = Label(root,font=('BeautyDream',15,'bold'),relief=RIDGE,borderwidth=4,bg='lightskyblue')
clock.place(x=10,y=10,width=300,height=50)
tick()
#############################################################################################    DATABASE
connectbutton= Button(root,text='DATA STORAGE',width=23,font=('BeautyDream',15,'bold'),relief=RIDGE,borderwidth=5,
                      bg='lightsteelblue',activebackground='lavender',activeforeground='black',command=connectdb)
connectbutton.place(x=1200,y=10,width=300,height=50)
root.mainloop()