# -*- coding:UTF-8 -*-
import pymssql
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sys
a = 0


def updateGlobal(b):
    global a
    a = b


def delButton(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)


# 各窗体定义
# 登录界面
windows = tk.Tk()
windows.title('高校成绩管理数据库系统登录窗口')
windows.geometry('600x500+510+150')

# 学生界面
windowsS = tk.Toplevel()
windowsS.title('学生界面')
windowsS.geometry('900x700+350+80')
windowsS.withdraw()

# 教师界面
windowsT = tk.Toplevel()
windowsT.title('教师界面')
windowsT.geometry('900x700+350+80')
windowsT.withdraw()

# 教务处界面
windowsD = tk.Toplevel()
windowsD.title('教务处界面')
windowsD.geometry('600x512+510+150')
windowsD.withdraw()
windowsD.configure(bg='white')

windowsDS = tk.Toplevel()
windowsDS.title('学生信息管理')
windowsDS.geometry('700x600+460+130')
windowsDS.withdraw()

windowsDT = tk.Toplevel()
windowsDT.title('教师信息管理')
windowsDT.geometry('700x600+460+130')
windowsDT.withdraw()

windowsDA = tk.Toplevel()
windowsDA.title('地区信息统计')
windowsDA.geometry('700x600+460+130')
windowsDA.configure(bg='white')
windowsDA.withdraw()


def End():
    s = tkinter.messagebox.askquestion(title='警告',
                                       message='您点击了关闭按钮,进程即将结束',
                                       default="no",
                                       icon="warning")
    if s == 'yes':
        sys.exit(0)


windows.protocol("WM_DELETE_WINDOW", End)
windowsT.protocol("WM_DELETE_WINDOW", End)
windowsS.protocol("WM_DELETE_WINDOW", End)
windowsD.protocol("WM_DELETE_WINDOW", End)
windowsDA.protocol("WM_DELETE_WINDOW", End)
windowsDT.protocol("WM_DELETE_WINDOW", End)
windowsDS.protocol("WM_DELETE_WINDOW", End)


# 登录界面控件
def get_login():
    global user
    global number
    number = e1.get()
    password = e2.get()

    user = comb.get()
    flag = 1

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    if user != '教务处':
        # 学生登录
        if user == '学生':
            cursor.execute("select chr_学生账号01 from Chenhr_学生登录01")
            while (True):
                data = cursor.fetchone()
                if data == None:
                    tk.messagebox.showerror(title='Error',
                                            message='您输入的账号不存在!')
                    comb.mainloop()
                    flag = 0
                    break
                if data[0] == number:
                    break
            if flag:
                cursor.execute(
                    f"select chr_学生密码01 from Chenhr_学生登录01 where chr_学生账号01 = {number}"
                )
                while (True):
                    data = cursor.fetchone()
                    if data == None:
                        tk.messagebox.showerror(title='Error',
                                                message='您输入的密码有误，请重新输入')
                        comb.mainloop()
                        break
                    if data[0] == password:
                        tk.messagebox.showinfo(title='Hello',
                                               message='欢迎进入学生管理系统')
                        windows.withdraw()
                        windowsS.deiconify()
                        break

        # 教师登录
        else:
            cursor.execute("select chr_教师账号01 from Chenhr_教师登录01")
            while (True):
                data = cursor.fetchone()
                if data == None:
                    tk.messagebox.showerror(title='Error',
                                            message='您输入的账号不存在!')
                    comb.mainloop()
                    flag = 0
                    break
                if data[0] == number:
                    break
            if flag:
                cursor.execute(
                    f"select chr_教师密码01 from Chenhr_教师登录01 where chr_教师账号01 = {number}"
                )
                while (True):
                    data = cursor.fetchone()
                    if data == None:
                        tk.messagebox.showerror(title='Error',
                                                message='您输入的密码有误，请重新输入')
                        comb.mainloop()
                        break
                    if data[0] == password:
                        tk.messagebox.showinfo(title='Hello',
                                               message='欢迎进入学生管理系统')
                        windows.withdraw()
                        windowsT.deiconify()
                        break

    # 教务处(管理员)登录
    else:
        cursor.execute("select chr_管理员账号01 from Chenhr_管理员登录01")
        while (True):
            data = cursor.fetchone()
            if data == None:
                tk.messagebox.showerror(title='Error', message='您输入的账号不存在!')
                comb.mainloop()
                flag = 0
                break
            if data[0] == number:
                break
        if flag:
            cursor.execute(
                f"select chr_管理员密码01 from Chenhr_管理员登录01 where chr_管理员账号01 = {number}"
            )
            while (True):
                data = cursor.fetchone()
                if data == None:
                    tk.messagebox.showerror(title='Error',
                                            message='您输入的密码有误，请重新输入')
                    comb.mainloop()
                    break
                if data[0] == password:
                    tk.messagebox.showinfo(title='Hello', message='欢迎进入学生管理系统')
                    windows.withdraw()
                    windowsD.deiconify()
                    break


windowsC = tk.Canvas(windows, width=600, height=500)
windowsC.pack()

windowsC.create_text(290, 100, text='高校成绩管理系统', font=('华文隶书', 25))
windowsC.create_text(100, 196, text='请选择身份:', font=('等线', 17))
windowsC.create_text(110, 251, text='登录账号:', font=('等线', 17))
windowsC.create_text(110, 306, text='输入密码:', font=('等线', 17))

e1 = tk.Entry(windows,
              show=None,
              font=('等线', 13),
              highlightcolor='black',
              highlightthickness=2)
e1.place(relx=0.346, rely=0.475, relwidth=0.51, relheight=0.06)

e2 = tk.Entry(windows,
              show='*',
              font=('等线', 13),
              highlightcolor='black',
              highlightthickness=2)
e2.place(relx=0.346, rely=0.575, relwidth=0.51, relheight=0.06)

var1 = tk.StringVar()
var1.set('学生')
comb = ttk.Combobox(windows,
                    textvariable=var1,
                    values=['学生', '教师', '教务处'],
                    font=('等线', 14),
                    state='readonly')
comb.place(relx=0.346, rely=0.361, relwidth=0.507, relheight=0.058)

b1 = tk.Button(windows,
               text='登录',
               width=9,
               height=1,
               command=get_login,
               bg='white',
               font=('等线', 13),
               relief='raised').place(x=250, y=400)

svar1 = tk.StringVar()
svar2 = tk.StringVar()


# 学生界面控件
def get_score():
    columns = ['1', '2', '3', '4', '5']
    slb = ttk.Treeview(windowsS, show="headings", columns=columns)
    slb.place(x=25, y=100, width=700, height=555)
    slb.column('1', width=100, anchor="center")
    slb.column('2', width=100, anchor="center")
    slb.column('3', width=100, anchor="center")
    slb.column('4', width=100, anchor="center")
    slb.column('5', width=100, anchor="center")
    slb.heading('1', text='学号')
    slb.heading('2', text='姓名')
    slb.heading('3', text='课程')
    slb.heading('4', text='得分')
    slb.heading('5', text='任课老师')

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    if scomb2.get() == '第一学期':
        term = 1
    else:
        term = 2

    sql = "select chr_学号01, chr_学生姓名01, chr_课程名称01, chr_成绩01, chr_教师姓名01 "
    sql += "from Chenhr_学生成绩01 "
    sql += f"where chr_学号01={str(number)} and chr_开课学年01={str(scomb1.get())} and chr_开课学期01={str(term)}"
    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            slb.insert('', cnt, values=(ll))
        else:
            break


def get_credit():
    columns = ['1', '2', '3']
    slb = ttk.Treeview(windowsS, show="headings", columns=columns)
    slb.place(x=25, y=100, width=700, height=555)
    slb.column('1', width=140, anchor="center")
    slb.column('2', width=140, anchor="center")
    slb.column('3', width=140, anchor="center")
    slb.heading('1', text='学号')
    slb.heading('2', text='姓名')
    slb.heading('3', text='学分')

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    if scomb2.get() == '第一学期':
        term = 1
    else:
        term = 2

    sql = "select chr_学号01, chr_学生姓名01, chr_学生总学分01 "
    sql += "from Chenhr_学生总学分01 "
    sql += f"where chr_学号01={str(number)} and chr_开课学年01={str(scomb1.get())} and chr_开课学期01={str(term)}"
    cursor = db.cursor()
    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            slb.insert('', cnt, values=(ll))
        else:
            break


def get_coffering():
    columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    slb = ttk.Treeview(windowsS, show="headings", columns=columns)
    slb.place(x=25, y=100, width=700, height=555)
    slb.column('1', width=95)
    slb.column('2', width=95)
    slb.column('3', width=135)
    slb.column('4', width=95)
    slb.column('5', width=90)
    slb.column('6', width=95)
    slb.column('7', width=90)
    slb.heading('1', text='班级')
    slb.heading('2', text='课程编号')
    slb.heading('3', text='课程名称')
    slb.heading('4', text='任课老师')
    slb.heading('5', text='学时')
    slb.heading('6', text='考核方式')
    slb.heading('7', text='学分')

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    if scomb2.get() == '第一学期':
        term = 1
    else:
        term = 2

    sql = "select chr_专业名称01, chr_班级编号01, chr_课程编号01, chr_课程名称01, chr_教师姓名01, chr_学时01, chr_考试或考查01, chr_学分01 "
    sql += "from Chenhr_学生课表01 "
    sql += f"where chr_学号01={str(number)} and chr_开课学年01={str(scomb1.get())} and chr_开课学期01={str(term)}"

    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            ll[0] = ll[0].replace(" ", "") + ll[1]
            ll.pop(1)
            slb.insert('', cnt, values=(ll))
        else:
            break


def get_infor():
    columns = ['1', '2', '3', '4', '5', '6', '7']
    slb = ttk.Treeview(windowsS, show="headings", columns=columns)
    slb.place(x=25, y=100, width=700, height=555)
    slb.column('1', width=100)
    slb.column('2', width=90)
    slb.column('3', width=90)
    slb.column('4', width=90)
    slb.column('5', width=90)
    slb.column('6', width=120)
    slb.column('7', width=90)
    slb.heading('1', text='学号', anchor="center")
    slb.heading('2', text='姓名', anchor="center")
    slb.heading('3', text='班级', anchor="center")
    slb.heading('4', text='性别', anchor="center")
    slb.heading('5', text='年龄', anchor="center")
    slb.heading('6', text='生源所在地', anchor="center")
    slb.heading('7', text='已修学分', anchor="center")

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    sql = "select chr_学号01, chr_学生姓名01, chr_专业名称01, Chenhr_专业班级01.chr_班级编号01, chr_学生性别01, chr_学生年龄01, chr_生源所在省01, chr_生源所在市01, chr_已修学分总数01 "
    sql += "from Chenhr_学生01, Chenhr_专业班级01 "
    sql += f"where chr_学号01={str(number)}"
    sql += " and Chenhr_学生01.chr_专业编号01=Chenhr_专业班级01.chr_专业编号01 "
    sql += " and Chenhr_学生01.chr_班级编号01=Chenhr_专业班级01.chr_班级编号01 "
    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            ll[2] = ll[2].replace(" ", "") + ll[3]
            ll[6] = ll[6].replace(" ", "") + ll[7]
            ll.pop(3)
            ll.pop(6)
            slb.insert('', cnt, values=(ll))
        else:
            break


def get_rank():
    columns = ['1', '2', '3', '4', '5']
    slb = ttk.Treeview(windowsS, show="headings", columns=columns)
    slb.place(x=25, y=100, width=700, height=555)
    slb.column('1', width=100)
    slb.column('2', width=100)
    slb.column('3', width=100)
    slb.column('4', width=100)
    slb.column('5', width=100)
    slb.heading('1', text='学号', anchor="center")
    slb.heading('2', text='姓名', anchor="center")
    slb.heading('3', text='班级', anchor="center")
    slb.heading('4', text='学年', anchor="center")
    slb.heading('5', text='绩点', anchor="center")

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    sql = "select b.* from Chenhr_绩点排名01 a, Chenhr_绩点排名01 b "
    sql += f"where a.chr_学号01 = '{str(number)}' and a.chr_专业名称01 = b.chr_专业名称01 and b.chr_开课学年01 = '{str(scomb1.get())}' "
    sql += "order by b.chr_绩点01 desc"
    cursor = db.cursor()
    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            if data[4].replace(" ", "") != str(scomb1.get()):
                continue
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            ll[2] = ll[2].replace(" ", "") + ll[3]
            ll.pop(3)
            slb.insert('', cnt, values=(ll))
        else:
            break


def get_backS():
    e1.delete(0, len(e1.get()))
    e2.delete(0, len(e2.get()))
    windows.deiconify()
    windowsS.quit()
    windowsS.withdraw()


svar1.set('2020')
svar2.set('第二学期')
canvass = tk.Canvas(windowsS, width=1200, height=1200)
canvass.pack()

scomb1 = ttk.Combobox(windowsS,
                      textvariable=svar1,
                      values=['2019', '2020', '2021', '2022'],
                      font=('等线', 14),
                      state='readonly')
scomb1.place(relx=0.0285, rely=0.051, relwidth=0.407, relheight=0.058)

scomb2 = ttk.Combobox(windowsS,
                      textvariable=svar2,
                      values=['第一学期', '第二学期'],
                      font=('等线', 14),
                      state='readonly')
scomb2.place(relx=0.565, rely=0.051, relwidth=0.407, relheight=0.058)

sb1 = tk.Button(windowsS,
                text='查询个人成绩',
                width=14,
                height=2,
                bg='white',
                font=('等线', 13),
                relief='raised',
                command=get_score).place(x=739, y=100)
sb2 = tk.Button(windowsS,
                text='查询获得学分',
                width=14,
                height=2,
                bg='white',
                font=('等线', 13),
                relief='raised',
                command=get_credit).place(x=739, y=196)
sb3 = tk.Button(windowsS,
                text='查询班级课表',
                width=14,
                height=2,
                bg='white',
                font=('等线', 13),
                relief='raised',
                command=get_coffering).place(x=739, y=292)
sb4 = tk.Button(windowsS,
                text='查询个人信息',
                width=14,
                height=2,
                bg='white',
                font=('等线', 13),
                relief='raised',
                command=get_infor).place(x=739, y=388)
sb5 = tk.Button(windowsS,
                text='查询绩点排名',
                width=14,
                height=2,
                bg='white',
                font=('等线', 13),
                relief='raised',
                command=get_rank).place(x=739, y=484)
sb6 = tk.Button(windowsS,
                text='返回登陆界面',
                width=14,
                height=2,
                bg='white',
                font=('等线', 13),
                relief='raised',
                command=get_backS).place(x=739, y=580)

columns = []
slb = ttk.Treeview(windowsS, show="headings", columns=columns)
slb.place(x=25, y=100, width=700, height=555)

# 教师界面控件
tls1 = tk.StringVar()
tls2 = tk.StringVar()
tls3 = tk.StringVar()
tls4 = tk.StringVar()
tls5 = tk.StringVar()
tls6 = tk.StringVar()
tls7 = tk.StringVar()


def get_backT():
    e1.delete(0, len(e1.get()))
    e2.delete(0, len(e2.get()))
    windows.deiconify()
    windowsT.quit()
    windowsT.withdraw()


def get_tinfor():
    columns = ['1', '2', '3', '4', '5', '6']
    trv = ttk.Treeview(windowsT, show="headings", columns=columns)
    trv.place(x=5, y=100, width=580, height=555)
    trv.column('1', width=90, anchor="center")
    trv.column('2', width=90, anchor="center")
    trv.column('3', width=90, anchor="center")
    trv.column('4', width=90, anchor="center")
    trv.column('5', width=90, anchor="center")
    trv.column('6', width=90, anchor="center")
    trv.heading('1', text='教师编号')
    trv.heading('2', text='姓名')
    trv.heading('3', text='性别')
    trv.heading('4', text='年龄')
    trv.heading('5', text='职称')
    trv.heading('6', text='联系电话')

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    sql = f"select * from Chenhr_教师01 where chr_教师编号01={str(number)}"
    cursor = db.cursor()
    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            trv.insert('', cnt, values=(ll))
        else:
            break


def get_avgc():
    columns = ['1', '2', '3', '4']
    trv = ttk.Treeview(windowsT, show="headings", columns=columns)
    trv.place(x=5, y=100, width=580, height=555)
    trv.column('1', width=150)
    trv.column('2', width=150)
    trv.column('3', width=150)
    trv.column('4', width=150)
    trv.heading('1', text='课程名称')
    trv.heading('2', text='开课学年')
    trv.heading('3', text='开课学期')
    trv.heading('4', text='平均成绩')

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    sql = "select * from Chenhr_课程平均成绩01"
    cursor = db.cursor()
    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            trv.insert('', cnt, values=(ll))
        else:
            break


def get_cinfor():
    columns = ['1', '2', '3', '4', '5', '6', '7', '8']
    trv = ttk.Treeview(windowsT, show="headings", columns=columns)
    trv.place(x=5, y=100, width=580, height=555)
    trv.column('1', width=100)
    trv.column('2', width=70)
    trv.column('3', width=120)
    trv.column('4', width=70)
    trv.column('5', width=70)
    trv.column('6', width=35)
    trv.column('7', width=70)
    trv.column('8', width=35)
    trv.heading('1', text='班级')
    trv.heading('2', text='课程编号')
    trv.heading('3', text='课程名称')
    trv.heading('4', text='任课老师')
    trv.heading('5', text='开课时间')
    trv.heading('6', text='学时')
    trv.heading('7', text='考核方式')
    trv.heading('8', text='学分')

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    sql = "select chr_专业名称01, chr_班级编号01, chr_课程编号01, chr_课程名称01, chr_教师姓名01, chr_开课学年01, chr_开课学期01, chr_学时01, chr_考试或考查01, chr_学分01 "
    sql += "from Chenhr_教师课表01 where "
    sql += f"chr_教师编号01={str(number)}"
    cursor = db.cursor()
    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            ll[0] = ll[0].replace(" ", "") + ll[1]
            ll.pop(1)
            ll[4] = ll[4].replace(" ", "") + '(' + ll[5].replace(" ", "") + ')'
            ll.pop(5)
            trv.insert('', cnt, values=(ll))
        else:
            break


def get_sinfor():
    templ = []

    def get_modify():
        try:
            int(te7.get()) or float(te7.get())
        except Exception:
            tk.messagebox.showwarning(message="您的输入格式有误,请重新输入")
            return
        trv.set(trv.selection()[0], '7', te7.get())
        sql = f"update Chenhr_上课01 set chr_成绩01={int(str(te7.get().replace(' ', '')))} where"
        sql += f" chr_学号01='{str(te1.get().replace(' ', ''))}' and chr_课程编号01='{str(te3.get().replace(' ', ''))}'"
        sql += f" and chr_开课学年01='{str(te6.get()[0:4])}' and chr_开课学期01='{str(te6.get()[5:6])}'"
        print(sql)
        templ.append(sql)
        tk.messagebox.showinfo(message="修改操作已记录!")

    def get_remember():
        try:
            db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                                 'ChenhrMIS01')
        except Exception:
            tk.messagebox.showerror(title='Error', message='连接数据库失败!')
        cursor = db.cursor()
        for sql in templ:
            cursor.execute(sql)
            db.commit()
        tk.messagebox.showinfo(message='修改录入成功!')

    tb_xiugai = tk.Button(windowsT,
                          text='修改',
                          font=('等线', 13),
                          relief='raised',
                          width=19,
                          height=2,
                          command=get_modify)
    tb_xiugai.place(x=665, y=390)

    tb_baocun = tk.Button(windowsT,
                          text='保存',
                          font=('等线', 13),
                          relief='raised',
                          width=19,
                          height=2,
                          command=get_remember)
    tb_baocun.place(x=665, y=460)

    def treeviewClick(event):  # 单击
        try:
            ll = []
            for item in trv.selection():
                item_text = trv.item(item, "values")
                for i in item_text:
                    ll.append(i)
            tls1.set(ll[0])
            tls2.set(ll[1])
            tls3.set(ll[2])
            tls4.set(ll[3])
            tls5.set(ll[4])
            tls6.set(ll[5])
            tls7.set(ll[6])
        except Exception:
            print('请勿乱点击!')

    columns = ['1', '2', '3', '4', '5', '6', '7']
    trv = ttk.Treeview(windowsT, show="headings", columns=columns)
    trv.place(x=5, y=100, width=580, height=555)
    trv.column('1', width=100, anchor="center")
    trv.column('2', width=60, anchor="center")
    trv.column('3', width=60, anchor="center")
    trv.column('4', width=120, anchor="center")
    trv.column('5', width=60, anchor="center")
    trv.column('6', width=80, anchor="center")
    trv.column('7', width=60, anchor="center")
    trv.heading('1', text='学号')
    trv.heading('2', text='姓名')
    trv.heading('3', text='课程编号')
    trv.heading('4', text='课程名称')
    trv.heading('5', text='专业')
    trv.heading('6', text='开课时间')
    trv.heading('7', text='成绩')

    trv.bind('<ButtonRelease-1>', treeviewClick)
    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()
    sql = "select chr_学号01, chr_学生姓名01, chr_课程编号01, chr_课程名称01, chr_专业名称01, chr_开课学年01, chr_开课学期01, chr_成绩01 "
    sql += f"from Chenhr_教师查学生成绩01 where chr_教师编号01={str(number)} order by chr_成绩01"
    cursor.execute(sql)
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            ll[5] = ll[5].replace(" ", "") + '(' + ll[6].replace(" ", "") + ')'
            ll.pop(6)
            trv.insert('', cnt, values=(ll))
        else:
            break


canvast = tk.Canvas(windowsT, width=900, height=700)
canvast.pack()

canvast.create_text(620, 110, text='学号:', font=('黑体', 17))
canvast.create_text(620, 150, text='姓名:', font=('黑体', 17))
canvast.create_text(620, 190, text='课号:', font=('黑体', 17))
canvast.create_text(620, 230, text='课名:', font=('黑体', 17))
canvast.create_text(620, 270, text='专业:', font=('黑体', 17))
canvast.create_text(620, 310, text='学期:', font=('黑体', 17))
canvast.create_text(620, 350, text='成绩:', font=('黑体', 17))
canvast.create_text(690, 50, text='学生成绩信息:', font=('等线', 25))

tb1 = tk.Button(windowsT,
                text='学生成绩管理',
                font=('等线', 13),
                relief='raised',
                width=13,
                height=2,
                command=get_sinfor)
tb1.place(x=10, y=30)

tb2 = tk.Button(windowsT,
                text='教师授课查询',
                font=('等线', 13),
                relief='raised',
                width=13,
                height=2,
                command=get_cinfor)
tb2.place(x=290, y=30)

tb5 = tk.Button(windowsT,
                text='返回登录界面',
                font=('等线', 13),
                relief='raised',
                width=19,
                height=2,
                command=get_backT)
tb5.place(x=665, y=600)

tb6 = tk.Button(windowsT,
                text='个人信息查询',
                font=('等线', 13),
                relief='raised',
                width=13,
                height=2,
                command=get_tinfor)
tb6.place(x=150, y=30)

tb6 = tk.Button(windowsT,
                text='课程平均成绩',
                font=('等线', 13),
                relief='raised',
                width=13,
                height=2,
                command=get_avgc)
tb6.place(x=430, y=30)

columns = ['1', '2', '3', '4', '5', '6', '7']
trv = ttk.Treeview(windowsT,
                   show="headings",
                   columns=columns,
                   selectmode=tk.BROWSE)
trv.column('1', width=68, anchor="center")
trv.column('2', width=68, anchor="center")
trv.column('3', width=68, anchor="center")
trv.column('4', width=68, anchor="center")
trv.column('5', width=68, anchor="center")
trv.column('6', width=68, anchor="center")
trv.column('7', width=68, anchor="center")
trv.place(x=5, y=100, width=580, height=555)
trv.insert('', 0, values=('', '', '', '', '', '', ''))

te1 = tk.Entry(windowsT,
               textvariable=tls1,
               highlightthickness=1,
               highlightcolor='black',
               font=('等线', 13))
te2 = tk.Entry(windowsT,
               textvariable=tls2,
               highlightthickness=1,
               highlightcolor='black',
               font=('等线', 13))
te3 = tk.Entry(windowsT,
               textvariable=tls3,
               highlightthickness=1,
               highlightcolor='black',
               font=('等线', 13))
te4 = tk.Entry(windowsT,
               textvariable=tls4,
               highlightthickness=1,
               highlightcolor='black',
               font=('等线', 13))
te5 = tk.Entry(windowsT,
               textvariable=tls5,
               highlightthickness=1,
               highlightcolor='black',
               font=('等线', 13))
te6 = tk.Entry(windowsT,
               textvariable=tls6,
               highlightthickness=1,
               highlightcolor='black',
               font=('等线', 13))
te7 = tk.Entry(windowsT,
               textvariable=tls7,
               highlightthickness=1,
               highlightcolor='black',
               font=('等线', 13))
te1.place(x=660, y=95, relwidth=0.21, relheight=0.05)
te2.place(x=660, y=135, relwidth=0.21, relheight=0.05)
te3.place(x=660, y=175, relwidth=0.21, relheight=0.05)
te4.place(x=660, y=215, relwidth=0.21, relheight=0.05)
te5.place(x=660, y=255, relwidth=0.21, relheight=0.05)
te6.place(x=660, y=295, relwidth=0.21, relheight=0.05)
te7.place(x=660, y=335, relwidth=0.21, relheight=0.05)

# 教务处界面控件
JAvar1 = tk.StringVar()
JAvar2 = tk.StringVar()
JAvar3 = tk.StringVar()
JAvar4 = tk.StringVar()
JAvar5 = tk.StringVar()
JAvar6 = tk.StringVar()
JAvar7 = tk.StringVar()
JAvar8 = tk.StringVar()
JAvar9 = tk.StringVar()
JAvar10 = tk.StringVar()
JAvar11 = tk.StringVar()
jesv1 = tk.StringVar()
jesv2 = tk.StringVar()
jesv3 = tk.StringVar()
jesv4 = tk.StringVar()
jesv5 = tk.StringVar()
jesv6 = tk.StringVar()
jesv7 = tk.StringVar()
jesv8 = tk.StringVar()
jesv9 = tk.StringVar()
jett1 = tk.StringVar()
jett2 = tk.StringVar()
jett3 = tk.StringVar()
jett4 = tk.StringVar()
jett5 = tk.StringVar()
jett6 = tk.StringVar()


def get_Sc():
    def treeviewClick2(event):
        try:
            ll = []
            for item in jtvs.selection():
                item_text = jtvs.item(item, "values")
                for i in item_text:
                    ll.append(i)
            jesv1.set(ll[0])
            jesv2.set(ll[1])
            jesv3.set(ll[2])
            jesv4.set(ll[3])
            jesv5.set(ll[4])
            jesv6.set(ll[5])
            jesv7.set(ll[6])
            jesv8.set(ll[7])
            jesv9.set(ll[8])
        except Exception:
            print('请勿乱点击!')

    def get_new():
        try:
            sql = f"insert into Chenhr_学生01 values('{str(jes1.get().replace(' ', ''))}', '{str(jes2.get().replace(' ', ''))}', '{str(jes3.get().replace(' ', ''))}', "
            sql += f"'{str(jes4.get().replace(' ', ''))}', '{str(jes5.get().replace(' ', ''))}', {str(jes6.get())}, '{str(jes7.get().replace(' ', ''))}', "
            sql += f"'{str(jes8.get().replace(' ', ''))}', {str(jes9.get())})"

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            cursor.execute(sql)
            db.commit()
            if int(jes6.get()) and int(jes9.get(
            )) and jes1.get() != '' and jes2.get() != '' and jes3.get(
            ) != '' and jes4.get() != '' and jes5.get() != '' and jes7.get(
            ) != '' and jes8.get() != '':
                jtvs.insert('',
                            0,
                            values=(jes1.get().replace(' ', ''),
                                    jes2.get().replace(' ', ''),
                                    jes3.get().replace(' ', ''),
                                    jes4.get().replace(' ', ''),
                                    jes5.get().replace(' ', ''),
                                    jes6.get().replace(' ', ''),
                                    jes7.get().replace(' ', ''),
                                    jes8.get().replace(' ', ''),
                                    jes9.get().replace(' ', '')))
                tk.messagebox.showinfo(message="新建成功!")
            else:
                tk.messagebox.showwarning(message="您的插入数据有误，请检查后重新插入")
        except Exception:
            tk.messagebox.showwarning(message="您的插入数据有误，请检查后重新插入")

    def get_modify2():
        number1 = jes1.get().replace(' ', '')
        if int(jes6.get()) and int(jes9.get()) and jes1.get(
        ) != '' and jes2.get() != '' and jes3.get() != '' and jes4.get(
        ) != '' and jes5.get() != '' and jes7.get() != '' and jes8.get() != '':
            pass
        else:
            tk.messagebox.showwarning(message="您的输入格式有误,请重新输入")
            return
        jtvs.set(jtvs.selection()[0], ['1'], jes1.get())
        jtvs.set(jtvs.selection()[0], ['2'], jes2.get())
        jtvs.set(jtvs.selection()[0], ['3'], jes3.get())
        jtvs.set(jtvs.selection()[0], ['4'], jes4.get())
        jtvs.set(jtvs.selection()[0], ['5'], jes5.get())
        jtvs.set(jtvs.selection()[0], ['6'], jes6.get())
        jtvs.set(jtvs.selection()[0], ['7'], jes7.get())
        jtvs.set(jtvs.selection()[0], ['8'], jes8.get())
        jtvs.set(jtvs.selection()[0], ['9'], jes9.get())
        try:
            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            sql = f"update Chenhr_学生01 set chr_学号01='{str(jes1.get().replace(' ', ''))}', chr_专业编号01='{str(jes2.get().replace(' ', ''))}', chr_班级编号01='{str(jes3.get().replace(' ', ''))}', "
            sql += f"chr_学生姓名01='{str(jes4.get().replace(' ', ''))}', chr_学生性别01='{str(jes5.get().replace(' ', ''))}', chr_学生年龄01={str(jes6.get().replace(' ', ''))}, "
            sql += f"chr_生源所在省01='{str(jes7.get().replace(' ', ''))}', chr_生源所在市01='{str(jes8.get().replace(' ', ''))}', chr_已修学分总数01={str(jes9.get().replace(' ', ''))} "
            sql += f"where chr_学号01='{str(number1)}'"
            cursor.execute(sql)
            db.commit()
            tk.messagebox.showinfo(message="修改成功!")
        except Exception:
            tk.messagebox.showwarning(message="遇到问题修改失败")

    def get_delete():
        try:
            sql = f"delete from Chenhr_学生01 where chr_学号01='{str(jes1.get().replace(' ', ''))}'"

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            cursor.execute(sql)
            db.commit()
            jtvs.delete(jtvs.selection()[0])
            tk.messagebox.showinfo(message="删除成功!")
        except Exception:
            tk.messagebox.showwarning(message="删除失败")

    def get_delb():
        try:
            sql = f"exec chr_毕业sp01 @chr_最低学分01={str(jes9.get().replace(' ', ''))}"

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            cursor.execute(sql)
            db.commit()
            jtvs.delete(jtvs.selection()[0])
            tk.messagebox.showinfo(message="删除成功!")
        except Exception:
            tk.messagebox.showwarning(message="删除失败")

    sb3 = tk.Button(windowsDS,
                    text='删除学生信息',
                    font=('等线', 13),
                    relief='raised',
                    width=13,
                    height=2,
                    command=get_delete)
    sb3.place(x=450, y=180)

    sb2 = tk.Button(windowsDS,
                    text='修改学生信息',
                    font=('等线', 13),
                    relief='raised',
                    width=13,
                    height=2,
                    command=get_modify2)
    sb2.place(x=450, y=120)

    sb1 = tk.Button(windowsDS,
                    text='新建学生信息',
                    font=('等线', 13),
                    relief='raised',
                    width=13,
                    height=2,
                    command=get_new)
    sb1.place(x=450, y=60)

    sb7 = tk.Button(windowsDS,
                    text='删除毕业学生',
                    font=('等线', 13),
                    relief='raised',
                    width=13,
                    height=2,
                    command=get_delb)
    sb7.place(x=450, y=240)

    windowsD.withdraw()
    windowsDS.deiconify()
    columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    jtvs = ttk.Treeview(windowsDS, show="headings", columns=columns)
    jtvs.place(x=52, y=310, width=600, height=255)
    jtvs.column('1', width=120, anchor="center")
    jtvs.column('2', width=60, anchor="center")
    jtvs.column('3', width=60, anchor="center")
    jtvs.column('4', width=40, anchor="center")
    jtvs.column('5', width=40, anchor="center")
    jtvs.column('6', width=40, anchor="center")
    jtvs.column('7', width=70, anchor="center")
    jtvs.column('8', width=70, anchor="center")
    jtvs.column('9', width=90, anchor="center")
    jtvs.heading('1', text='学号')
    jtvs.heading('2', text='专业编号')
    jtvs.heading('3', text='班级编号')
    jtvs.heading('4', text='姓名')
    jtvs.heading('5', text='性别')
    jtvs.heading('6', text='年龄')
    jtvs.heading('7', text='生源所在省')
    jtvs.heading('8', text='生源所在市')
    jtvs.heading('9', text='已修学分总数')
    jtvs.yview_scroll(10, 'units')
    jtvs.bind('<ButtonRelease-1>', treeviewClick2)

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    cursor.execute("select * from Chenhr_学生01")
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            jtvs.insert('', cnt, values=(ll))
        else:
            break


def get_Tc():
    def treeviewClick3(event):
        try:
            ll = []
            for item in jtvt.selection():
                item_text = jtvt.item(item, "values")
                for i in item_text:
                    ll.append(i)
            jett1.set(ll[0])
            jett2.set(ll[1])
            jett3.set(ll[2])
            jett4.set(ll[3])
            jett5.set(ll[4])
            jett6.set(ll[5])
        except Exception:
            print('请勿乱点击!')

    def get_new2():
        try:
            sql = f"insert into Chenhr_教师01 values('{str(jett1.get().replace(' ', ''))}', '{str(jett2.get().replace(' ', ''))}', '{str(jett3.get().replace(' ', ''))}', "
            sql += f"'{str(jett4.get().replace(' ', ''))}', '{str(jett5.get().replace(' ', ''))}', '{str(jett6.get().replace(' ', ''))}')"

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            cursor.execute(sql)
            db.commit()
            if int(jett4.get()) and jett1.get() != '' and jett2.get() != '' and jett3.get() != '' and jett5.get() != '' and jett6.get() != '':
                jtvt.insert('',
                            0,
                            values=(jett1.get()[0:9], jett2.get(),
                                    jett3.get()[0:1], jett4.get(), jett5.get(),
                                    jett6.get()[0:11]))
                tk.messagebox.showinfo(message="新建成功!")
            else:
                tk.messagebox.showwarning(message="您的插入数据有误，请检查后重新插入")
        except Exception:
            tk.messagebox.showwarning(message="您的插入数据有误，请检查后重新插入")

    def get_modify3():
        if int(jet1.get()) and int(jet4.get()) and int(jet6.get()) and jet2.get() != '' and jet3.get() != '' and jet5.get() != '':
            pass
        else:
            tk.messagebox.showwarning(message='您的输入格式有误,请重新输入')
            return
        jtvt.set(jtvt.selection()[0], ['1'], jet1.get())
        jtvt.set(jtvt.selection()[0], ['2'], jet2.get())
        jtvt.set(jtvt.selection()[0], ['3'], jet3.get())
        jtvt.set(jtvt.selection()[0], ['4'], jet4.get())
        jtvt.set(jtvt.selection()[0], ['5'], jet5.get())
        jtvt.set(jtvt.selection()[0], ['6'], jet6.get())
        try:
            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            sql = f"update Chenhr_教师01 set chr_教师编号01='{str(jet1.get().replace(' ', ''))}', chr_教师姓名01='{str(jet2.get().replace(' ', ''))}',chr_教师性别01='{str(jet3.get().replace(' ', ''))}', "
            sql += f"chr_教师年龄01='{str(jet4.get().replace(' ', ''))}', chr_职称01='{str(jet5.get().replace(' ', ''))}', chr_联系电话01='{str(jet6.get().replace(' ', ''))}' where chr_教师编号01='{str(jet1.get().replace(' ', ''))}'"
            cursor.execute(sql)
            db.commit()
            tk.messagebox.showinfo(message="修改成功!")
        except Exception:
            tk.messagebox.showwarning(message='修改失败!')

    def get_delete2():
        try:
            sql = f"delete from Chenhr_教师01 where chr_教师编号01='{str(jet1.get().replace(' ', ''))}'"

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            cursor.execute(sql)
            db.commit()
            jtvt.delete(jtvt.selection()[0])
            tk.messagebox.showinfo(message="删除成功!")
        except Exception:
            tk.messagebox.showwarning(message="删除失败")

    columns = ['1', '2', '3', '4', '5', '6']
    jtvt = ttk.Treeview(windowsDT, show="headings", columns=columns)
    jtvt.column('1', width=100, anchor="center")
    jtvt.column('2', width=100, anchor="center")
    jtvt.column('3', width=100, anchor="center")
    jtvt.column('4', width=100, anchor="center")
    jtvt.column('5', width=98, anchor="center")
    jtvt.column('6', width=98, anchor="center")
    jtvt.heading('1', text='编号')
    jtvt.heading('2', text='姓名')
    jtvt.heading('3', text='性别')
    jtvt.heading('4', text='年龄')
    jtvt.heading('5', text='职称')
    jtvt.heading('6', text='联系电话')
    jtvt.place(x=52, y=310, width=600, height=255)

    try:
        db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin', 'admin',
                             'ChenhrMIS01')
    except Exception:
        tk.messagebox.showerror(title='Error', message='连接数据库失败!')
    cursor = db.cursor()

    cursor.execute("select * from Chenhr_教师01")
    cnt = -1
    while (True):
        cnt += 1
        data = cursor.fetchone()
        ll = []
        if data:
            for i in data:
                if i and isinstance(i, str):
                    s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                    ll.append(s)
                elif i:
                    ll.append(i)
            jtvt.insert('', cnt, values=(ll))
        else:
            break
    tb1 = tk.Button(windowsDT,
                    text='新建教师信息',
                    font=('等线', 13),
                    relief='raised',
                    width=13,
                    height=2,
                    command=get_new2)
    tb2 = tk.Button(windowsDT,
                    text='修改教师信息',
                    font=('等线', 13),
                    relief='raised',
                    width=13,
                    height=2,
                    command=get_modify3)
    tb3 = tk.Button(windowsDT,
                    text='删除教师信息',
                    font=('等线', 13),
                    relief='raised',
                    width=13,
                    height=2,
                    command=get_delete2)
    tb1.place(x=450, y=80)
    tb2.place(x=450, y=160)
    tb3.place(x=450, y=240)
    windowsD.withdraw()
    windowsDT.deiconify()
    jtvt.bind('<ButtonRelease-1>', treeviewClick3)


def get_At():
    def handler(event):
        temp = ja1.get()
        if temp == '北京':
            ja2.place(x=370, y=90, width=290, height=30)
            updateGlobal(2)
        elif temp == '浙江':
            ja3.place(x=370, y=90, width=290, height=30)
            updateGlobal(3)
        elif temp == '江苏':
            ja4.place(x=370, y=90, width=290, height=30)
            updateGlobal(4)
        elif temp == '上海':
            ja5.place(x=370, y=90, width=290, height=30)
            updateGlobal(5)
        elif temp == '不限':
            ja2.place_forget()  # place_forget()隐藏按钮
            ja3.place_forget()
            ja4.place_forget()
            ja5.place_forget()
            updateGlobal(0)

    def get_Count():
        if ja1.get() == '不限':
            columns = ['1', '2']
            jtva = ttk.Treeview(windowsDA, show="headings", columns=columns)
            jtva.place(x=30, y=150, width=400, height=400)
            jtva.column('1', width=200, anchor="center")
            jtva.column('2', width=190, anchor="center")
            jtva.heading('1', text='省')
            jtva.heading('2', text='人数')

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            sql = "select * from Chenhr_学生生源地省01"
            cursor.execute(sql)
            cnt = -1
            while (True):
                cnt += 1
                data = cursor.fetchone()
                ll = []
                if data:
                    for i in data:
                        if i and isinstance(i, str):
                            s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                            ll.append(s)
                        elif i:
                            ll.append(i)
                    jtva.insert('', cnt, values=(ll))
                else:
                    break
        elif a == 0 or ja2.get() == '不限':
            columns = ['1', '2']
            jtva = ttk.Treeview(windowsDA, show="headings", columns=columns)
            jtva.place(x=30, y=150, width=400, height=400)
            jtva.column('1', width=200, anchor="center")
            jtva.column('2', width=190, anchor="center")
            jtva.heading('1', text='市')
            jtva.heading('2', text='人数')

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            sql = f"select chr_生源所在市01, chr_学生数量01 from Chenhr_学生生源地市01 where chr_生源所在省01='{str(ja1.get())}'"
            cursor.execute(sql)
            cnt = -1
            while (True):
                cnt += 1
                data = cursor.fetchone()
                ll = []
                if data:
                    for i in data:
                        if i and isinstance(i, str):
                            s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                            ll.append(s)
                        elif i:
                            ll.append(i)
                    jtva.insert('', cnt, values=(ll))
                else:
                    break

        elif a == 2:
            columns = ['1', '2']
            jtva = ttk.Treeview(windowsDA, show="headings", columns=columns)
            jtva.place(x=30, y=150, width=400, height=400)
            jtva.column('1', width=200, anchor="center")
            jtva.column('2', width=190, anchor="center")
            jtva.heading('1', text='市')
            jtva.heading('2', text='人数')

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            sql = f"select chr_生源所在市01, chr_学生数量01 from Chenhr_学生生源地市01 where chr_生源所在市01='{str(ja2.get())}'"
            cursor.execute(sql)
            cnt = -1
            while (True):
                cnt += 1
                data = cursor.fetchone()
                ll = []
                if data:
                    for i in data:
                        if i and isinstance(i, str):
                            s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                            ll.append(s)
                        elif i:
                            ll.append(i)
                    jtva.insert('', cnt, values=(ll))
                else:
                    break
        elif a == 3:
            columns = ['1', '2']
            jtva = ttk.Treeview(windowsDA, show="headings", columns=columns)
            jtva.place(x=30, y=150, width=400, height=400)
            jtva.column('1', width=200, anchor="center")
            jtva.column('2', width=190, anchor="center")
            jtva.heading('1', text='市')
            jtva.heading('2', text='人数')

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            sql = f"select chr_生源所在市01, chr_学生数量01 from Chenhr_学生生源地市01 where chr_生源所在市01='{str(ja3.get())}'"
            cursor.execute(sql)
            cnt = -1
            while (True):
                cnt += 1
                data = cursor.fetchone()
                ll = []
                if data:
                    for i in data:
                        if i and isinstance(i, str):
                            s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                            ll.append(s)
                        elif i:
                            ll.append(i)
                    jtva.insert('', cnt, values=(ll))
                else:
                    break
        elif a == 4:
            columns = ['1', '2']
            jtva = ttk.Treeview(windowsDA, show="headings", columns=columns)
            jtva.place(x=30, y=150, width=400, height=400)
            jtva.column('1', width=200, anchor="center")
            jtva.column('2', width=190, anchor="center")
            jtva.heading('1', text='市')
            jtva.heading('2', text='人数')

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            sql = f"select chr_生源所在市01, chr_学生数量01 from Chenhr_学生生源地市01 where chr_生源所在市01='{str(ja4.get())}'"
            cursor.execute(sql)
            cnt = -1
            while (True):
                cnt += 1
                data = cursor.fetchone()
                ll = []
                if data:
                    for i in data:
                        if i and isinstance(i, str):
                            s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                            ll.append(s)
                        elif i:
                            ll.append(i)
                    jtva.insert('', cnt, values=(ll))
                else:
                    break
        elif a == 5:
            columns = ['1', '2']
            jtva = ttk.Treeview(windowsDA, show="headings", columns=columns)
            jtva.place(x=30, y=150, width=400, height=400)
            jtva.column('1', width=200, anchor="center")
            jtva.column('2', width=190, anchor="center")
            jtva.heading('1', text='市）')
            jtva.heading('2', text='人数')

            try:
                db = pymssql.connect('DESKTOP-32DLNTS\\SQL2014', 'admin',
                                     'admin', 'ChenhrMIS01')
            except Exception:
                tk.messagebox.showerror(title='Error', message='连接数据库失败!')
            cursor = db.cursor()

            sql = f"select chr_生源所在市01, chr_学生数量01 from Chenhr_学生生源地市01 where chr_生源所在市01='{str(ja5.get())}'"
            cursor.execute(sql)
            cnt = -1
            while (True):
                cnt += 1
                data = cursor.fetchone()
                ll = []
                if data:
                    for i in data:
                        if i and isinstance(i, str):
                            s = i.encode('latin-1', errors='ignore').decode('gbk', errors='ignore')
                            ll.append(s)
                        elif i:
                            ll.append(i)
                    jtva.insert('', cnt, values=(ll))
                else:
                    break

    jab1 = tk.Button(windowsDA,
                     text='查询',
                     font=('等线', 13),
                     relief='raised',
                     width=15,
                     height=2,
                     command=get_Count)
    jab1.place(x=500, y=220)
    ja1.bind('<<ComboboxSelected>>', handler)
    windowsD.withdraw()
    windowsDA.deiconify()


# 后退到登录界面
def get_backj():
    e1.delete(0, len(e1.get()))
    e2.delete(0, len(e2.get()))
    windows.deiconify()
    windowsD.quit()
    windowsD.withdraw()


# 从学生管理界面后退到教务处界面
def get_backjs():
    windowsDS.withdraw()
    windowsD.deiconify()


# 从教师管理界面后退到教务处界面
def get_backjt():
    windowsDT.withdraw()
    windowsD.deiconify()


# 从地区信息统计界面后退到教务处界面
def get_backja():
    windowsDA.withdraw()
    windowsD.deiconify()


# 管理功能选择界面
jl = tk.Label(windowsD,
              text='教务处信息管理',
              font=('华文隶书', 20),
              bg='Red',
              width=25,
              height=2)
jl.place(x=110, y=40)

jb1 = tk.Button(windowsD,
                text='学生信息管理',
                font=('等线', 16),
                relief='raised',
                width=19,
                height=2,
                command=get_Sc)
jb2 = tk.Button(windowsD,
                text='教师信息管理',
                font=('等线', 16),
                relief='raised',
                width=19,
                height=2,
                command=get_Tc)
jb3 = tk.Button(windowsD,
                text='地区信息统计',
                font=('等线', 16),
                relief='raised',
                width=19,
                height=2,
                command=get_At)
jb4 = tk.Button(windowsD,
                text='返回登录界面',
                font=('等线', 12),
                relief='raised',
                width=16,
                height=2,
                command=get_backj)
jb1.place(x=190, y=150)
jb2.place(x=190, y=250)
jb3.place(x=190, y=350)
jb4.place(x=235, y=440)

# 教务处学生信息管理界面
jls1 = tk.Label(windowsDS, text='学号:', font=('等线', 13))
jls2 = tk.Label(windowsDS, text='专业编号:', font=('等线', 13))
jls3 = tk.Label(windowsDS, text='班级编号', font=('等线', 13))
jls4 = tk.Label(windowsDS, text='姓名:', font=('等线', 13))
jls5 = tk.Label(windowsDS, text='性别:', font=('等线', 13))
jls6 = tk.Label(windowsDS, text='年龄:', font=('等线', 13))
jls7 = tk.Label(windowsDS, text='地区（省）:', font=('等线', 13))
jls8 = tk.Label(windowsDS, text='地区（市）:', font=('等线', 13))
jls9 = tk.Label(windowsDS, text='已修学分总数:', font=('等线', 13))
jls10 = tk.Label(windowsDS, text='学生信息:', font=('等线', 20))
jls11 = tk.Label(windowsDS, text='操作选择:', font=('等线', 20))
jls1.place(x=50, y=80)
jls2.place(x=50, y=105)
jls3.place(x=50, y=130)
jls4.place(x=50, y=155)
jls5.place(x=50, y=180)
jls6.place(x=50, y=205)
jls7.place(x=50, y=230)
jls8.place(x=50, y=255)
jls9.place(x=50, y=280)
jls10.place(x=40, y=20)
jls11.place(x=420, y=20)
jes1 = tk.Entry(windowsDS,
                textvariable=jesv1,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes2 = tk.Entry(windowsDS,
                textvariable=jesv2,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes3 = tk.Entry(windowsDS,
                textvariable=jesv3,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes4 = tk.Entry(windowsDS,
                textvariable=jesv4,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes5 = tk.Entry(windowsDS,
                textvariable=jesv5,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes6 = tk.Entry(windowsDS,
                textvariable=jesv6,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes7 = tk.Entry(windowsDS,
                textvariable=jesv7,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes8 = tk.Entry(windowsDS,
                textvariable=jesv8,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes9 = tk.Entry(windowsDS,
                textvariable=jesv9,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jes1.place(x=160, y=80, relwidth=0.21, relheight=0.04)
jes2.place(x=160, y=105, relwidth=0.21, relheight=0.04)
jes3.place(x=160, y=130, relwidth=0.21, relheight=0.04)
jes4.place(x=160, y=155, relwidth=0.21, relheight=0.04)
jes5.place(x=160, y=180, relwidth=0.21, relheight=0.04)
jes6.place(x=160, y=205, relwidth=0.21, relheight=0.04)
jes7.place(x=160, y=230, relwidth=0.21, relheight=0.04)
jes8.place(x=160, y=255, relwidth=0.21, relheight=0.04)
jes9.place(x=160, y=280, relwidth=0.21, relheight=0.04)

sb4 = tk.Button(windowsDS,
                text='返回',
                font=('等线', 13),
                relief='raised',
                width=12,
                height=1,
                command=get_backjs)
sb4.place(x=290, y=560)

# 教务处教师信息管理界面
jlt1 = tk.Label(windowsDT, text='编号:', font=('等线', 13))
jlt2 = tk.Label(windowsDT, text='姓名:', font=('等线', 13))
jlt3 = tk.Label(windowsDT, text='性别:', font=('等线', 13))
jlt4 = tk.Label(windowsDT, text='年龄:', font=('等线', 13))
jlt5 = tk.Label(windowsDT, text='职称:', font=('等线', 13))
jlt6 = tk.Label(windowsDT, text='电话:', font=('等线', 13))
jlt8 = tk.Label(windowsDT, text='教师信息:', font=('等线', 20))
jlt9 = tk.Label(windowsDT, text='操作选择:', font=('等线', 20))
jlt1.place(x=50, y=80)
jlt2.place(x=50, y=116)
jlt3.place(x=50, y=152)
jlt4.place(x=50, y=188)
jlt5.place(x=50, y=224)
jlt6.place(x=50, y=260)
jlt8.place(x=40, y=20)
jlt9.place(x=420, y=20)
jet1 = tk.Entry(windowsDT,
                textvariable=jett1,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jet2 = tk.Entry(windowsDT,
                textvariable=jett2,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jet3 = tk.Entry(windowsDT,
                textvariable=jett3,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jet4 = tk.Entry(windowsDT,
                textvariable=jett4,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jet5 = tk.Entry(windowsDT,
                textvariable=jett5,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))
jet6 = tk.Entry(windowsDT,
                textvariable=jett6,
                highlightthickness=1,
                highlightcolor='black',
                font=('等线', 13))

jet1.place(x=110, y=80, relwidth=0.21, relheight=0.05)
jet2.place(x=110, y=116, relwidth=0.21, relheight=0.05)
jet3.place(x=110, y=152, relwidth=0.21, relheight=0.05)
jet4.place(x=110, y=188, relwidth=0.21, relheight=0.05)
jet5.place(x=110, y=224, relwidth=0.21, relheight=0.05)
jet6.place(x=110, y=260, relwidth=0.21, relheight=0.05)

tb4 = tk.Button(windowsDT,
                text='返回',
                font=('等线', 13),
                relief='raised',
                width=12,
                height=1,
                command=get_backjt)

tb4.place(x=290, y=560)

# 教务处地区信息统计
jtva = ttk.Treeview(windowsDA)
jtva.place(x=30, y=150, width=400, height=400)
ja = tk.Label(windowsDA, text='生源地信息统计:', font=('华文隶书', 25), bg='green')
ja.place(x=223, y=30)
ja1 = ttk.Combobox(
    windowsDA,
    textvariable=JAvar1,
    values=['不限', '北京', '浙江', '江苏', '上海'],
    # 苇名城, 仙峰寺, 源之宫, 坠落之谷
    # 北京，浙江，江苏，上海
    font=('等线', 14),
    state='readonly')
ja2 = ttk.Combobox(windowsDA,
                   textvariable=JAvar2,
                   values=['不限', '朝阳区', '海淀区', '通州区'],
                   # 城邑, 虎口阶梯, 天守阁
                   # 朝阳区，海淀区，通州区
                   font=('等线', 14),
                   state='readonly')
ja3 = ttk.Combobox(windowsDA,
                   textvariable=JAvar3,
                   values=['不限', '嘉兴市', '温州市', '宁波市', '杭州市'],
                   # 修炼道, 正殿, 内殿, 钟鬼佛堂
                   # 嘉兴市，温州市，宁波市，杭州市
                   font=('等线', 14),
                   state='readonly')
ja4 = ttk.Combobox(windowsDA,
                   textvariable=JAvar4,
                   values=['不限', '南京市', '苏州市'],
                   # 朱桥, 水生宅邸
                   # 南京市，苏州市
                   font=('等线', 14),
                   state='readonly')
ja5 = ttk.Combobox(windowsDA,
                   textvariable=JAvar5,
                   values=['不限', '松江区', '宝山区', '金山区'],
                   # 铁炮要塞, 菩萨谷, 裂缝洞窟
                   # 松江区，宝山区，金山区
                   font=('等线', 14),
                   state='readonly')
ja1.place(x=30, y=90, width=290, height=30)
ja1.current(0)
ja2.current(0)
ja3.current(0)
ja4.current(0)
ja5.current(0)

jab2 = tk.Button(windowsDA,
                 text='返回',
                 font=('等线', 13),
                 relief='raised',
                 width=15,
                 height=2,
                 command=get_backja)
jab2.place(x=500, y=450)

windows.mainloop()
windowsS.mainloop()
windowsT.mainloop()
windowsD.mainloop()
windowsDS.mainloop()
windowsDT.mainloop()
windowsDA.mainloop()
