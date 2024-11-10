
'''
一共写了3种斐波那契数列，本质上是迭代和递归

我自己编的错的版本
def feibonaq():
    if n <= 1:
        return n=1 使用 return 时，它需要一个值或表达式来返回，而不能是一个赋值语句。
    f(n)=f(n-1)+f(n-2)
n=input()
 print (n)

''''''

''' '''
AI改的错的版本，我并不想只输出n
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a number: "))
print(n.fibonacci())

'''

'''
memo = {}
lis=[]
def fibonacci(n):
    # 检查缓存中是否已有结果
    if n in memo:
        return memo[n]
    # 递归基本情况
    if n <= 1:
        return n
    # 递归计算并存储结果
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    lis=lis.append(fibonacci(n))
    return memo[n]

# 测试
n = int(input())
print(fibonacci,lis)'''



memo = {}
lis = []
#breakpoint()
def fibonacci(n):
    # 检查缓存中是否已有结果
    if n in memo:
        return memo[n]
    # 递归基本情况
    if n <= 1:
        memo[n] = 1
        lis.append(memo[n])  # 在基本情况时加入到 lis
        return memo[n]
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    lis.append(memo[n])
    return memo[n]
    # 将结果加入列表
    #lis=lis.append(memo[n])，list.append() 是 list 类型的一个方法，
    # .append(),而不是append（），是因为它是list的方法，它用于操作列表对象的内容。用“”append返回的是None

n = int(input("请输入斐波那契数列的项数（迭代写法）："))
fibonacci(n)
print(lis)
print(memo[n])

#print("斐波那契数列：", " ".join(map(str, lis)))#转换成字符串了，也可以直接输出列表

'''
l=[]
a=int(input("斐波那契数列for的写法1:",))
for j in range(2,a+1):#这里因为是左开右闭，如果不加1就会少，因为是从0开始的，得根据题目调整
    if j<=1:
        l[j]=1
        l.append(1)
        #l.append(m[j])
    l[j]=l[j-1]+l[j-2]
    l.append(l[j])
print(l2)

'''

''' 
l = []  # 空列表
a = 5
for j in range(2, a):  # 从索引2开始
    l[j] = 1  # 错误，列表长度不足，无法直接修改l[2]
    

'''
l = [1, 1]  # 初始化前两个斐波那契数
a = int(input("斐波那契数列for的写法1:"))
for j in range(2, a+1):  # 这里从2开始，计算后续项，不需要再判断
    l.append(l[j - 1] + l[j - 2])  # 根据递推公式计算当前项并添加到列表

print(l)

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(c):
    # 基本情况
    if c <= 1:
        return c
    # 递归计算
    return fibonacci(c - 1) + fibonacci(c - 2)

# 测试
c = 10
print(f"Fibonacci({c}) =", fibonacci(c))


def fibonacci(d):
    if d <= 1:
        return d

    x, y = 0, 1
    for _ in range(2, d + 1):#这里直接用了占位符
        x, y = y, x + y
    return y

d = 10
print(f"Fibonacci({d}) =", fibonacci(d))
