'''
还是不懂11.11
为什么这个例子不能print（double（2））

#breakpoint()


def dec(f):
    return 3

@dec
def double(x):
    return x*2
'''
def dec(f):
    def double(x):
        return x * 2
    return double
'''

x=4
print(double(x))
print(type(double))
'''




