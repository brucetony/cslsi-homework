# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:49:43 2017

@author: Bruce
"""
#==============================================================================
# Exercise 1a - Recursive LCS function
#==============================================================================

def lcs_rec(str1,str2):
    '''Recursively determine LCS of two strings'''
    if len(str1)==0 or len(str2)==0: # Check if string is empty then stops
        return ''
    elif str1[0]==str2[0]: # Compares the first character of strings
        return str1[0] + lcs_rec(str1[1:], str2[1:]) #Adds letter if matched
    else:
        #Recursively go through both combos
        return max(lcs_rec(str1[1:],str2) , lcs_rec(str1,str2[1:]), key=len)

#S1="AGGTACCCGATC"
#S2="GTAAGAGTACCGATTGATC"
#print(lcs_rec(S1, S2))

#==============================================================================
# Exercise 1c
#==============================================================================

def lcs_d(str1,str2):
    """Create a table with the lengths of LCSs, \
    then work backwards to generate seq"""
    
    if len(str1)==0 or len(str2)==0: # Check if string is empty then stops
        raise ValueError('One string is empty, check your inputs!')
    
    #We need to create an mxn matrix that will track our matches/lengths
    m=len(str1) 
    n=len(str2)
    
    #Initialized every value in matrix to 0
    dp=[[0 for j in range(n+1)] for i in range(m+1)] 
    
    # Now we generate a rules that will track all possible length combos
    # We are only tracking lengths and not the strings themselves
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0 #Base case (top left)
                
            #Move to diagnal and increase length of LCS by 1
            elif str1[i-1]==str2[j-1]: 
                 dp[i][j]= dp[i-1][j-1]+1
            
        #If they don't match, take max value from either above or to the left
            else:
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
 
    
    #Next we want to take the longest lcs and \
    # create the string using the dp table
    
    # Make empty list to store matched characters in
    lcs = []
 
    # Start at our max value (bottom right of table) and iterate up/left
    posx = m
    posy = n
    
    while posx > 0 and posy > 0: #If either reaches 0 then we are done
        # Only append list if we have a match then jump diagonally
        if str1[posx-1] == str2[posy-1]:
            lcs.append(str1[posx-1])
            posx -=1
            posy -=1
        #Follow larger value
        elif dp[posx-1][posy] > dp[posx][posy-1]:
            posx -=1
        else:
            posy -=1
    
    return ''.join(lcs[::-1]) #We worked backwards so reverse order and join

#S1="AGGTACCCGATC"
#S2="GTAAGAGTACCGATTGATC"

#print(lcs_d(S1, S2))

#==============================================================================
# Exercise 2a -
#==============================================================================

def iSmall(alist, i):
    """Finds the ith smallest numbers in an unsorted, 1 dimensional array \
   which uses Quicksort to only sort the partitions that i is in"""
    if i > len(alist) or i < 0: # In case input is outside array range
        raise ValueError('Chosen position is outside the range of the \
list. Please choose a position between 1 and \
the length of the list')
   # Call helper function from start to the end index
    iSmallHelper(alist,0,len(alist)-1, i-1)
    return alist[i-1]

def iSmallHelper(alist,first,last, i):
   # If length of list is greater than 1
   if first<last:
       # Find the splitting point of the array (w.r.t. pivot's true position)
       splitpoint = partition(alist,first,last)

       # Sort left only the list that i is in
       if i in range(first, splitpoint):
           iSmallHelper(alist,first,splitpoint-1, i)
       elif i in range(splitpoint+1, len(alist)):
            iSmallHelper(alist,splitpoint+1,last, i)
       elif i == splitpoint:
            return alist[splitpoint]


def partition(alist, first, last):
    # Choose first element as pivot
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
       # Move the left marker to reach a value greater than pivot
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        #Move the right marker to reach a value less than pivot
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        #If left and right marker has reached each other then we are done
        if rightmark < leftmark:
            done = True
        else:
           # Swap the values pointed by the left and the right marker
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
   # Swap the pivot with the right marker position (final pivot position)
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

   # Position of the right marker is the splitting position
    return rightmark

#S = [5,3,1,7,2,3,1]

#==============================================================================
# Exercise 2b
#==============================================================================

def count_sort(nlist, power):
    '''Sorts using the counting method at the given power of 10 place'''
    radix = 10
    
    #Counting list with length = highest value in the inputList
    count_list = [0] * radix
    
    #Sorted list to return with = length as inputList
    sorted_list = [0] * len(nlist)
    
    #Add 1 to each position in countlist that appears in inputList
    for i in range(len(nlist)):
        digit = (nlist[i]//radix**power)%radix
        count_list[digit] += 1
    
    #Each value is replaced with the sum of itself and the previous value
    for j in range(1, len(count_list)): 
        count_list[j] += count_list[j-1]
    
    #Counting list used to indicate position of each value of inputList
    k = len(nlist)-1
    while k >= 0:
        digit = (nlist[k]//radix**power)%radix
        count_list[digit] -= 1
        sorted_list[count_list[digit]] = nlist[k]
        k-=1
    
    #Iterate for each value
    for i in range(len(nlist)):
        nlist[i] = sorted_list[i]
        
    return sorted_list


def string_sort(some_strings):
    '''Converts strings into numerical values and using count_sort to sort \
    number by each decimal place starting with the Least Significant'''
    stringList = list(some_strings)
    max_length = 0 #Initialize max_length with first
    
    for i in range(len(stringList)):
        if len(stringList[i]) > max_length:
            max_length = len(stringList[i])
        stringList[i] = list(stringList[i])
    
    # Add '-' at end if string is shorter than max length
    for i in range(len(stringList)):
        while len(stringList[i]) < max_length:
            stringList[i].append('-')
    
    letters = ['-','a','b','c', 'd', 'e', 'f', 'g', 'h','i','j','k','l', 'm',\
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    #Dict where each letter a corresponding number
    letter_dict = dict(zip(letters, range(27)))
    
    # Exchange letter values for numerical
    for i in range(len(stringList)):
        for j in range(len(stringList[i])):
            stringList[i][j] = letter_dict[stringList[i][j]]
        stringList[i] = int(''.join(map(str, stringList[i]))) #Combine int
    
    # Make dict to translate our original strings into their numbers   
    input_dict = dict(zip(stringList, some_strings))
    
    max_num = max(stringList) #Find max to set while loop end
    
    power = 0 #Set base power to 0
    while max_num/(10**power) > 0:
        results = count_sort(stringList, power)
        power += 1
    
    #Convert sorted numbers back into strings and output    
    sorted_strings = []
    for number in results:
        sorted_strings.append(input_dict[number])
    
    return sorted_strings
    

test = ["b","cda","db","da","ab","a"]

print(string_sort(test))
