"""""
Stanford - Divide and Conquer Algorithms - Challenge 3
by James Kwon Lee (v8.07.22)

Challenge brief:
    1 - Sort list of 10000 numbers using Quick Sort.
    2 - Count number of comparisons made between the pivot and elements in the numbers list.
"""

comparisons = 0


def main():

    array_input = open("QuickSort.txt").readlines()
    array_input = list(map(int, array_input))

    start_index = 0
    end_index = len(array_input) - 1
    result = quick_sort(array_input, start_index, end_index)

    print("final comparisons: ", comparisons)

    return result


def pick_pivot(array, start_index, end_index):

    if len(array[start_index:(end_index + 1)]) % 2 != 0:
        middle_index = len(array[start_index:(end_index + 1)]) // 2
    else:
        middle_index = (len(array[start_index:(end_index + 1)]) // 2 - 1)

    first_ele = array[start_index]
    middle_ele = array[start_index + middle_index]
    last_ele = array[end_index]

    if first_ele > middle_ele > last_ele or last_ele > middle_ele > first_ele:
        return middle_index + start_index

    elif first_ele > last_ele > middle_ele or middle_ele > last_ele > first_ele:
        return end_index

    else:
        return start_index


def partition(array, start_index, end_index):

    global comparisons

    pivot_index = pick_pivot(array, start_index, end_index)
    pivot = array[pivot_index]

    # pre-process step - pivot element is swapped with first element of array
    temp = array[pivot_index]
    array[pivot_index] = array[start_index]
    array[start_index] = temp

    i = start_index + 1

    comparisons += (end_index - start_index)

    for j in range(start_index + 1, end_index + 1):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i = i + 1

    temp = array[start_index]
    array[start_index] = array[i - 1]
    array[i - 1] = temp

    return i - 1


def quick_sort(array, start_index, end_index):

    if len(array[start_index:(end_index + 1)]) <= 1:
        return array

    if start_index < end_index:
        pivot_index = partition(array, start_index, end_index)
        quick_sort(array, start_index, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end_index)

    return array


if __name__ == '__main__':
    main()

