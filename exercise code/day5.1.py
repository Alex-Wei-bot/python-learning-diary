# fibonacci sequence 注释部分是我自己写的代码，但会报错 SyntaxError: cannot assign to function call 目前还没有理解
# def fib_loop(i):
#     if i<=2:
#         return 2*i-1
#     else:
#         fib_loop(i)=fib_loop(i-1)+fib_loop(i-2)
#         return fib_loop(i)
# i=fib_loop(20)
# print(i)
def fib_loop(n):
    a,b=0,1
    for i in range(n+1):
        a,b=b,a+b
    return a
    
 
for i in range(20):
    print(fib_loop(i),end=' ')