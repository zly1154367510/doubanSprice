#-*- coding:utf-8 -*-
choice = -1

menustr="\n"
menustr+="\n1:输入学生成绩"
menustr+="\n2:显示学生成绩"
menustr+="\n3:显示平均分"
menustr+="\n4:退出程序"
message = {}
def in_grade():
    print("录入成绩")
    name = raw_input("姓名")
    cj = input("成绩")
    message[name] = cj
    return 0


def show_grade():
    print ("显示成绩")
    for key, value in message.items():
        print "[" + `key` + "," + `value` + "]\n"
    return  0


def show_avg(lst):
    print("显示平均分")
    hex = 0
    i = 0
    for key, value in message.items():
        hex += float(value)
        i += 1
    print "平均分为" + `hex / i`
    return  0

def quit_pro():
    print("退出程序")
    return  0


print menustr

while True:
    chiose = input("请输入所需功能编号")
    if chiose == 1:
        in_grade()
    elif chiose == 2:
        show_grade()
    elif chiose == 3:
        show_avg()
    elif chiose == 4:
        quit_pro()
        break;



