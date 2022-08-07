def _merge_sort(indices, list):
    Awal = indices[0]
    Akhir = indices[1]
    half_way = (Akhir - Awal) // 2 + Awal
    if Awal < half_way:
        _merge_sort((Awal, half_way), list)
    if half_way + 1 <= Akhir and Akhir - Awal != 1:
        _merge_sort((half_way + 1, Akhir), list)
    sort_sub_list(list, indices[0], indices[1])
    return list

def sort_sub_list(list, Awal, Akhir):
    orig_Awal = Awal
    initial_Awal_second_list = (Akhir - Awal) // 2 + Awal + 1
    list2_first_index = initial_Awal_second_list
    new_list = []
    while Awal < initial_Awal_second_list and list2_first_index <= Akhir:
        first1 = list[Awal]
        first2 = list[list2_first_index]
        if first1 > first2:
            new_list.append(first2)
            list2_first_index += 1
        else:
            new_list.append(first1)
            Awal += 1
    while Awal < initial_Awal_second_list:
        new_list.append(list[Awal])
        Awal += 1
    while list2_first_index <= Akhir:
        new_list.append(list[list2_first_index])
        list2_first_index += 1
    for i in new_list:
        list[orig_Awal] = i
        orig_Awal += 1
    return list

def merge_sort(list):
    return _merge_sort((0, len(list) - 1), list)
