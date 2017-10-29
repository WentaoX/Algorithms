# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 10:46:56 2017

@author: Xu Wen Tao
"""

def quick_sort(a, start, end,  pivot_select):
    '''
    a: unsorted list
    pivot_select: the way to select pivot
    start: the start index 
    end: the end index
    This function is to is to sort list a, with pivot_select method provided
    '''
    
    if end - start <= 0:
        # end could be smaller than start, for example, when end = len(a), 
        # start could be len(a) + 1 becuase of the i += 1 in teh next for loop
        return a[end]
    else:
        global comparision
        comparision += (end - start)
        if pivot_select == "first":
            # first element is pivot
            pass
        elif pivot_select == "last":
            # last element is pivot
            swap(a, start, end)
            
        elif pivot_select == "median-of-three":
            # from the first, last and middle postiion element, select 
            # median of the three value as pivot
            fe = a[start]
            le = a[end]
            mindex = int((start+end)/2)
            me = a[mindex]
            if (fe <= me <= le) or (le <= me <= fe):
                # me is the median of the three
                swap(a, start, mindex)
            elif (fe <= le <= me) or (me <= le <= fe):
                # le(last element) is the median of the three
                swap(a, start, end)
        l = start
        i = l + 1   
        for j in range(i, end+1):
            if a[j] < a[l]:
                # between a[l+1] and a[i-1], every element is samller than a[l]
                # between a[i] and a[j-1], every element is bigger than a[l]
                swap(a, i, j)
                i += 1
                
        swap(a, i-1, l)
        #print(str(a) + " " + str(i) +  " " + str(j) +  " " + str(l))
    quick_sort(a, l, i-2, pivot_select)
    quick_sort(a, i, j, pivot_select)
            
    
    
def swap(a, i, j):
    '''
    given a list a, and index i and j, swap a[i] with a[j]
    '''
    t = a[i]
    a[i] = a[j]
    a[j] = t



if __name__ == "__main__":
    
    with open("QuickSort.txt", 'r') as f:
        strlist = f.read()
    strlist = strlist.split()
    # each element is string, change it to int
    alist = [int(x) for x in strlist]
    global comparision
    comparision = 0
    #alist = [4,1,2,0,3]
    print(len(alist))
    quick_sort(alist,0,len(alist)-1, "median-of-three")
    print(alist[0:100])
    #print(type(alist))
   # print(len(alist))
    print(comparision)
