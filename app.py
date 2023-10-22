#function que retorna o enesimo da sequência de Fibonacci 
def enesimo(n):
    if n==1 or n==2:
        return 1
    else:
        return enesimo(n-1) + enesimo(n-2)
print(enesimo(10))
        
        