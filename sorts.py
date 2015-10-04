import random
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

def quick_sort_start(alist):
    quick_sort(alist, 0, len(alist) - 1)

def quick_sort(alist, lo, hi):
    if lo < hi:
        # Find the center and recursively sort them
        center = partition(alist, lo, hi)
        quick_sort(alist, lo, center)
        quick_sort(alist, center + 1, hi)

def partition(alist, lo, hi):
    # Choose random pivot for better average case
    pivot = alist[random.randint(lo, hi)]

    # We need Do-Whiles to get to the return in case of duplicate numbers
    # This initial will offset the Do-Whiles when it first starts
    i = lo - 1
    j = hi + 1
    while True:
        # Find larger values on the left side
        i += 1
        while alist[i] < pivot:
            i += 1

        # Find smaller values on the right side
        j -= 1
        while alist[j] > pivot:
            j -= 1

        # If we passed the pivot, return
        # If not swap elements
        if i < j:
            temp = alist[i]
            alist[i] = alist[j]
            alist[j] = temp
        else:
            return j    

def merge_sort_start(alist):
    return merge_sort(alist)

def merge_sort(alist):
    # Recursively breakup the list
    if len(alist) > 1:
        # Break into 2 separate halves
        left_half = alist[:len(alist)/2]
        right_half = alist[len(alist)/2 : ]

        # Recursively sort them
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        # Merge the two sorted halves
        return merge(left_half, right_half)
    return alist

def merge(left_half, right_half):
    merged_list = []

    # Repeatedly add the lower of the two lists
    while left_half and right_half:
        if left_half[0] < right_half[0]:
            merged_list.append(left_half.pop(0))
        else:
            merged_list.append(right_half.pop(0))

    # Add in leftover amounts
    while left_half:
        merged_list.append(left_half.pop(0))
    while right_half:
        merged_list.append(right_half.pop(0))
    return merged_list

def test_not_in_place_sort(name, fn, test, solution):
    failure = False
    original = test[:]
    output = fn(test)
    if output == solution:
        print("\t%s Sort success on %s" % (name, output))
    else:
        failure = True
        print("\t%s Sort failure" % name)
        print("\t Input:\t %s" % original)
        print("\t Outpu:\t %s" % output)
    return failure


def test_in_place_sort(name, fn, test, solution):
    failure = False
    original = test[:]
    fn(test)
    if test == solution:
        print("\t%s Sort success on %s" % (name, test))
    else:
        failure = True
        print("\t%s Sort failure" % name)
        print("\t Input:\t %s" % original)
        print("\t Outpu:\t %s" % test)
    return failure

def test_sort(name, fn, test_fn):
    a = []
    fn(a)
    failure = False
    if a != []:
        failure = True
        print("\t%s Sort failure on empty list" % (name))
    else:
        print("\t%s Sort success on empty list" % (name))

    # Test normal set
    test = [7, 1, 4, 2]
    solution = [1, 2, 4, 7]
    failure = failure or test_fn(name, fn, test, solution)

    # Test normal set
    test = [15, 32, 25, 27, 28, 32, 1, 100]
    solution = [1, 15, 25, 27, 28, 32, 32, 100]
    failure = failure or test_fn(name, fn, test, solution)

    # Test Negative/Duplicates
    test = [-25, -13, 50, 3, 28, 0, -32, 1, 102, 50]
    solution = [-32, -25, -13, 0, 1, 3, 28, 50, 50, 102]
    failure = failure or test_fn(name, fn, test, solution)

    if failure: 
        print("%s Sort Test FAILED" % (name))
    else:
        print("%s Sort Test SUCCESS" % (name))


def main():
    test_sort("Insertion", insertion_sort, test_in_place_sort)
    test_sort("Selection", selection_sort, test_in_place_sort)
    test_sort("Quick", quick_sort_start, test_in_place_sort)
    test_sort("Merge", merge_sort_start, test_not_in_place_sort)

if __name__ == "__main__":
    main()



