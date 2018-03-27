# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:12:23 2018
implement the "Median Maintenance" algorithm
Use Min-heap and Max-heap
algorithm: creat a min-heap and max-heap, suppose number of current numbers are 
    n, max-heap contains the lower half of n numbers, with length n/2 (n is even)
    or (n+1)/2 (n is odd), so the head of the max-heap is always median
    
please always remember the position of the element in a heap is always +1 
    compared with the index of the same element, since list is 0 starting
@author: Xu Wen Tao
"""
#from collections import deque
class MaxHeap():
    def __init__(self):
        self.list = [] # add a zero so that the fist element is indexed as 1 
        self.len = 0
        
    def insert(self,x):
        self.list.append(x)
        self.len += 1
        if self.len != 1:
            # make sure heap is valid
            current = self.len  # the position of last element, but index is 1 decreament
            parent = current//2
            if self.list[parent - 1] < x:
                self.swap(parent, current)
                
    def swap(self, p, c):
        # recursively swap until parent is larger than child{}
        print("swap {} and {}".format(p,c))
        i = self.list[c-1]
        self.list[c-1] = self.list[p-1]
        self.list[p-1] = i
        if p > 1:
            parent = p//2
            if self.list[parent -1] < self.list[p-1]:
                self.swap(parent, p)
                
    def bubbleup(self, i):
        # the current position i is empty , recursively move the child up
        #   move the larger child up until position i have no child
        # now self.list[0] is actually self.list[1] before popup, so we minus 1
        #    when we index current self.list
        leftchild = i*2 
        rightchild  = i*2 + 1
        if leftchild > self.len: # there is no child, so insert the last element to this position
            self.list[i - 1] = self.list[self.len-1]
            del self.list[self.len-1]
            self.len -= 1
            parent = i//2
            if self.list[parent-1] < self.list[i - 1]:
                self.swap(parent, i)
            #pass # there is no child
        elif leftchild == self.len:  # only one child, just replace parent with child
            self.list[i-1] = self.list[leftchild - 1]
            del self.list[leftchild - 1]
            self.len -= 1
        elif rightchild == self.len: # only two child, and right child is the last element
            if self.list[rightchild-1] >= self.list[leftchild - 1]:
                self.list[i - 1] = self.list[rightchild - 1]
                
            else: 
                self.list[i - 1] = self.list[leftchild - 1]
                self.list[leftchild - 1] = self.list[rightchild - 1]
            del self.list[rightchild - 1]
            self.len -= 1
        else: # left child < self.len - 1
            if self.list[rightchild-1] >= self.list[leftchild - 1]:
                self.list[i - 1] = self.list[rightchild - 1]
                self.bubbleup(rightchild)
            else: 
                self.list[i - 1] = self.list[leftchild - 1]
                self.bubbleup(leftchild)
            
    def pophead(self):
        # pop out head
        if self.len == 0:
            raise ValueError('Cannot delete empty heap!')
        r = self.list[1-1] # root
        if self.len == 1: # empty heap
            del self.list[0]
            self.len -= 1
        elif self.len == 2:
            self.list[0] = self.list[1]
            del self.list[1]
            self.len -= 1
        else:
            self.bubbleup(1)
        return r
                
class MinHeap():
    def __init__(self):
        self.list = [] # add a zero so that the fist element is indexed as 1 
        self.len = 0
        
    def insert(self,x):
        self.list.append(x)
        self.len += 1
        if self.len != 1:
            # make sure heap is valid
            current = self.len  # the position of last element, but index is 1 decreament
            parent = current//2
            if self.list[parent - 1] > x:
                self.swap(parent, current)
                
    def swap(self, p, c):
        # recursively swap until parent is larger than child{}
        print("swap {} and {}".format(p,c))
        i = self.list[c-1]
        self.list[c-1] = self.list[p-1]
        self.list[p-1] = i
        if p > 1:
            parent = p//2
            if self.list[parent -1] > self.list[p-1]:
                self.swap(parent, p)
                
    def bubbleup(self, i):
        # the current position i is empty , recursively move the child up
        #   move the larger child up until position i have no child
        # now self.list[0] is actually self.list[1] before popup, so we minus 1
        #    when we index current self.list
        leftchild = i*2 
        rightchild  = i*2 + 1
        if leftchild > self.len: # there is no child, so insert the last element to this position
            self.list[i - 1] = self.list[self.len-1]
            del self.list[self.len-1]
            self.len -= 1
            parent = i//2
            if self.list[parent-1] > self.list[i - 1]:
                self.swap(parent, i)
            #pass # there is no child
        elif leftchild == self.len:  # only one child, just replace parent with child
            self.list[i-1] = self.list[leftchild - 1]
            del self.list[leftchild - 1]
            self.len -= 1
        elif rightchild == self.len: # only two child, and right child is the last element
            if self.list[rightchild-1] <= self.list[leftchild - 1]:
                self.list[i - 1] = self.list[rightchild - 1]
                
            else: 
                self.list[i - 1] = self.list[leftchild - 1]
                self.list[leftchild - 1] = self.list[rightchild - 1]
            del self.list[rightchild - 1]
            self.len -= 1
        else: # left child < self.len - 1
            if self.list[rightchild-1] <= self.list[leftchild - 1]:
                self.list[i - 1] = self.list[rightchild - 1]
                self.bubbleup(rightchild)
            else: 
                self.list[i - 1] = self.list[leftchild - 1]
                self.bubbleup(leftchild)
            
    def pophead(self):
        # pop out head
        if self.len == 0:
            raise ValueError('Cannot delete empty heap!')
        r = self.list[1-1] # root
        if self.len == 1: # empty heap
            del self.list[0]
            self.len -= 1
        elif self.len == 2:
            self.list[0] = self.list[1]
            del self.list[1]
            self.len -= 1
        else:
            self.bubbleup(1)
        return r

t = [1,5,3,0,9,4, 7,2,11,6]
mh = MinHeap()
#min_heap = MinHeap()
for e in t:
    mh.insert(e)
    #min_heap.insert(e)
print(mh.list)
#print(min_heap.list)
                
            
            