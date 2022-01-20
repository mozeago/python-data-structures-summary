def bubble_sort(elements):
    elements_size = len(elements)
    for k in range(elements_size - 1):
        for j in range(elements_size - 1):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp



if __name__ == "__main__":
    elements = [3, 67, 45, 23, 9, 11, 75, 20, 1, 2, 8]
    bubble_sort(elements)
    print(elements)
