############################################Add Student#########################################-#
def addstudent():
    def SUBMITTED():
        id = idval.get()
        Name = Nameval.get()
        Course = Courseval.get()
        Branch = Branchval.get()
        Mobile = Mobileval.get()
        Email = Emailval.get()
        Gender = Genderval.get()
        DOB = DOBval.get()
        Address = Addressval.get()
        Addedtime = time.strftime("%H:%M:%S")
        Addeddate = time.strftime("%d:%m:%y")
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,Name,Course,Branch,Mobile,Email,Gender,DOB,Address,Addedtime,Addeddate))
            con.commit() # Commit are use to access changes in database
            res = messagebox.askyesnocancel('Notification','Id {} Name {} Added Successfully... and want to clean the form'.format(id,Name),parent=addroot)
            if(res==True):
                idval.set('')
                Nameval.set('')
                Courseval.set('')
                Branchval.set('')
                Mobileval.set('')
                Emailval.set('')
                Genderval.set('')
                DOBval.set('')
                Addressval.set('')
        except:
            messagebox.showerror('Notification','Id already exist try another id...',parent=addroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]]
            studenttable.insert('',END,values=vv)
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.title('Student Entries')
    addroot.config(bg='light green')
    addroot.geometry("450x550+300+70")
    addroot.iconbitmap('Enteries image.ico')
    addroot.resizable(0,0)
#---------------------------------------Add student Label-----------------------------------------------#
    idlabel = Label(addroot,text='Enter ID :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=15)
    Namelabel = Label(addroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=12, anchor='w')
    Namelabel.place(x=10, y=70)
    Courselabel = Label(addroot, text='Course :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3,width=12, anchor='w')
    Courselabel.place(x=10, y=125)
    Branchlabel = Label(addroot, text='Branch :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    Branchlabel.place(x=10, y=185)
    Mobilelabel = Label(addroot, text='Mobile No :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3,width=12, anchor='w')
    Mobilelabel.place(x=10, y=240)
    Emaillabel = Label(addroot, text='Enter Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    Emaillabel.place(x=10, y=295)
    Genderlabel = Label(addroot, text='GENDER :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    Genderlabel.place(x=10, y=350)
    DOBlabel = Label(addroot, text='DOB :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    DOBlabel.place(x=10, y=405)
    Addresslabel = Label(addroot, text='Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    Addresslabel.place(x=10, y=460)
#-----------------------------------------For Getting Add Student DAta-----------------------------------------#
    idval = StringVar()
    Nameval = StringVar()
    Courseval = StringVar()
    Branchval = StringVar()
    Mobileval = StringVar()
    Emailval = StringVar()
    Genderval = StringVar()
    DOBval = StringVar()
    Addressval = StringVar()
    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,width=20,textvariable=idval)
    identry.place(x=228,y=17)
    Nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Nameval)
    Nameentry.place(x=228, y=72)
    Courseentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Courseval)
    Courseentry.place(x=228, y=127)
    Branchentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Branchval)
    Branchentry.place(x=228, y=182)
    Mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Mobileval)
    Mobileentry.place(x=228, y=237)
    Emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,width=20,textvariable=Emailval)
    Emailentry.place(x=228,y=295)
    Genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Genderval)
    Genderentry.place(x=228, y=350)
    DOBentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=DOBval)
    DOBentry.place(x=228, y=410)
    Addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Addressval)
    Addressentry.place(x=228, y=460)
#--------------------------------------------Submit Btn---------------------------------------------------------------#
    SubmitBtn = Button(addroot,text='SUBMIT',font=('roman',12,'bold'),bg='red',relief=RAISED,width=14,bd=5,activebackground='Blue',
                       activeforeground='white',command=SUBMITTED)
    SubmitBtn.place(x=160,y=505)
    addroot.mainloop()

######################################### Search Student ###########################################################
def searchstudent():
    def search():
        id = idval.get()
        Name = Nameval.get()
        Course = Courseval.get()
        Branch = Branchval.get()
        Mobile = Mobileval.get()
        Email = Emailval.get()
        Gender = Genderval.get()
        DOB = DOBval.get()
        Address = Addressval.get()
        Addeddate = time.strftime("%d:%m:%y")
        if(id != ''):
            strr = 'select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (Name != ''):
            strr = 'select * from studentdata where Name=%s'
            mycursor.execute(strr, (Name))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (Course != ''):
            strr = 'select * from studentdata where Course=%s'
            mycursor.execute(strr, (Course))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (Branch != ''):
            strr = 'select * from studentdata where Branch=%s'
            mycursor.execute(strr, (Branch))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (Mobile != ''):
            strr = 'select * from studentdata where Mobile=%s'
            mycursor.execute(strr, (Mobile))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (Email != ''):
            strr = 'select * from studentdata where Email=%s'
            mycursor.execute(strr, (Email))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (Gender != ''):
            strr = 'select * from studentdata where Gender=%s'
            mycursor.execute(strr, (Gender))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (DOB != ''):
            strr = 'select * from studentdata where DOB=%s'
            mycursor.execute(strr, (DOB))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (Address != ''):
            strr = 'select * from studentdata where Address=%s'
            mycursor.execute(strr, (Address))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
        elif (Addeddate != ''):
            strr = 'select * from studentdata where Addeddate=%s'
            mycursor.execute(strr, (Addeddate))
            datas = mycursor.fetchall()
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
                studenttable.insert('', END, values=vv)
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.title('Search Student')
    searchroot.config(bg='light green')
    searchroot.geometry("450x610+300+10")
    searchroot.iconbitmap('Search imgae.ico')
    searchroot.resizable(0,0)
#-------------------------------------------- Add student Label ----------------------------------------------------#
    idlabel = Label(searchroot,text='Enter ID :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=15)
    NAmelabel = Label(searchroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    NAmelabel.place(x=10, y=70)
    Courselabel = Label(searchroot, text='Course :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,width=12, anchor='w')
    Courselabel.place(x=10, y=125)
    Branchlabel = Label(searchroot, text='Branch :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    Branchlabel.place(x=10, y=185)
    Mobilelabel = Label(searchroot, text='Mobile No :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,width=12, anchor='w')
    Mobilelabel.place(x=10, y=240)
    Emaillabel = Label(searchroot, text='Enter Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    Emaillabel.place(x=10, y=295)
    Genderlabel = Label(searchroot, text='GENDER :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    Genderlabel.place(x=10, y=350)
    DOBlabel = Label(searchroot, text='DOB :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    DOBlabel.place(x=10, y=405)
    Addresslabel = Label(searchroot, text='Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    Addresslabel.place(x=10, y=460)
    Datelabel = Label(searchroot, text='Date :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    Datelabel.place(x=10, y=515)
#--------------------------------For Getting Search Student DAta-----------------------------#
    idval = StringVar()
    Nameval = StringVar()
    Courseval = StringVar()
    Branchval = StringVar()
    Mobileval = StringVar()
    Emailval = StringVar()
    Genderval = StringVar()
    DOBval = StringVar()
    Addressval = StringVar()
    Dateval = StringVar()
    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,width=20,textvariable=idval)
    identry.place(x=228,y=17)
    Nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Nameval)
    Nameentry.place(x=228, y=72)
    Courseentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Courseval)
    Courseentry.place(x=228, y=127)
    Branchentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Branchval)
    Branchentry.place(x=228, y=182)
    Mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Mobileval)
    Mobileentry.place(x=228, y=237)
    Emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,width=20,textvariable=Emailval)
    Emailentry.place(x=228,y=295)
    Genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Genderval)
    Genderentry.place(x=228, y=350)
    DOBentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=DOBval)
    DOBentry.place(x=228, y=410)
    Addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Addressval)
    Addressentry.place(x=228, y=460)
    Dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Dateval)
    Dateentry.place(x=228, y=515)
#-----------------------------------Submit Btn-------------------------------------------------------#
    SubmitBtn = Button(searchroot,text='SUBMIT',font=('roman',12,'bold'),bg='red',relief=RAISED,width=14,bd=5,activebackground='Blue',
                       activeforeground='white',command=search)
    SubmitBtn.place(x=160,y=560)

################################# Delete Student ##########################################################
def deletestudent():
    cc = studenttable.focus() # search value and focus on variable
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','Id {} deleted successfully...'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
        studenttable.insert('', END, values=vv)

########################################### Update Student ###########################################################
def updatestudent():
    def update():
        id = idval.get()
        Name = Nameval.get()
        Course = Courseval.get()
        Branch = Branchval.get()
        Mobile = Mobileval.get()
        Email = Emailval.get()
        Gender = Genderval.get()
        DOB = DOBval.get()
        Address = Addressval.get()
        timee = Dateval.get()
        date = Timeval.get()

        strr = 'update studentdata set Name=%s,Course=%s,Branch=%s,Mobile=%s,Email=%s,Gender=%s,DOB=%s,Address=%s,time=%s,date=%s where id=%s'
        mycursor.execute(strr,(Name,Course,Branch,Mobile,Email,Gender,DOB,Address,timee,date,id))
        con.commit()
        messagebox.showinfo('Notification','Id {} updated successfully'.format(id))
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
            studenttable.insert('', END, values=vv)
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.title('Update Details ')
    updateroot.config(bg='light green')
    updateroot.geometry("450x640+300+0")
    updateroot.iconbitmap('Update image.ico')
    updateroot.resizable(0,0)
#---------------------------------- Update student Label ---------------------------------------------#
    idlabel = Label(updateroot,text='Enter ID :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=15)
    NAmelabel = Label(updateroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    NAmelabel.place(x=10, y=70)
    Courselabel = Label(updateroot, text='Course :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,width=12, anchor='w')
    Courselabel.place(x=10, y=125)
    Branchlabel = Label(updateroot, text='Branch :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    Branchlabel.place(x=10, y=185)
    Mobilelabel = Label(updateroot, text='Mobile No :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3,width=12, anchor='w')
    Mobilelabel.place(x=10, y=240)
    Emaillabel = Label(updateroot, text='Enter Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    Emaillabel.place(x=10, y=295)
    Genderlabel = Label(updateroot, text='GENDER :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    Genderlabel.place(x=10, y=350)
    DOBlabel = Label(updateroot, text='DOB :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    DOBlabel.place(x=10, y=405)
    Addresslabel = Label(updateroot, text='Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    Addresslabel.place(x=10, y=460)
    Datelabel = Label(updateroot, text='Date :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    Datelabel.place(x=10, y=515)
    Timelabel = Label(updateroot, text='Time :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    Timelabel.place(x=10, y=565)
#---------------------------------------- For Getting Update Student DAta ----------------------------------------#
    idval = StringVar()
    Nameval = StringVar()
    Courseval = StringVar()
    Branchval = StringVar()
    Mobileval = StringVar()
    Emailval = StringVar()
    Genderval = StringVar()
    DOBval = StringVar()
    Addressval = StringVar()
    Dateval = StringVar()
    Timeval = StringVar()
    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,width=20,textvariable=idval)
    identry.place(x=228,y=17)
    Nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Nameval)
    Nameentry.place(x=228, y=72)
    Courseentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Courseval)
    Courseentry.place(x=228, y=127)
    Branchentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Branchval)
    Branchentry.place(x=228, y=182)
    Mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Mobileval)
    Mobileentry.place(x=228, y=237)
    Emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,width=20,textvariable=Emailval)
    Emailentry.place(x=228,y=295)
    Genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Genderval)
    Genderentry.place(x=228, y=350)
    DOBentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=DOBval)
    DOBentry.place(x=228, y=410)
    Addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Addressval)
    Addressentry.place(x=228, y=460)
    Dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Dateval)
    Dateentry.place(x=228, y=515)
    Timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, width=20, textvariable=Timeval)
    Timeentry.place(x=228, y=565)
#---------------------------------- Submit Btn ------------------------------------------------------#
    SubmitBtn = Button(updateroot,text='SUBMIT',font=('roman',12,'bold'),bg='red',relief=RAISED,width=10,bd=5,activebackground='Blue',
                       activeforeground='white',command=update)
    SubmitBtn.place(x=160,y=605)
#--------------------------------Changes in previous value -------------------------------------------#
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        Nameval.set(pp[1])
        Courseval.set(pp[2])
        Branchval.set(pp[3])
        Mobileval.set(pp[4])
        Emailval.set(pp[5])
        Genderval.set(pp[6])
        DOBval.set(pp[7])
        Addressval.set(pp[8])
        Dateval.set(pp[9])
        Timeval.set(pp[10])
        updateroot.mainloop()

#################################################### Show All #################################################
def showallstudent():
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
        studenttable.insert('', END, values=vv)

########################################### Export Data ##########################################################
def exportdata():
    ff = filedialog.asksaveasfilename() #Filedialog is a moulde to deal with files
    gg = studenttable.get_children()
    id,Name,Course,Branch,MobileNo,Emailid,Gender,DOB,Address,AddedDate,AddedTime=[],[],[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),Name.append(pp[1]),Course.append(pp[2]),Branch.append(pp[3]),MobileNo.append(pp[4]),Emailid.append(pp[5]),Gender.append(pp[6]),
        DOB.append(pp[7]),Address.append(pp[8]),AddedDate.append(pp[9]),AddedTime.append(pp[10])
    dd = ['id','Name','Course','Branch','MobileNo','Emailid','Gender','DOB','Address','AddedDate','AddedTime']
    df = pandas.DataFrame(list(zip(id,Name,Course,Branch,MobileNo,Emailid,Gender,DOB,Address,AddedDate,AddedTime)),columns=dd) #Pandas is module of datascience to use to create dataset
    path = r'{}.csv'.format(ff) #For create a csv file
    df.to_csv(path,index=False)
    messagebox.showinfo('Notification','Student Data Saved'.format(path))

##################################### Exit Button ##################################################################
def exit():
    ext = messagebox.askyesnocancel('notification','Do You Want to exit?')
    if (ext==True):
        root.destroy()

#----------------------------------Connect to Database----------------------------------------------------------#
def connectdb():
    def submitdb():
        global con,mycursor
        host = hostVal.get()
        user = UserVal.get()
        password = passwordVal.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password) #Accept only user database id and password
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Incorrect! please try again')
            return
        try:
            strr = 'create database Administrationsystem'
            mycursor.execute(strr)
            strr = 'use Administrationsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int(20),Name varchar(30),course varchar(20),Branch varchar(20),Mobile varchar(10),Email varchar(20),Gender varchar(10),DOB varchar(10),Address varchar(30),Time varchar(40),Date varchar(40))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created now you are connected...', parent=dbroot)
        except:
            strr = 'use Administrationsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now You Are Connected To The Database.....',parent=dbroot)
            dbroot.destroy()
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.title("Admin credentials")
    dbroot.geometry("450x330+670+180")
    dbroot.config(bg='Brown')
    dbroot.iconbitmap('Admin image.ico')
    dbroot.resizable(0,0)

###################################### Create Admin Cradetials option ####################################
    hostlabel = Label(dbroot,text="Enter Host :",bg='gold2',font=('times',22,'bold'),
               relief=GROOVE,borderwidth=3,width=10,anchor='w')
    hostlabel.place(x=20,y=40)
    Userlabel = Label(dbroot,text="User ID:", bg='gold2', font=('times',22, 'bold'),
               relief=GROOVE, borderwidth=3, width=10,anchor='w')
    Userlabel.place(x=20,y=110)
    Password = Label(dbroot, text="Password:", bg='gold2', font=('times',22,'bold'),
               relief=GROOVE, borderwidth=3, width=10,anchor='w')
    Password.place(x=20,y=180)
#---------------------------------------Admin Options-----------------------------------------------------#
    hostVal = StringVar()
    UserVal = StringVar()
    passwordVal = StringVar()
    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=6,textvariable=hostVal)
    hostentry.place(x=220,y=40)
    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=6, textvariable=UserVal)
    userentry.place(x=220, y=110)
    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=6, textvariable=passwordVal)
    passwordentry.place(x=220, y=180)
    Submit = Button(dbroot,text='SUBMIT',font=('roman',15,'bold'),bg='green',bd=5,width=20,
                    activebackground='pink',activeforeground='white',command=submitdb)
    Submit.place(x=140,y=250)
    dbroot.mainloop()

#-------------------------------Date Time-------------------------------------------------------------#
def Tick():
    time_string = time.strftime("%H/%M/%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Time :'+time_string+"\n"+"Date :"+date_string)
    clock.after(200,Tick)
#-------------------------------Live running status of Datetime ----------------------------------------#
def IntrolabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        sliderlabel.config(text=text)
    else:
        text = text+ss[count]
        sliderlabel.config(text=text)
        count += 1
    sliderlabel.after(155,IntrolabelTick)

##################################### Import Files #########################################################
from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
import pandas
import pymysql
import time
root = Tk()
root.title("RKGIT ADMISSION CELL")
root.config(bg='wheat')
root.geometry("1100x635+90+0")
root.iconbitmap("RKGIT_logo.ico")
root.resizable(0,0)

#####################################################Data Entry Frames ###############################################
DataEntry = Frame(root,bg='aquamarine',relief=GROOVE,borderwidth=10)
DataEntry.place(x=5,y=130,width=400,height=500)
#-------------------------------------Data Entry Frame---------------------------------------#
DataEntryFrame = Label(DataEntry,text='-----------------Student Details-----------------',bg='aquamarine',
                       width=30,font=('arial',16,'italic bold'))
DataEntryFrame.pack(side=TOP,expand=True)
AddBtn = Button(DataEntry,text='1. Add Student',width=20,font=('Roman',14,'bold'),bd=6,bg='blue',
                activebackground='orange',relief=GROOVE,activeforeground='white',command=addstudent)
AddBtn.pack(side=TOP,expand=True)
searchstudent = Button(DataEntry,text='2. Search Student',width=20,font=('Roman',14,'bold'),bd=6,bg='blue'
                ,activebackground='orange',relief=GROOVE,activeforeground='white',command=searchstudent)
searchstudent.pack(side=TOP,expand=True)
DeleteBtn = Button(DataEntry,text='3. Delete Student',width=20,font=('Roman',14,'bold'),bd=6,bg='blue',
                activebackground='orange',relief=GROOVE,activeforeground='white',command=deletestudent)
DeleteBtn.pack(side=TOP,expand=True)
UpdateBtn = Button(DataEntry,text='4. Update Student',width=20,font=('Roman',14,'bold'),bd=6,bg='blue',
                activebackground='orange',relief=GROOVE,activeforeground='white',command=updatestudent)
UpdateBtn.pack(side=TOP,expand=True)
showallBtn = Button(DataEntry,text='5. Show All',width=20,font=('Roman',14,'bold'),bd=6,bg='blue',
                activebackground='orange',relief=GROOVE,activeforeground='white',command=showallstudent)
showallBtn.pack(side=TOP,expand=True)
exportdatabtn = Button(DataEntry,text='6. Export Data',width=20,font=('Roman',14,'bold'),bd=6,bg='blue',
                activebackground='orange',relief=GROOVE,activeforeground='white',command=exportdata)
exportdatabtn.pack(side=TOP,expand=True)
exitbtn = Button(DataEntry,text='7. Exit',width=20,font=('Roman',14,'bold'),bd=6,bg='blue',
                activebackground='orange',relief=GROOVE,activeforeground='white',command=exit)
exitbtn.pack(side=TOP,expand=True)

################################################### Show Data Frame ##################################################
ShowDataFrame = Frame(root,bg='aquamarine',relie=GROOVE,borderwidth=10)
ShowDataFrame.place(x=495,y=130,width=600,height=500)
#---------------------------------Show Data Frame----------------------------------------#
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('ID','Name','Course','Branch','Mobile No','E mail'
    ,'Gender','DOB','Address','Added Time','Added Date'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Course',text='Course')
studenttable.heading('Branch',text='Branch')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('E mail',text='Email ID')
studenttable.heading('Gender',text='Gender')
studenttable.heading('Address',text='Address')
studenttable.heading('DOB',text='DOB')
studenttable.heading('Added Time',text='Added Time')
studenttable.heading('Added Date',text='Added Date')
studenttable['show'] = 'headings'
studenttable.column('ID',width=100)
studenttable.pack(fill=BOTH,expand=1)

############################################## Slider ################################################################
ss = 'Welcome to RKGIT Admin Cell'
count = 0
text = ''
sliderlabel = Label(root,text=ss,relief=RIDGE,font=('Times',30,'bold'),borderwidth=4,
                    width=28,bg='yellow',fg='red')
sliderlabel.place(x=260,y=0)
IntrolabelTick()

############################################## Clock ##################################################################
clock = Label(root,font=('Times',14,'bold'),relief=RIDGE,borderwidth=4,width=15,bg='gold2')
clock.place(x=0,y=0)
Tick()

############################################ DataBAse Button #################3########################################
ConnectDataBase = Button(root,text='Connect to Database',width=30,font=('Times',14,'bold'),
                         relief=RIDGE,borderwidth=3,bg='light green',activebackground='Sky blue',
                         activeforeground='red',command=connectdb)
ConnectDataBase.place(x=630,y=80)
root.mainloop()