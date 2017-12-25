# coding: utf-8
'''
用栈实现四则运算
@author: Ivnali
@time:   2017/12/25
'''
from stack.main.ChainStack import ChainStack

class Stack(object):

    def __init__(self):
        self.stack = []

    # 入栈
    def push(self, data):
        self.stack.append(data)
    # 出栈
    def pop(self):
        self.stack.pop()
    # 获取栈顶元素
    def getTop(self):
        return self.stack[-1]


class Operate(object):

    def __init__(self):
        pass

    # 判断elem为数字or字符
    def judgeNum(self, data):
        try:
            data = int(data)
        except Exception as e:
            pass
        return data

    # 判断优先级
    def judgePriority(self, data):
        if data in ["*", "%"]:
            return 1
        elif data in ["+", "-", "("]:
            return 0

    # 出栈左括号
    def popLeftPar(self):
        pass

    def logic(self, stack, data, postfixExp):
        if stack:
            top_data = stack.getTop()
            while data in [")"] or self.judgePriority(top_data) >= self.judgePriority(data):
                # 若为右括号或优先级小于等于栈顶元素，栈顶元素出栈，直至优先级>data的优先级
                if top_data != "(":
                    postfixExp = postfixExp + str(top_data)
            stack.push(data)  # 若优先级大于，则data入栈
        else:
            stack.push(data)  # 若为空栈，则入栈
        return postfixExp


    # 中缀表达式转化为后缀表达式
    def convertToPostfix(self, nifixExp):
        stack = Stack()
        postfixExp = ""
        stack = ChainStack()
        for elem in nifixExp:
            if self.judgeNum(elem) is int:
                postfixExp = postfixExp + str(elem)  # 数字直接输出
            else:
                postfixExp = self.logic(stack, elem, postfixExp)

        return postfixExp


if __name__ == "__main__":
    nifixExp = "9+(3-1)*3+10/2"
    oper = Operate()
    print oper.convertToPostfix(nifixExp)
