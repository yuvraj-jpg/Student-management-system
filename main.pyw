# function 
def heading():
    global count,text
    if count>=len(ss):
        count=-1
        text=''
        sliderlabel.config(text=text)
    else:
        text=text+ss[count]
        sliderlabel.config(text=text)
        count+=1
    sliderlabel.after(200,heading)
def tick():
    time1=time.strftime("%H:%M")
    date=time.strftime("%d/%m/%y")
    clock.config(text="Date : "+date+ "\n"+ "Time : "+time1)
    clock.after(200,tick)
def connect(): 
    def submit():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passval.get()
        # host='localhost'
        # user='root'
        # password=''
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notification','Data is Incorrect  Please Try Again  ')
            return
        try:
            strr='create database management'
            mycursor.execute(strr)
            strr='use management'
            mycursor.execute(strr)
            strr='create table student1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(10),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr) 
            strr='alter table student1 modify column id int not null'
            mycursor.execute(strr)
            strr='alter table student1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Connected to the Database',parent=dbox)
        except:
            strr='use management'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database',parent=dbox)
        dbox.destroy()
    dbox=Toplevel()
    dbox.grab_set()
    dbox.config(bg='blue')
    dbox.title("Databases connection")
    dbox.geometry('470x250+800+230')
    dbox.resizable(False,False)

    idlabel=Label(dbox,text="Enter host",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    idlabel.place(x=10,y=10)
    namelabel=Label(dbox,text="Enter username ",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    namelabel.place(x=10,y=70)
    passlabel=Label(dbox,text="Enter password",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    passlabel.place(x=10,y=130)
    
    hostval=StringVar() 
    userval=StringVar()
    passval=StringVar()

    hostentry=Entry(dbox,textvariable=hostval,font="roman 15 bold",bd=5)
    hostentry.place(x=250,y=10)

    userentry=Entry(dbox,textvariable=userval,font="roman 15 bold",bd=5)
    userentry.place(x=250,y=70)

    passentry=Entry(dbox,textvariable=passval,font="roman 15 bold",bd=5)
    passentry.place(x=250,y=130)

    submit=Button(dbox,text='Submit',font="roman 15 bold",bg='red',bd=5,width=20,activebackground='blue',activeforeground='white',command=submit)
    submit.place(x=150,y=190)
    dbox.mainloop()
def add():
    def submitadd():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get() 
        gender=genderval.get() 
        email=emailval.get()
        address=addressval.get()
        dob=dobval.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d/%m/%y")
         
        try:
            strr='insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,gender,email,address,dob,addedtime,addeddate))
            con.commit()
            res=messagebox.askyesnocancel('Notification','Id {} Name {} added sucessfully ... and want to clean form'.format(id,name),parent=addbox)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                genderval.set('')
                addressval.set('')
                emailval.set('')                
                dobval.set('')


        except:
            res=messagebox.askyesnocancel('Notification','Id {} Already Exist Try another'.format(id),parent=addbox)
        strr='select * from student1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

 
    
    addbox=Toplevel(master=dataentryframe1)
    addbox.grab_set()
    addbox.config(bg='green')
    addbox.title("ADD STUDENT")
    addbox.geometry('470x470+220+200')
    addbox.resizable(False,False)

    idlabel=Label(addbox,text="Enter ID :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    idlabel.place(x=10,y=10)
    namelabel=Label(addbox,text="Enter NAME :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    namelabel.place(x=10,y=70)
    mobilelabel=Label(addbox,text="Enter MOBILE :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    mobilelabel.place(x=10,y=130)
    emaillabel=Label(addbox,text="Enter EMAIL :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    emaillabel.place(x=10,y=190)
    addresslabel=Label(addbox,text="Enter ADDRESS :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    addresslabel.place(x=10,y=250)
    genderlabel=Label(addbox,text="Enter GENDER :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    genderlabel.place(x=10,y=310)
    doblabel=Label(addbox,text="Enter D.O.B :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    doblabel.place(x=10,y=370)
    
    idval=StringVar() 
    nameval=StringVar()
    mobileval=StringVar()
    genderval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    dobval=StringVar()

    identry=Entry(addbox,textvariable=idval,font="roman 15 bold",bd=5)
    identry.place(x=250,y=10) 

    nameentry=Entry(addbox,textvariable=nameval,font="roman 15 bold",bd=5)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(addbox,textvariable=mobileval,font="roman 15 bold",bd=5)
    mobileentry.place(x=250,y=130)

    genderentry=Entry(addbox,textvariable=genderval,font="roman 15 bold",bd=5)
    genderentry.place(x=250,y=190)

    emailentry=Entry(addbox,textvariable=emailval,font="roman 15 bold",bd=5)
    emailentry.place(x=250,y=250)

    addressentry=Entry(addbox,textvariable=addressval,font="roman 15 bold",bd=5)
    addressentry.place(x=250,y=310)

    dobentry=Entry(addbox,textvariable=dobval,font="roman 15 bold",bd=5)
    dobentry.place(x=250,y=370)

    submit=Button(addbox,text='Submit',font="roman 15 bold",bg='red',bd=5,width=20,activebackground='blue',activeforeground='white',command=submitadd)
    submit.place(x=150,y=420)
    addbox.mainloop()
def search():
    def searchbtn():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get() 
        gender=genderval.get() 
        email=emailval.get()
        address=addressval.get()
        dob=dobval.get()
        addeddate=time.strftime("%d/%m/%y")
        if id!='':
            strr='select * from student1 where id =%s'
            mycursor.execute(strr,id)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif name!='':
            strr='select * from student1 where name =%s'
            mycursor.execute(strr,name)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif mobile!='':
            strr='select * from student1 where mobile =%s'
            mycursor.execute(strr,mobile)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif email!='':
            strr='select * from student1 where email =%s'
            mycursor.execute(strr,email)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif address!='':
            strr='select * from student1 where address =%s'
            mycursor.execute(strr,address)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif gender!='':
            strr='select * from student1 where gender =%s'
            mycursor.execute(strr,gender)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
        elif dob!='':
            strr='select * from student1 where dob =%s'
            mycursor.execute(strr,dob)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)    
        elif addeddate!='':
            strr='select * from student1 where addeddate =%s'
            mycursor.execute(strr,addeddate)
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)



    searchbox=Toplevel(master=dataentryframe1)
    searchbox.grab_set()
    searchbox.config(bg='green')
    searchbox.title("SEARCH STUDENT")
    searchbox.geometry('470x540+220+200')
    searchbox.resizable(False,False)

    idlabel=Label(searchbox,text="Enter ID :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    idlabel.place(x=10,y=10)
    namelabel=Label(searchbox,text="Enter NAME :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    namelabel.place(x=10,y=70)
    mobilelabel=Label(searchbox,text="Enter MOBILE :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    mobilelabel.place(x=10,y=130)
    emaillabel=Label(searchbox,text="Enter EMAIL :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    emaillabel.place(x=10,y=190)
    addresslabel=Label(searchbox,text="Enter ADDRESS :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    addresslabel.place(x=10,y=250)
    genderlabel=Label(searchbox,text="Enter GENDER :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    genderlabel.place(x=10,y=310)
    doblabel=Label(searchbox,text="Enter D.O.B :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    doblabel.place(x=10,y=370)
    datelabel=Label(searchbox,text="Enter DATE :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=13,anchor=W)
    datelabel.place(x=10,y=370)    
    idval=StringVar() 
    nameval=StringVar()
    mobileval=StringVar()
    genderval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    dobval=StringVar()
    dateval=StringVar()

    identry=Entry(searchbox,textvariable=idval,font="roman 15 bold",bd=5)
    identry.place(x=250,y=10) 

    nameentry=Entry(searchbox,textvariable=nameval,font="roman 15 bold",bd=5)
    nameentry.place(x=250,y=70)
 
    mobileentry=Entry(searchbox,textvariable=mobileval,font="roman 15 bold",bd=5)
    mobileentry.place(x=250,y=130)

    genderentry=Entry(searchbox,textvariable=genderval,font="roman 15 bold",bd=5)
    genderentry.place(x=250,y=190)

    emailentry=Entry(searchbox,textvariable=emailval,font="roman 15 bold",bd=5)
    emailentry.place(x=250,y=250)

    addressentry=Entry(searchbox,textvariable=addressval,font="roman 15 bold",bd=5)
    addressentry.place(x=250,y=310)

    dobentry=Entry(searchbox,textvariable=dobval,font="roman 15 bold",bd=5)
    dobentry.place(x=250,y=370)

    dateentry=Entry(searchbox,textvariable=dateval,font="roman 15 bold",bd=5)
    dateentry.place(x=250,y=370)

    submit=Button(searchbox,text='Submit',font="roman 15 bold",bg='red',bd=5,width=20,activebackground='blue',activeforeground='white',command=searchbtn)
    submit.place(x=150,y=480)
    searchbox.mainloop()
def delete():
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values'][0]
    strr='delete from student1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','ID {} Deleted succesfully'.format(pp))
    strr='select * from student1 '
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)
def update():
    def updatebtn():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update student1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updatebox)
        strr = 'select *from student1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)


    updatebox=Toplevel(master=dataentryframe1)
    updatebox.grab_set()
    updatebox.config(bg='green')
    updatebox.title("UPDATE STUDENT")
    updatebox.geometry('470x585+220+160')
    updatebox.resizable(False,False)

    idlabel=Label(updatebox,text="Enter ID :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    idlabel.place(x=10,y=10)
    namelabel=Label(updatebox,text="Enter NAME :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    namelabel.place(x=10,y=70)
    mobilelabel=Label(updatebox,text="Enter MOBILE :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    mobilelabel.place(x=10,y=130)
    emaillabel=Label(updatebox,text="Enter EMAIL :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    emaillabel.place(x=10,y=190)
    addresslabel=Label(updatebox,text="Enter ADDRESS :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    addresslabel.place(x=10,y=250)
    genderlabel=Label(updatebox,text="Enter GENDER :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    genderlabel.place(x=10,y=310)
    doblabel=Label(updatebox,text="Enter D.O.B :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    doblabel.place(x=10,y=370)
    datelabel=Label(updatebox,text="Enter DATE :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    datelabel.place(x=10,y=430)   
    timelabel=Label(updatebox,text="Update TIME :",bg='gold2',font="times 20 bold",relief=SUNKEN,borderwidth=3,width=12,anchor=W)
    timelabel.place(x=10,y=490)   

    idval=StringVar() 
    nameval=StringVar()
    mobileval=StringVar()
    genderval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()


    identry=Entry(updatebox,textvariable=idval,font="roman 15 bold",bd=5)
    identry.place(x=250,y=10) 

    nameentry=Entry(updatebox,textvariable=nameval,font="roman 15 bold",bd=5)
    nameentry.place(x=250,y=70)
 
    mobileentry=Entry(updatebox,textvariable=mobileval,font="roman 15 bold",bd=5)
    mobileentry.place(x=250,y=130)

    genderentry=Entry(updatebox,textvariable=genderval,font="roman 15 bold",bd=5)
    genderentry.place(x=250,y=190)

    emailentry=Entry(updatebox,textvariable=emailval,font="roman 15 bold",bd=5)
    emailentry.place(x=250,y=250)

    addressentry=Entry(updatebox,textvariable=addressval,font="roman 15 bold",bd=5)
    addressentry.place(x=250,y=310)

    dobentry=Entry(updatebox,textvariable=dobval,font="roman 15 bold",bd=5)
    dobentry.place(x=250,y=370)

    dateentry=Entry(updatebox,textvariable=dateval,font="roman 15 bold",bd=5)
    dateentry.place(x=250,y=430)

    updatedateentry=Entry(updatebox,textvariable=timeval,font="roman 15 bold",bd=5)
    updatedateentry.place(x=250,y=490)

    submit=Button(updatebox,text='Submit',font="roman 15 bold",bg='red',bd=5,width=20,activebackground='blue',activeforeground='white',command=updatebtn)
    submit.place(x=150,y=540)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updatebox.mainloop()
def show(): 
    strr='select * from student1 '
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert('',END,values=vv)
def export():
    ff=filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studenttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['Id','NAME','MOBILE','Email','ADDRESS','GENDER','DOB','ADDED DATE','ADDED TIME']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications','Student data is saved to {}'.format(paths))
def exit():
    res=messagebox.askyesnocancel('Notification','Do You Want To Exit')
    if res==True:
        box.destroy()
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas   
import time


box=Tk()
box.title('Student Management System')
box.config(bg='green3')
box.iconbitmap('icon.ico')
box.geometry('1400x700+200+50')
box.resizable(False,False)
    
# frame
dataentryframe1=Frame(box,bg="white",relief=SUNKEN,borderwidth=5)
dataentryframe1.place(x=20,y=80,width=500,height=600)
# dataentryframe 1 mwthod and buttons
frontlabel=Label(dataentryframe1,text="Welcome",width=30,font="arial 22 bold",bg="green3")
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(dataentryframe1,text="1. ADD STUDENT ",width=25,font="arial 20 bold",bd=6,bg="skyblue",relief=RIDGE,activebackground='blue',activeforeground='white',command=add)
addbtn.pack(side=TOP,expand=True)
searchbtn=Button(dataentryframe1,text="2.  SEARCH STUDENT ",width=25,font="arial 20 bold",bd=6,bg="skyblue",relief=RIDGE,activebackground='blue',activeforeground='white',command=search)
searchbtn.pack(side=TOP,expand=True)
deletebtn=Button(dataentryframe1,text="3. DELETE STUDENT ",width=25,font="arial 20 bold",bd=6,bg="skyblue",relief=RIDGE,activebackground='blue',activeforeground='white',command=delete)
deletebtn.pack(side=TOP,expand=True)
updatebtn=Button(dataentryframe1,text="4. UPDATE STUDENT ",width=25,font="arial 20 bold",bd=6,bg="skyblue",relief=RIDGE,activebackground='blue',activeforeground='white',command=update)
updatebtn.pack(side=TOP,expand=True)
showbtn=Button(dataentryframe1,text="5. SHOW ALL ",width=25,font="arial 20 bold",bd=6,bg="skyblue",relief=RIDGE,activebackground='blue',activeforeground='white',command=show)
showbtn.pack(side=TOP,expand=True)
exportbtn=Button(dataentryframe1,text="6. EXPORT DATA ",width=25,font="arial 20 bold",bd=6,bg="skyblue",relief=RIDGE,activebackground='blue',activeforeground='white',command=export)
exportbtn.pack(side=TOP,expand=True)
exitbtn=Button(dataentryframe1,text="7. EXIT ",width=25,font="arial 20 bold",bd=6,bg="skyblue",relief=RIDGE,activebackground='blue',activeforeground='white',command=exit)
exitbtn.pack(side=TOP,expand=True)
#frame 2
style=ttk.Style()
style.configure('Treeview.Heading',font="timesroman 15 bold",foreground='blue')
style.configure('Treeview',font="timesroman 15 bold",background='cyan',foreground='black')
dataentryframe2=Frame(box,bg="white",relief=SUNKEN,borderwidth=5)
dataentryframe2.place(x=750,y=80,width=620,height=600)

scroll_x=Scrollbar(dataentryframe2,orient=HORIZONTAL)
scroll_y=Scrollbar(dataentryframe2,orient=VERTICAL)

studenttable=Treeview(dataentryframe2,column=('Id','Name','Mobile No.','Email','Address','Gender','D.O.B','Added date','Added time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added date',text='Added date')
studenttable.heading('Added time',text='Added time')
studenttable['show']='headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=100)
studenttable.column('Mobile No.',width=100)
studenttable.column('Email',width=100)
studenttable.column('Address',width=100)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=100)
studenttable.column('Added date',width=100)
studenttable.column('Added time',width=100)
# studenttable.pack(fill=BOTH,expand=1)
# heading
ss="STUDENT MANAGEMENT SYSTEM "
count=0
text=''
sliderlabel=Label(box,text=ss,font="timesroman 30 bold",relief=RIDGE,borderwidth=4,width=30,bg='cyan')
sliderlabel.place(x=300,y=0)
# clock
clock=Label(box,font="timesroman 14 bold",relief=RIDGE,borderwidth=4)
clock.place(x=0,y=0)
tick()
#database connect button
connectbutton=Button(box,text='Connect to Database',font="timesroman 15 bold",relief=RIDGE,borderwidth=4,width=23,bg='cyan',command=connect)
connectbutton.place(x=1130,y=0)
heading()
box.mainloop()