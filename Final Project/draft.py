#%s is used as a placeholder for string values you want inject into a formatted string
#%d is used as a placeholder for numeric or decimal values

from datetime import datetime

data_line = []
data_File = []
max_temp = 0.0
min_temp = 0.0
year_temp = open('yearTemp.txt','r') #Assigns contents of yearTemp.txt to 'year_temp'

for item in year_temp:#for however many items in 'year_temp'
  data_line = item.split(',')#split them by a ','
  date = data_line[0]#assigns the date to index 0
  max_temp = data_line[1]
  min_temp = data_line[2]
  
  max_temp = float(max_temp) / 10.0 * 9/5 +32
  min_temp = float(min_temp) / 10.0 * 9/5 +32
  
  data_line.append(date + str(max_temp) + str(min_temp))
  data_File.append(data_line)
  #print(data_line)
  #print(date)
  #print( '%4.1f' % (max_temp))
  #print('%4.1f' % (min_temp))


def bubbleSort(alist):
  start_time = datetime.now() 
  for num_passes in range(0, len(alist)-1,1):#for num_passes, go through the list for however many records alist has - 1 and increment by 1 (Starts i at index 0)
    for i in range(num_passes):#Starts 'i' at index 0 and moves through the list for the length of num_passes
      if alist[i] > alist[i + 1]:#If value at position 'i' is greater than the value at position 'i + 1' (i+1 is the next position after the first, so position 0, 0 + 1 is 1)
        temp = alist[i]#store the value at position [i] in the variable 'temp'
        alist[i] = alist[i + 1]#then change the variable 'alist[i]' at position 'i' to the value of the variable 'alist[i+1] at position 'i + 1' 
        alist[i + 1] = temp#then the value of position [i+1] is changed to the value stored in 'temp'
  return alist
  time_elapsed = datetime.now() - start_time 
  print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

def printList(alist):
    count = 0
    for x in range(len(alist)):#for the number of records in 'alist'
        if count % 10 == 0:#prints out every 10th record
            print()
        print("%4s" % alist[x])#comment this out , end = " "
        count = count + 1

def main():
    print("Unsorted")
    printList(data_File)
    data_file = bubbleSort(data_File)
    print()
    print("Sorted")
    printList(data_File)

main()









