# Sorting Drill
#
# By Alex Colby
#
# Demonstrates a bubble, selection, and insertion sort

# define sorting function that takes three lists as arguments
def mySort(myList1,myList2,myList3):
    # bubble sort on list 1
    for passNum in range(myLen1-1,0,-1):
        for i in range(passNum):
            if myList1[i] > myList1[i+1]:
                temp = myList1[i]
                myList1[i] = myList1[i+1]
                myList1[i+1] = temp

    # selection sort on list 2
    for fillslot in range(myLen2-1,0,-1):
        maxPosition = 0
        for position in range(1,fillslot+1):
            if myList2[position] > myList2[maxPosition]:
                maxPosition = position

            temp = myList2[fillslot]
            myList2[fillslot] = myList2[maxPosition]
            myList2[maxPosition] = temp

    # insertion sort on list 3
    for index in range(1,myLen3):
        currentValue = myList3[index]
        position = index

        while position > 0 and myList3[index-1] > currentValue:
            myList3[position] = myList3[position-1]
            position = position - 1

        myList3[position] = currentValue
            
# define lists and list lengths
myList1 = [67, 45, 2, 13, 1, 998]
myList2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
myList3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
myLen1 = len(myList1)
myLen2 = len(myList2)
myLen3 = len(myList3)

# print unsorted lists
print("Unsorted list 1: {}".format(myList1))
print("Unsorted list 2: {}".format(myList2))
print("Unsorted list 3: {}".format(myList3))
print("\nSorting lists...\n")

# call sort function and pass both lists into it
mySort(myList1,myList2,myList3)

# print sorted lists
print("Sorted list 1: {}".format(myList1))
print("Sorted list 2: {}".format(myList2))
print("Sorted list 3: {}".format(myList3))
