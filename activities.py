def arb_args(*args):
    for a in args:
        print(a)


def inner_func(x,y):
    def inner_1():
        return x+y
    def inner_2():
        return x-y
    print(inner_1()+inner_2())

def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

def sum_n_product(x,y):
    return x+y, x*y

alias_arb_args = arb_args

def arb_mean(*args):
  total = 0
  for a in args:
    total += a
  print(a/len(args))

def arb_longest_string(*args):
  long = 0
  longest = ""
  for a in args:
    if len(a) > long:
      long = len(a)
      longest = a
  return longest


# Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.

# Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

unsorted_list= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 
sorted_list= sorted(unsorted_list, key=lambda x: x[1])
print(sorted_list)

# Write a lambda function to cube every element of a list. Original list: [3,6,9,2] List after lambda function: [27,216,729,8]
cubed = lambda x: [i**3 for i in x]
print(cubed([3,6,9,2]))

# Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
even_odd = lambda x: True if x%2 == 0 else False
print([even_odd(x) for x in [3,6,9,2]])

# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).
nums = [i for i in range(1,101)]
print(nums)

# Use a dictionary comprehension to count the length of each word in a sentence.
sent = "The quick brown fox jumped over the fence."
print({word:len(word) for word in sent.split()})