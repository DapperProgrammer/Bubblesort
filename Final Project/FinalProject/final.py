# Calvin Tracy
# CS 222 02
# Final Project
# Date Due: 05072018
# Date Turned in: 05072018
# Program to sort imported data in order by date, convert the min and max temps to farenheight, then ask the user for a date and display its associated temperatures. Finally, prints out the average temperature associated with each month. 


#%s is used as a placeholder for string values
#%d is used as a placeholder for numeric or decimal values

import time

data_line = []
date_list = []
max_temp_list = []
min_temp_list = []
average_temp = {}

data_Fields = []
data_File = []
bubble_sort = [] # This will hold the bubble sorted list

year_temp = open('yearTemp1.txt','r') #Assigns contents of yearTemp.txt to 'year_temp'

for item in year_temp:#for however many items in 'year_temp'
  data_line = item.split(',')#split them by a ','
  date = data_line[0]#assigns the date to index 0, and to the 'data_line' list
  max_temp = data_line[1]
  min_temp = data_line[2]
  
  #Convert from Celsius to Fahrenheight
  max_temp = ((float(max_temp) / 10.0) * 9/5) + 32.0
  min_temp = ((float(min_temp) / 10.0) * 9/5) + 32.0
  
  #Uses 'format' to round the temperatures to an appropriate value
  data_Fields.append(str(date))	#Put date into 'data_Fields'
  data_Fields.append(format(max_temp, '.2f'))	#Put max temp into 'data_Fields'
  data_Fields.append(format(min_temp, '.2f')) #Put min temp into 'data_Fields'
  #print(data_Fields)
  
  data_File.append(data_Fields)
  data_Fields = []

#Bubble_Sort
def bubbleSort(alist):
  count = 0
  t1 = time.time()
  for num_passes in range(0, len(alist)-1,1): #Go through the list for however many records alist has - 1 and increment by 1 (Starts i at index 0)
    for i in range(0, len(alist) -1, 1): #Starts 'i' at index 0 and moves through the list for how ever many records are in 'alist'
      #print("alist[i][0]",alist[i][0])
      if alist[i][0] > alist[i + 1][0]: #If value at position 'i' is greater than the value at position 'i + 1' (i+1 is the next position after the first, so position 0, 0 + 1 is 1)
        # swap date fields
        temp = alist[i][0] #store the value at position [i] in the variable 'temp'
        alist[i][0] = alist[i + 1][0] #then change the variable 'alist[i]' at position 'i' to the value of the variable 'alist[i+1] at position 'i + 1' 
        alist[i + 1][0] = temp #then the value of position [i+1] is changed to the value stored in 'temp'
        # Swap max temp fields
        temp = alist[i][1] #store the value at position [i] in the variable 'temp'
        alist[i][1] = alist[i + 1][1] #then change the variable 'alist[i]' at position 'i' to the value of the variable 'alist[i+1] at position 'i + 1' 
        alist[i + 1][1] = temp #then the value of position [i+1] is changed to the value stored in 'temp'
        # Swap min temp fields
        temp = alist[i][2] #store the value at position [i] in the variable 'temp'
        alist[i][2] = alist[i + 1][2] #then change the variable 'alist[i]' at position 'i' to the value of the variable 'alist[i+1] at position 'i + 1' 
        alist[i + 1][2] = temp #then the value of position [i+1] is changed to the value stored in 'temp'
        count = count + 1
  t2 = time.time()
  print()
  print("Sorted Bubble list")
  print('Time taken: ', t2 - t1)
  print('Number of comparisons:', count)
  return alist
  

#Shell_Sort
def shellSort(alist):
    count = 0
    t1 = time.time()
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)
        #print("After increment of size", sublistCount, "the list is")
        #printList(alist)
        sublistCount = sublistCount // 2
    count = count + 1
    t2 = time.time()
    print()
    print('Shell Sort')
    print('Time Taken: ', t2-t1)
    print('Number of comparisons:', count)
    print()
    
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap and \
              alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue

		
def PythonSort(alist):
    t1 = time.time()
    alist.sort()
    t2 = time.time()
    print()
    print('Python Sort')
    print('Time Taken: ', "%2.2f" % t2-t1)
    print()
    return
	

###################################################################
# Ask user for date input until 'Done' is entered
def userInput(alist):
  date_Found = False
  user_choice = 0
  while user_choice != 'Done':
      user_choice = input('Please enter a date: ')
      for i in range(0, len(alist)):
          count = 0
          if user_choice == alist[i][0]:# If the users date choice which is at index [i][0] is in 'alist' which has the data of 'data_File'
              print()
              print(alist[i][0], alist[i][1], alist[i][2])# Print out that date and its associated temperatures which are: date at [i][0] max temp at [i][1] and min temp at [i][2]
              count = count + 1
              print()
              print('Number of comparisons:', count)
              date_Found = True
              break
      if date_Found is False:
          print('Error: Date:',user_choice, ' not found!')
          print('Number of comparisons:', count)

# Calculate the average temperature for each month in each year
# Initialized average_temp dict at the top
def averageTemp(alist):
  average_temp = {'01':0,
                  '02':0,
                  '03':0,
                  '04':0,
                  '05':0,
                  '06':0,
                  '07':0,
                  '08':0,
                  '09':0,
                  '10':0,
                  '11':0,
                  '12':0,}
				  			  
  for i in range (0, len(alist)):
    month = alist[i][0][4:6]
    average_temp[str(month)] = average_temp[str(month)] + float(alist[i][1])
  for month, value in average_temp.items():
      print('Average temp for month ', month ,"is ", "%3.2f" % (value//len(alist)))

###################################################################
def main():
  bubble_sort = bubbleSort(data_File)#passes in 'data_File' to 'alist'
  shell_sort = shellSort(data_File)#prints sorted Shell list
  PythonSort(data_file)
  
  #print(userInput(data_File))
  #print(averageTemp(data_File))

main()