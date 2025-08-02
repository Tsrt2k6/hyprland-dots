def range_of_list(store):
    return max(store) - min(store)




if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)