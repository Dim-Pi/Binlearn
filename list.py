





def bin (x,y) :
    for q in y :
        if not (q in x) :
            return False
    return True






def list_get (lis,x,y):
    if len(lis) > x :
        return lis[x]
    else:
        return y




def blist (lis,x):
    if len(lis) > x :
        return True 
    else:
        return False 




def b_list(x,y):
    for q in x:
        y.append(q)




def b_dict (x,y):
    for q in x :
        y [q] = x[q]




def alist (lis,x,y):
    for q in range (0, x - len(lis) +1 ):
        lis.append (y)



def taf_lis (x,y) :
    q = list()
    b_list (x,q)
    for q10 in y:
        if q10 in q :
            q.remove (q10)
            
    return q 
    





#ew  = [1,2,3,5,7]
#alist(ew ,10,int())

#qqq = 0


