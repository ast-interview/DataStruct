# coding: utf-8
'''
用栈实现四则运算
1. 将中缀表达式转化为后缀表达式
2. 计算后缀表达式
@author: Ivnali
@time:   2017/12/25
'''

'''
利用列表简单实现栈
'''
class Stack(object):

    def __init__(self):
        self.stack = []

    # 入栈
    def push(self, data):
        self.stack.append(data)

    # 出栈
    def pop(self):
        return self.stack.pop()

    # 获取栈顶元素
    def getTop(self):
        return self.stack[-1]

    # 判断栈是否为空
    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True

'''
中缀表达式转化为后缀表达式 -- 栈用来进出运算的符号
1. 从左向右遍历中缀表达式，若是数字就直接输出进后缀表达式
2. 若是符号，则判断其与栈顶符号的优先级，若为右括号或优先级<=栈顶符号优先级，则栈顶元素依次出栈输出进后缀表达式，直到其优先级>栈顶符号优先级，该符号入栈
3. 重复2步骤，直到遍历完中缀表达式，若此时栈中还有元素，依次出栈进后缀表达式
'''
class Convert(object):

    def __init__(self):
        self.stack = Stack()  # 生成栈

    # 判断elem为数字or字符
    def judgeNum(self, data):
        try:
            data = int(data)
        except Exception as e:
            pass
        return data

    # 判断优先级
    def judgePriority(self, data):
        if data in ["("]:
            return 2
        elif data in ["*", "/"]:
            return 1
        elif data in ["+", "-"]:
            return 0

    # string expression -> list expression  "9+(3-1)*3+10/2" -> ['9', '+', '(', '3', '-', '1', ')', '*', '3', '+', '10', '/', '2']
    def convertToList(self, str_nifixExp):
        data = ""
        list_nifixExp = []
        for s in str_nifixExp:
            if type(self.judgeNum(s)) is int:
                data = data + s  # 多位数
            else:
                if data:
                    list_nifixExp.append(data)
                    data = ""
                list_nifixExp.append(s)
        if data:  # 若以数字结尾，则最后数字也append
            list_nifixExp.append(data)
            data = ""
        return list_nifixExp

    # 判断符号优先级进出栈
    def logic(self, stack, data, postfixExp):
        if not stack.isEmpty():
            top_data = stack.getTop()  # 获取栈顶元素
            while data in [")"] or self.judgePriority(data) <= self.judgePriority(top_data):
                # 若为右括号或优先级小于等于栈顶元素，栈顶元素出栈，直至遇到优先级>data优先级的元素，停止pop
                if top_data != "(":  # pop，直到遇到左括号为止

                    if postfixExp:
                        postfixExp = postfixExp + " " + stack.pop()
                    else:
                        postfixExp = postfixExp + stack.pop()

                    if not stack.isEmpty():
                        top_data = stack.getTop()
                    else:
                        break  # 若为空栈，exit

                elif top_data == "(" and data == ")":  # 匹配左右括号，弹出左括号
                    stack.pop()
                    break
                else:
                    break
            if data not in [")"]:
                stack.push(data)  # 若优先级大于，则data入栈，右括号除外，不入栈
        else:
            stack.push(data)  # 若为空栈，则入栈
        return postfixExp


    # 中缀表达式转化为后缀表达式
    def convertToPostfix(self, nifixExp):
        str_nifixExp = self.convertToList(nifixExp)
        postfixExp = ""
        for elem in str_nifixExp:  # 从左到右遍历表达式
            if type(self.judgeNum(elem)) is int:
                if postfixExp:
                    postfixExp = postfixExp + " " + str(elem)  # 数字直接输出
                else:
                    postfixExp = postfixExp + str(elem)  # 数字直接输出
            else:
                postfixExp = self.logic(self.stack, elem, postfixExp)  # 若为符号，则判断优先级进出栈
        if not self.stack.isEmpty():  # 若后缀表达式到尾，栈中还有元素，则全部pop
            for i in range(len(self.stack.stack)):
                postfixExp = postfixExp + " " + self.stack.pop()
        return postfixExp

'''
计算后缀表达式 -- 栈用来进出运算的数字
1. 从左到右遍历表达式的每个数字和符号
2. 若为数字则进栈，若为符号，则出栈栈顶2个数字，进行运算，结果入栈
3. 重复2，直到栈为空
'''
class CalcPostfix(Convert):

    def __init__(self):
        super(CalcPostfix, self).__init__()
        self.stack = Stack()  # 生成栈

    # 计算后缀表达式
    def logic(self, postfixExp):

        for elem in postfixExp.split():  # 从左到右遍历表达式
            if type(self.judgeNum(elem)) is int:
                self.stack.push(int(elem))  # 若为数字，直接入栈
            else:
                top_data = self.stack.pop()  # 若为符号，取栈顶2个元素，做运算，结果入栈
                second_top_data = self.stack.pop()
                exp = str(second_top_data) + elem + str(top_data)
                result = eval(exp)
                self.stack.push(int(result))
        return self.stack.pop()

if __name__ == "__main__":
    conv = Convert()
    calc = CalcPostfix()
    nifixExp = "9+(3-1)*3+10/2"
    postfix = conv.convertToPostfix(nifixExp)
    print calc.logic(postfix)
