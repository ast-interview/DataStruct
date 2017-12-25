# coding: utf-8
'''
利用栈匹配括号
'''
class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def getTop(self):
        return self.stack[len(self.stack)-1]

    def logic(self, data):
        print "now the data is : " + data
        if self.stack:
            topData = self.getTop()
            if topData == "{" and data == "}":
                self.stack.pop()
            elif topData == "[" and data == "]":
                self.stack.pop()
            elif topData == "(" and data == ")":
                self.stack.pop()
            elif data in ["[", "]", "(", ")", "{", "}"]:
                self.push(data)
        elif data in ["[", "]", "(", ")", "{", "}"]:
            self.push(data)

if __name__ == "__main__":

    l = "[ ( [ ] [ ] ) ]"
    s = Stack()
    for elem in l:
        s.logic(elem)
        print s.stack

    # print s.stack

