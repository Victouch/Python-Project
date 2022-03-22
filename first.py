#21-03-2022
#ITERATOR
"""
An iterator has both __iter__() and __next__() method.
you could call the next method on an iterator to get the next value.
to make any container object to be 
"""

from pkg_resources import yield_lines


name = "Leonard"
# for x in name:
#     print(name)

# it = iter(name)
# print(name[0])

# class MyOwnIterator:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.index = 0   #len(self.data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == len(self.data):
#             raise stop iteration
        


#GENERATOR
"""
genarators possess the next() and iter() method automatically.
A function that possess the yield statement automatically becomes a generator
A generator remembers the state of your loop
"""
# def iterator_simplified(data):
#     for x in range(len(data)):
#         yield data[x]


# gen = iterator_simplified("leo")
# print(next(gen))
   

#GENERATOR EXPRESSION
num = [2,4,6,8]
# print(sum((x*x for x in num)))
#sum is for iterables

# def add(*args):
#     return sum(args + args + args + args)

# print(add(2, 3, 4))


name = "zach"
namy =name[::-1]
print(list(namy[x] for x in range(len(namy))))
def gen_created(*data):
    for x in range(len(data)):
        yield data[x]

gen = gen_created(list("zach"[::-1]))
print(next(gen))
