#%s is used as a placeholder for string values you want inject into a formatted string
#%d is used as a placeholder for numeric or decimal values

import time

data_line = []
date_list = []
max_temp_list = []
min_temp_list = []

data_File = []

#year_temp = open('FinalTablex.txt','r') #Assigns contents of yearTemp.txt to 'year_temp'
year_temp = open('yearTemp.txt','r') #Assigns contents of yearTemp.txt to 'year_temp'

for item in year_temp:#for however many items in 'year_temp'
  data_line = item.split(',')#split them by a ','
  date = data_line[0]#assigns the date to index 0, and to the 'data_line' list
  max_temp = data_line[1]
  min_temp = data_line[2]
 # Convert from Celsius to Fahrenheight
  max_temp = float(max_temp) % 10.0 * 9/5 + 32
  min_temp = float(min_temp) % 10.0 * 9/5 + 32
  
 
  
  date_list.append(date)
  max_temp_list.append(max_temp)
  min_temp_list.append(min_temp)
  
  data_File.append(date_list)
  data_File.append(max_temp_list)
  data_File.append(min_temp_list)


  print( '%4.1f' % (max_temp))
  print('%4.1f' % (min_temp))

#Bubble_Sort
def bubbleSort(alist):
  t1 = time.time()
  for num_passes in range(0, len(alist)-1,1):#Go through the list for however many records alist has - 1 and increment by 1 (Starts i at index 0)
    for i in range(0, len(alist) -1, 1):#Starts 'i' at index 0 and moves through the list for how ever many records are in 'alist'
      if alist[i] > alist[i + 1]:#If value at position 'i' is greater than the value at position 'i + 1' (i+1 is the next position after the first, so position 0, 0 + 1 is 1)
        temp = alist[i]#store the value at position [i] in the variable 'temp'
        alist[i] = alist[i + 1]#then change the variable 'alist[i]' at position 'i' to the value of the variable 'alist[i+1] at position 'i + 1' 
        alist[i + 1] = temp#then the value of position [i+1] is changed to the value stored in 'temp'
  t2 = time.time()
  print()
  print("Sorted Bubble list")
  print('Time taken: ', t2 - t1)
  return alist
  

#Shell_Sort
def shellSort(alist):
    t1 = time.time()
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)
        #print("After increment of size", sublistCount, "the list is")
        #printList(alist)
        sublistCount = sublistCount // 2
    t2 = time.time()
    print('Time Taken: ', t2-t1)
    
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap and \
              alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue
    
###################################################################
def printList(alist):
    count = 0
    for x in range(len(alist)):#for the number of records in 'alist'
        if count % 10 == 0:#prints out every 10th record
            print()
        print("%4s" % alist[x])#alist[x]???
        count = count + 1

###################################################################
def main():
    print("Unsorted list")
    printList(data_File)#Prints unsorted list
    bubble_sort = bubbleSort(data_File)#passes in 'data_File' to 'alist'
   # printList(data_File)#passes in 'data_File' to 'alist', prints sorted Bubble List
    print()
    
    #printList(data_File)#passes in 'data_File' to 'alist'
    shell_sort = shellSort(data_File)#prints sorted Shell list
    print()
    print('Sorted Shell list')
    print("find 20040106 in sorted list")
    #for x in range(len(data_File)):
      #if data_File[0][x] == '20040106':
        #print("Found")
        
    print(data_line[0], data_line[1], data_line[2])
    data_File[data_File.index(20040106)][0]
    data_File[data_File.index(20040106)][1]
    #printList(data_File)#Prints sorted list
    #user_choice = 0
    #while user_choice != '1':
      #user_choice = input('Enter year to see temps, hit 1 to end program. ')
    

main()









