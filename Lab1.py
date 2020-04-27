from collections import Counter
import operator
import json
import argparse
import os.path


# ---------------------------------TASK 1-----------------------------------------------------

def task1(filename):
    if os.path.exists(filename):
        print("Your file was opened successfully! :)")
        with open(filename) as some_text:
            file = some_text.read()
    else:
        print("it is not possible to open file")

    task = file.split()
    complete = Counter(task)
    print(dict(complete))


# ---------------------------------TASK 2-----------------------------------------------------

def task2(filename):
    if os.path.exists(filename):
        print("Your file was opened successfully! :)")
        with open(filename) as some_text:
            file = some_text.read()
        some_text.close()
    else:
        print("it is not possible to open file")

    task = file.split()
    complete = Counter(task)
    print(dict(complete))
    complete1 = dict(complete)
    items = dict(complete.most_common(10))

    for key in items:
        print(key, end=" ")


# ---------------------------------TASK 3-----------------------------------------------------

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def task3(filename):
    data = []
    if os.path.exists(filename):
        print("Your file was opened successfully! :)")
        with open(filename) as f:
            for line in f:
                data.append([int(x) for x in line.split()])
        f.close()
    else:
        print("it is not possible to open file")

    print(data)
    quick_sort(data)
    print(data)

    if os.path.exists("Output.txt"):
        with open('Output.txt', 'w') as fw:
            json.dump(data, fw)
        fw.close()
        print("Result was succesfully written in output.txt")
    else:
        print("it is not possible to open Output.txt")


# ---------------------------------TASK 4-----------------------------------------------------

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def task4(filename):
    data = []
    if os.path.exists(filename):
        print("Your file was opened successfully! :)")
        with open(filename) as f:
            for line in f:
                data.append([int(x) for x in line.split()])
    else:
        print("it is not possible to open file")

    print(data)
    merge_sort(data)
    print(merge_sort(data))


# ---------------------------------FIBONACHI-----------------------------------------------------

def Fibonacci(row_length):
    fib1, fib2 = 0, 1
    for i in range(row_length):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1
    print("End")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='5- Fibonacci')
    parser.add_argument("task", help="Number of task, u want to run", type=int)
    parser.add_argument("input",
                        help="Providing name of input file, text.txt for 1/2 task, numbers.txt for 3 task",
                        type=str)

    args = parser.parse_args()

    # gets number of task from cmd
    task_num = args.task
    task_input = args.input

    # python task1.py 1 text.txt
    if task_num == 1:
        task1(task_input)
    # python task1.py 2 text.txt
    elif task_num == 2:
        task2(task_input)

    # python task1.py 3 numbers.txt
    elif task_num == 3:
        task3(task_input)
    # python task1.py 4 numbers.txt
    elif task_num == 4:
        task4(task_input)
    # python task1.py 5 r
    elif task_num == 5:
        print("Enter number: ")
        n = input()
        answer = list(Fibonacci(int(n)))
        print(answer)
        print("It's ")
        print(answer.__getitem__(len(answer) - 1))
