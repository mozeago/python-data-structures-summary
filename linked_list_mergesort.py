def merge_two_sorted_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    # i is the pointer for list a and j for list b
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    left_list = unsorted_list[:mid]
    right_list = unsorted_list[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge_two_sorted_lists(left_list, right_list)


if __name__ == "__main__":
    unsorted_list = [34, 56, 87, 5, 24, 10, 78]
    print(merge_sort(unsorted_list))
