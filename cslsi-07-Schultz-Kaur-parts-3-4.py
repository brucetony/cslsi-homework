# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:12:30 2017

@author: Bruce
"""
import random
import time

foo = random.sample(range(-100, 100), 10)
blah = list(foo)

#Exercise 03

def minSwapSort(array):
    #main=[]
    #if_iter=[]
    for i in range(len(array)):
        #main.append(i)
        j = array.index(min(array[i:]))
        if i != j:
            array[i], array[j] = array[j], array[i]
            #if_iter.append(1)
    #print (len(main))
    #print (len(if_iter))
    return array

minSwapSort(foo)


#Point 1
#This function sorts an array of n integers by identifying the minimum value from
#    i to n-1, assigning it the index j, and swapping the values of array[i] and array[j].
#    In that way, the smallest values are moved to the beginning of the array as the 
#    index i continues down the array and the values are thus sorted.
#    
#The invariant is that for an array (A) of n integers, all values A[:i] are
#    sorted in non-descending order. If array B was the non-descending sorted version of A,
# then B[:i] would be equal to A[:i] for all i. 
#
#Point 2
#There are n comparisons performed in iteration i of the for loop. i must be compared to
# j at every iteration of the length of the array (n).
#
#Point 3
#The array elements are swapped a minimum of 0 times (if the array was already in non-descending order)
# and a maximum of n-1 times (all elements in array were in ascending order EXCEPT the 
# largest element was in the first position).

#Example minimum = [1, 2, 3, 4, 5]
#Example maximum = [5, 1, 2, 3, 4]


#Exercise 04

k = [4, -5, 3, -9, 6]

def min_sum(l, r, array): #Has O(n2)
    if l >= r :
        return 0 
    else:
        return min(min_sum(l + 1, r, array), min_sum(l, r - 1, array), sum(array[l : r]))

        


def min_sum2(array): #Has O(n)
    current_min = array[0] #Set initial min to first value
    ultimate_min = array[0] #Set initial min to first value
    start_index = 0 #First value index
    end_index = 1 #First end value
    for i in range(1, len(array)):
        if array[i] < (current_min + array[i]):
            start_index = i #Change which index starts the new min
        
        current_min = min(array[i], current_min + array[i]) #Find the min!
        
        #MUST be either the new value, or the sum of\
        # previous subarray with new value. Does not necessarily replace global min.
        
        if current_min < ultimate_min:
            ultimate_min = current_min #Replace global min if current is smaller
            end_index = i+1 #Change which index ends the new min
    if end_index > len(array)-1: #So we can use proper notation
        end_index = ''
    return ('The minimum sum of consecutive elements is {} \
which ranges from [{}:{}] of your array.'.format(ultimate_min, start_index, end_index))

print(min_sum(0, 10, blah))
print(min_sum2(blah))

#start_time = time.clock()
#print(min_sum(0, 25, blah))
#print (time.clock() - start_time, "seconds")
#
#start_time = time.clock()
#min_sum2(blah)
#print (time.clock() - start_time, "seconds")


