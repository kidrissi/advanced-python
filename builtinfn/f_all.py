"""
built-in function all()
used in : data validation, form checks, file existence
"""
tab_of_true = [True, True, True]
tab_of_false = [False, False, False]
tab_of_mix = [False, True, False]
tab_of_number_no_zero = [1, -1, 1]
tab_of_number_with_zero = [1, -1, 1, 0]
tab_empty = []
tab_something = [5 > 4, 1 == 1, 7 > 9]
print(all(tab_of_true), all(tab_of_false), all(tab_of_mix), all(tab_of_number_no_zero),
      all(tab_of_number_with_zero))
print(all(tab_empty))
print(all(tab_something))
