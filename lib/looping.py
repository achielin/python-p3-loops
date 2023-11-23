#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
  counter = 10
  while counter > 0:
      print(counter)
      counter += 1
  

def square_integers(int_list):
    # code goes here!
    pass
def square_integers(lst):
    squared_lst = [x**2 for x in lst]
    return squared_lst

def fizzbuzz():
    # code goes here!
     for i in range(1, 101):
       if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
       elif i % 3 == 0:
            print("Fizz")
       elif i % 5 == 0:
             print("Buzz")
       else:
             print (i)
  
