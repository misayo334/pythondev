def test(x,y):  #足し算でまず試してみる
    z = x + y
    return z

def fibo(a): #フィボナッチ数列を返す関数
    if a < 3:
        return 1
    
    else:
        return fibo(a - 1) + fibo(a - 2)
