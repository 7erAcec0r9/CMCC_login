import os
import sys
import tkinter
from tkinter import ttk

import conf
import module

ldconfig = {}


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def get_id():
    global ldconfig
    ldconfig = conf.load_config()
    if flag.get() == 3:
        var2.set('您的上网IP为：' + ldconfig['cellphone_ip'] + '  上网账号：' + ldconfig['usr_name'])
    else:
        var2.set('您的上网IP为：' + module.get_ip(flag.get()) + '  上网账号：' + ldconfig['usr_name'])
    check()


def connect():
    global ldconfig
    ldconfig = conf.load_config()
    if flag.get() == 0:
        var1.set('请先选择上网方式')
    elif flag.get() == 3:
        var1.set(module.connect(ldconfig['cellphone_ip'],
                                ldconfig['usr_name'],
                                ldconfig['usr_pwd'],
                                ldconfig['operator']))
    else:
        var1.set(module.connect(module.get_ip(flag.get()),
                                ldconfig['usr_name'],
                                ldconfig['usr_pwd'],
                                ldconfig['operator']))


def check():
    global ldconfig
    ldconfig = conf.load_config()
    if flag.get() == 0:
        var1.set('请先选择上网方式')
    elif flag.get() == 3:
        var1.set(module.check(ldconfig['cellphone_ip']))
    else:
        var1.set(module.check(module.get_ip(flag.get())))


def disconnect():
    global ldconfig
    ldconfig = conf.load_config()
    if flag.get() == 0:
        var1.set('请先选择上网方式')
    elif flag.get() == 3:
        var1.set(module.disconnect(ldconfig['cellphone_ip']))
    else:
        var1.set(module.disconnect(module.get_ip(flag.get())))


def config():
    window_config = tkinter.Toplevel(window)
    window_config.geometry('300x200')
    window_config.iconbitmap(resource_path('259800440fb1a3aa40a3f60da85822cff2aaba97.ico'))
    window_config.title('CONFIG')

    def cfm():
        pwd = usr_pwd.get()
        name = usr_name.get()
        cell_ip = cellphone_ip.get()
        operator = op_box.get()
        conf.write_config(name, pwd, cell_ip, operator)
        ld()
        get_id()

    def ld():
        global ldconfig
        ldconfig = conf.load_config()
        usr_name.set(ldconfig['usr_name'])
        usr_pwd.set(ldconfig['usr_pwd'])
        cellphone_ip.set(ldconfig['cellphone_ip'])
        if ldconfig['operator'] == 'njupt':
            op_box.current(0)
        elif ldconfig['operator'] == 'cmcc':
            op_box.current(1)
        elif ldconfig['operator'] == 'chinanet':
            op_box.current(2)

    usr_name = tkinter.StringVar()  # 将输入的注册名赋值给变量
    tkinter.Label(window_config, text='用户名： ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_usr_name = tkinter.Entry(window_config, textvariable=usr_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_usr_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    usr_pwd = tkinter.StringVar()
    tkinter.Label(window_config, text='密码： ').place(x=10, y=50)
    entry_usr_pwd = tkinter.Entry(window_config, textvariable=usr_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)

    cellphone_ip = tkinter.StringVar()
    tkinter.Label(window_config, text='手机ip： ').place(x=10, y=90)
    entry_cellphone_ip = tkinter.Entry(window_config, textvariable=cellphone_ip)
    entry_cellphone_ip.place(x=130, y=90)

    op_box = ttk.Combobox(window_config)
    op_box.place(x=130, y=130)
    op_box['value'] = ('njupt', 'cmcc', 'chinanet')
    op_box.current(1)
    tkinter.Label(window_config, text='Operator: ').place(x=10, y=130)

    btn_confirm = tkinter.Button(window_config, text='Confirm', command=cfm)
    btn_load = tkinter.Button(window_config, text='Load', command=ld)
    btn_confirm.place(x=180, y=170)
    btn_load.place(x=70, y=170)


window = tkinter.Tk()

window.title('校园网工具箱')
window.iconbitmap(resource_path('259800440fb1a3aa40a3f60da85822cff2aaba97.ico'))
window.geometry('500x200')

var1 = tkinter.StringVar()
var2 = tkinter.StringVar()
flag = tkinter.IntVar()
flag.set(0)
l1 = tkinter.Label(window, text='感谢使用南京邮电大学校园网工具箱', fg='black', font=('Arial', 12), width=50, height=2)
l2 = tkinter.Label(window, textvariable=var2, fg='black', font=('Arial', 12), width=50, height=2)
l3 = tkinter.Label(window, textvariable=var1, fg='black', font=('Arial', 12), width=50, height=2)
l4 = tkinter.Label(window, text='上网方式', fg='black', font=('Arial', 12), width=7, height=2)
l1.place(x=20, y=0, anchor='nw')
l2.place(x=20, y=45, anchor='nw')
l3.place(x=20, y=90, anchor='nw')
l4.place(x=20, y=160, anchor='nw')
b1 = tkinter.Button(window, text="CONNECT", command=connect)
b2 = tkinter.Button(window, text="CHECK", command=check)
b3 = tkinter.Button(window, text="DISCONNECT", command=disconnect)
b4 = tkinter.Button(window, text="CONFIG", command=config)
b1.place(x=22, y=135, anchor='nw')
b2.place(x=215, y=135, anchor='nw')
b3.place(x=380, y=135, anchor='nw')
b4.place(x=300, y=135, anchor='nw')
r1 = tkinter.Radiobutton(window, text='有线网络', variable=flag, value=1, command=get_id)
r2 = tkinter.Radiobutton(window, text='无线网络', variable=flag, value=2, command=get_id)
r3 = tkinter.Radiobutton(window, text='手机登录', variable=flag, value=3, command=get_id)
r1.place(x=120, y=170, anchor='nw')
r2.place(x=240, y=170, anchor='nw')
r3.place(x=380, y=170, anchor='nw')
window.mainloop()
