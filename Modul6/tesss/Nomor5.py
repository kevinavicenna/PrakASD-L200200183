def _merge_sort(indices, the_list):
    start = indices[0]
    Akhir = indices[1]
    half_way = (Akhir - start) // 2 + start
    if start < half_way:
        _merge_sort((start, half_way), the_list)
    if half_way + 1 <= Akhir and Akhir - start != 1:
        _merge_sort((half_way + 1, Akhir), the_list)
    sort_sub_list(the_list, indices[0], indices[1])
    return the_list

def sort_sub_list(the_list, start, Akhir):
    orig_start = start
    initial_start_second_list = (Akhir - start) // 2 + start + 1
    list2_first_index = initial_start_second_list
    new_list = []
    while start < initial_start_second_list and list2_first_index <= Akhir:
        first1 = the_list[start]
        first2 = the_list[list2_first_index]
        if first1 > first2:
            new_list.appAkhir(first2)
            list2_first_index += 1
        else:
            new_list.appAkhir(first1)
            start += 1
    while start < initial_start_second_list:
        new_list.appAkhir(the_list[start])
        start += 1
    while list2_first_index <= Akhir:
        new_list.appAkhir(the_list[list2_first_index])
        list2_first_index += 1
    for i in new_list:
        the_list[orig_start] = i
        orig_start += 1
    return the_list

def merge_sort(the_list):
    return _merge_sort((0, len(the_list) - 1), the_list)
