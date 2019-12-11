def frequency_func(elements_list, rev = False):
    frequency_counter = {}

    for index, value in enumerate(elements_list):
        if value not in frequency_counter:
            frequency_counter[value] = 1
        else:
            frequency_counter[value] += 1

    m_key = -1
    m_value = -1
    for key, value in frequency_counter.items():
        if freq_function(value, m_value, rev):
            m_value = value
            m_key = key

    return m_key

def freq_function(value, current, rev):
  if rev: # jeśli szuka najmniejszego występowania
    if current == -1: # przy pierwszym wykonaniu
      return True
    return value < current
  else:
     return value > current


def main():
  list1 = [1, 2, 3, 4, 5, 4, 5, 4, 4, 2, 3]
  print(frequency_func(list1) == 4)
  print(frequency_func(list1, rev=True) == 1)

  list2 = [3, 5, 3, 4, 5, 5, 4, 5, 4, 4, 5]
  print(frequency_func(list2) == 5)
  print(frequency_func(list2, rev=True) == 3)

  list3 = []
  print(frequency_func(list3) == -1) # returns -1 for no values
  print(frequency_func(list3, rev=True) == -1)


if __name__ == '__main__':
    main()
