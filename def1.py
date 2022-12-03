def summa(b_first,q,n):
    import numpy as np
    b_prev = b_first
 
    summa = b_prev
    for i in np.arange(1,n):
        b_cur = b_prev*q
        print(b_cur)
     
        summa = summa+b_cur
        b_prev = b_cur 
    return(summa)