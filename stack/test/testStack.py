# coding: utf-8
class Hello(object):
    def clear(self):
        self = None

if __name__ == "__main__":
    h = Hello()
    m = None
    print type(h), type(m)
    print h, m
    h.clear()
    print type(h)
    print h