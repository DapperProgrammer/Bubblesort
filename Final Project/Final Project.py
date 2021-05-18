#%s is used as a placeholder for string values you want inject into a formatted string
#%d is used as a placeholder for numeric or decimal values

import time
data_line = []
data_File = []
max_temp = 0.0
min_temp = 0.0
year_temp = open('yearTemp.txt','r') #Assigns contents of yearTemp.txt to 'year_temp'

for item in year_temp:
  data_line = item.split(',')
  year = data_line[0]
  max_temp = data_line[1]
  min_temp = data_line[2]
  
  max_temp = float(max_temp) / 10.0 * 9/5 +32
  min_temp = float(min_temp) / 10.0 * 9/5 +32
  
  data_line.append(year + str(max_temp) + str(min_temp))
  data_File.append(data_line)


def bubbleSort(alist):
    swap = True
    passNum = len(alist) - 1  #Passnum == length of the list minus 1
    while swap: # While True
        swap = False
        for i in range(passNum): # for length of passNum  
            if alist[i] > alist[i + 1]:  # if record i greater than itself + 1
                swap = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        #passnum = passnum - 1
    return alist

def printList(alist):
    count = 0
    for x in range(len(alist)): # number of records in data file
        
        if count % 10 == 0:
            print()
        print("%4s" % alist[x])  # comment this out , end = " "
        count = count + 1

def main():
    print("unsorted")
    printList(data_File)
    data_file = bubbleSort(data_File)
    print("Sorted")
    printList(data_File)

main()








