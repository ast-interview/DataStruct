# coding: utf-8
'''
利用递归实现斐波那契数列
递归的实质是系统用栈实现的
'''
def Fbi(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return Fbi(i-1) + Fbi(i-2)

if __name__ == "__main__":
    for i in range(1, 12):
        print Fbi(i)