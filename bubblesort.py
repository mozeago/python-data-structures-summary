def bubble_sort(elements):
    elements_size = len(elements)
    for k in range(elements_size - 1):
        swapped = False
        for j in range(elements_size - 1 - k):
            if elements[j] > elements[j + 1]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = ["moses", "hannah", "amina", "aisha", "paul", "zainab"]
    bubble_sort(elements)
    print(elements)
