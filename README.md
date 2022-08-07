# Counting Comparisons Depending on Pivot Selection of Quick Sort Algorithm
by James Kwon Lee (v8.07.22)

## Challenge brief:
    1 - Sort list of 10000 numbers using Quick Sort.
    2 - Count number of comparisons made between the pivot and elements in the numbers list.

## Background:
    - Quick sort, published by Tony Hoare in 1961, involves the partioning of an unsorted group of numbers about a Pivot.
        - Any value less than pivot are partitioned to the left, and values greater than pivot are partioned to the right.
        - The sorting of the left and right lists are called recursively until the base case of a single element list is reached.
    - Time Complexity: Quick Sort can be upper-bounded by O(n log n) or O(n^2) depending on what pivot is chosen.
        - For example, in the worst case, a pivot is selected in which it doesn't allow for the partitioning of the array
            at each recursive step because it is either the lowest are highest element, leading to quadratic time.
        - But a pivot that is approximately the median value of the array will split the array approximately in half at each recursive step, 
            leading to log n performance.
        - One of the best ways to pick the median pivot is by randomly sampling three numbers and assigning the median value from that group as the pivot.

## Psuedocode:
    1 - Pick an approximately median-value (middle 50%) pivot:
            - From input list, select the first element, last element, and middle element.
            - compare the three values and output the median value, assigning it as the pivot.
    2 - Partition around the pivot:
            - Split up list so that elements less than pivot are partitioned to the left and greater than pivot to the right.
    3 - Recursively sort the left list and right list.
    4 - Count the comparisons:
            - Specifically, count the number of times the pivot is compared to each of the other elements in the list.
            - Dismiss counting comparisons involving the selection of the pivot
                --it's a collection of if-else statements that can be suppressed, for now, due to its constant running time.

## Personal Challenges:
    1 - Implementing Quick Sort was easy because it was elegantly designed and explained by its creator.
    2 - What was hard though, was counting the number of comparisons, in Python.
            - With C or C++, I know that pointers could be used to update count via its reference across functions.
                - But It took me a while to figure that out with Python--I thought merely returning the count from one function and inputting it
                        as a parameter on another would do the trick, but doing this did not update the count properly.
            - As a blanket statement, I learned that most data types pass by value in python, but . . .
                - Certain data types like Lists (aka arrays) are mutable and behave as if passed by reference.
                - https://realpython.com/python-pass-by-reference/
    3 - Also, I struggled with hours of debugging because the middle element at the pivot selection stage did not yield the proper value.
            - Since some kind of pivot was chosen, it allowed for my list to sort properly--but the overall comparison count was inaccurate.
            - Because lists are mutable even when changes are made locally, I was, properly so, slicing the array
                for each recursive call, but, I forgot to adjust the median index by an offset 
                    based on what section of the array was being partitioned.
    4 - Recursion: The typical format of tail-recursion is a function returning the call to itself 
            with some kind of change of value leading to a base case.
            - Because lists are mutable, and since two sorting lists are to be run in parallel, I couldn't use this typical
                format. I didn't copy Quick Sort from the publication, I wanted to figure it out myself, so figuring out how
                 exactly to format the recursion took a while for me to figure out.

## Lessons Learned:
    1 - Divide and Conquer the problem solving. When a code fails to compile, first check overall logic, and if that's correct,
            then break up the code by discrete parts and test in small units at a time.
    2 - Write clean test cases using debugger software and/or well-labeled print statements.
            -It takes a while to do this but it's a good trade-off and saves a lot of time later on.
    3 - Figuring out how to solve the problem could take several minutes. Fixing bugs could take several hours.

## Future Direction:
    1 - The point of the exercise is to show the actual performance gains from choosing the right pivot.
            - So if I have more time, I will allow user to toggle between different pivots so they can see it easily.
            - For now, you can comment out the "pick pivot" subroutine and assign the pivot variable with the desired value.

    2 - Random sampling improves with greater sample size, but undoubtedly, a too big of a sample interferes with performance.
            - Thus, I would like to observe performance after sampling from 7, 9, and 13+ points.
                - Values should be many n factors smaller than entire sample, and secondly, are odd so that median selection is simple.

    3 - Use Dictionary to tether associate numerical value with some kind of object. 
            - Allow for the sorting of these objects based on attributes and/or rank.



## SOLVED Comparisons:
    FIRST ELEMENT AS PIVOT: 162085

    LAST ELEMENT AS PIVOT: 164123

    RANDOMIZED-MEDIAN PIVOT: 138382

## Conclusion:
    - As we can see from the results, a randomized pivot selection significantly reduces the number of comparisons made,
        and thus, improves overall running time for the sort.
