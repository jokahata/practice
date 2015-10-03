
def insertion_sort(alist):
    # Iterate through, swapping from the end of the sorted list to the bottom
    for i in range(1, len(alist)):
        position = i
        while position > 0 and alist[position - 1] > alist[position]:
            temp = alist[position]
            alist[position] = alist[position - 1]
            alist[position - 1] = temp

            position -= 1

def selection_sort(alist):
    length = len(alist)
    # Iterate through entire array, last number will be min element in unsorted set
    for i in range(length - 1):
        min_index = i

        # Find smallest number in unsorted section of array
        for j in range(i + 1, length):
            if alist[j] < alist[min_index]:
                min_index = j

        # Swap only if we didn't already have the min element
        if min_index != i:
            temp = alist[i]
            alist[i] = alist[min_index]
            alist[min_index] = temp



        

def test_sort(name, fn):
    a = []
    fn(a)
    failure = False
    if a != []:
        failure = True
        print("%s Sort failure on empty list" % (name))


    # Test normal set
    a = [15, 32, 25, 27, 28, 32, 1, 100]
    original = a[:]
    fn(a)
    if a != [1, 15, 25, 27, 28, 32, 32, 100]:
        failure = True
        print("%s Sort failure on %s got %s" % (name, original, a))

    # Test Negative/Duplicates
    a = [-25, -13, 50, 3, 28, 0, -32, 1, 102, 50]
    original = a[:]
    fn(a)
    if a != [-32, -25, -13, 0, 1, 3, 28, 50, 50, 102]:
        failure = True
        print("%s Sort failure on %s got %s" % (name, original, a))


    if failure: 
        print("%s Sort Test FAILED" % (name))
    else:
        print("%s Sort Test SUCCESS" % (name))


def main():
    test_sort("Insertion", insertion_sort)
    test_sort("Selection", selection_sort)

if __name__ == "__main__":
    main()



