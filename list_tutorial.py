if __name__ == "__main__":
    data_list = ['a', 'e', 'i', 'o', 'i', 'u']

    # element 'i' is searched
    index = data_list.index('i')

    # index is printed
    print('The index of e: {}'.format(index))

    # list remove
    del data_list[0]
    print('data_list:', data_list)
    data_list.remove('e')
    print('data_list:', data_list)

    # apply
    target_sort = ['2', '1', '3', '8', '0']
    oringin = ['0', '1', '2', '3', '8']
    result = sorted(oringin, key=lambda x: target_sort.index(x))
    print(result)
