def freq_function(elements_list):
    frequency_counter = {}

    for index, value in enumerate(elements_list):
        if value not in frequency_counter:
            frequency_counter[value] = 1
        else:
            frequency_counter[value] += 1

    max_key = -1
    max_value = -1
    for key, value in frequency_counter.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key


def main():
  list1 = [1, 2, 3, 4, 5, 4, 5, 4, 4, 2, 3]
  print(freq_function(list1) == 4)

  list2 = [3, 5, 3, 4, 5, 5, 4, 5, 4, 4, 5]
  print(freq_function(list2) == 5)

  list3 = []
  print(freq_function(list3) == -1) # returns -1 for no values


if __name__ == '__main__':
    main()
