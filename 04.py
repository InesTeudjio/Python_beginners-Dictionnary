# 4. Write a Python script to check if a given key already exists in a dictionary.

def is_key_present(d,x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
      return d
is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},5)
is_key_present({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},100)
