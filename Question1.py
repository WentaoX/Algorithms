# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def countInves(A):
    '''
    This function is to is to compute the number of inversions in a file given, 
    where the ith row of the file indicates the ith entry of an array.
    the fast divide-and-conquer algorithm is used.
    '''
    with open(A, 'r') as f:
        alist = f.read()
    
    alist = alist.split()
    print(len(alist))
    global inversions
    inversions = int(0)
    dividConquer(alist)
    return inversions
    
   


def dividConquer(alist):
    
    if len(alist) == 0 or len(alist) == 1:
        return alist
    
    else:
        #print('splitting')
        i = len(alist)//2
        alist_left = alist[0:i]
        alist_right = alist[i:]
        
        a = dividConquer(alist_left)
        b = dividConquer(alist_right)
        
        i = 0
        j = 0
        global inversions
        c = []
        while i < len(a)  and j < len(b):
            #print('merge')
            if a[i] <= b[j]:
                c.append (a[i])
                i += 1
            else: 
                c.append(b[j])
                j += 1
                inversions += len(a) - i # number of inversions in split 
           
        while i < len(a):
            c.append(a[i])
            i += 1
            
        while j < len(b):
            c.append(b[j])
            j += 1
            
        return c
            
    
if __name__ == '__main__':
    x = countInves('IntegerArray.txt')
    print(x)
    
