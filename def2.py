def elem(b_first3,q3,n3):
    import numpy as np

    b_prev = b_first3
    for i in np.arange(1,n3):
        b_cur = b_prev*q3
        b_prev = b_cur 
    a=[(b_prev)]
    print (a)