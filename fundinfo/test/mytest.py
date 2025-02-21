import asyncio

async def task(i):
    print(i)
    
task(1)

# from queue import Queue
# from threading import Thread
# import time

# class ClosableQueue(Queue):
#     SENTINEL=object()
    
#     def close(self):
#         self.put(self.SENTINEL)
    
#     def __iter__(self):
#         while True:
#             item=self.get()
#             try:
#                 if item is self.SENTINEL:
#                     return 
#                 yield item
#             finally:
#                 self.task_done()

# class StoppableWorker(Thread):
#     def __init__(self, func,in_queue,out_queue):
#         super().__init__()
#         self.func=func
#         self.in_queue=in_queue
#         self.out_queue=out_queue
    
#     def run(self):
#         for item in self.in_queue:
#             result=self.func(item)
#             self.out_queue.put(result)    


# download_queue=ClosableQueue()
# resize_queue=ClosableQueue()
# upload_queue=ClosableQueue()
# done_queue=ClosableQueue()
# threads=[StoppableWorker(download,download_queue,resize_queue),
#          StoppableWorker(resize,resize_queue,upload_queue),
#          StoppableWorker(upload,upload_queue,done_queue),
#          ]                        

# for thread in threads:
#     thread.start()

# for _ in range(1000):
#     download_queue.put(object())

# download_queue.close()
# download_queue.join()
# resize_queue.close()
# upload_queue.close()
# upload_queue.join()
# print(download_queue.qsize(),'item finished')

# for thread in threads:
#     thread.join()
    

# my_queue=Queue(1)
# def consumer():
#     time.sleep(0.1)
#     my_queue.get()
#     print('Consumer got 1')
#     my_queue.get()
#     print('Consumer got 2')
#     print('Consumer done')

# thread=Thread(target=consumer)
# thread.start()

# print('Producer putting')
# my_queue.put(object())
# print('Producer put 1')
# my_queue.put(object())
# print('Producer put 2')
# print('Producer done')
# thread.join()



# from threading import Thread
# import time


# class FactorizeThread(Thread):
#     def __init__(self, number):
#         super().__init__()
#         self.number = number

#     def run(self):
#         self.factors = list(factorize(self.number))
#         print(self.factors)


# def factorize(number):
#     for i in range(1, number+1):
#         if number % i == 0:
#             yield i


# numbers = [2139079, 1214759, 1516637, 1852285]
# start = time.time()
# threads = []
# for number in numbers:
#     thread = FactorizeThread(number)
#     thread.start()
#     threads.append(thread)

# for thread in threads:
#     thread.join()

# end = time.time()
# delta = end-start
# print(f'took {delta:.3f} seconds')


# for number in numbers:
#     a=list(factorize(number))
# end = time.time()
# delta = end-start
# print(f'took {delta:.3f} seconds')
# print(a)

# import subprocess

# proc=subprocess.Popen(['sleep','1'])
# while proc.poll() is None:
#     print('Wroking')

# print('Exit status',proc.poll())


# import os
# from threading import Thread
# import random


# class GenericInputData:
#     def read(self):
#         raise NotADirectoryError

#     @classmethod
#     def generate_input(cls, config):
#         raise NotImplementedError


# class GenericWorker:
#     def __init__(self, input_data):
#         self.input_data = input_data
#         self.result = None

#     def map(self):
#         raise NotImplementedError

#     def reduce(self, other):
#         raise NotImplementedError

#     @classmethod
#     def create_workers(cls, input_class, config):
#         workers = []
#         for input_data in input_class.generate_input(config):
#             workers.append(cls(input_data))
#         return workers


# class PathInputData(GenericInputData):
#     def __init__(self, path):
#         super().__init__()
#         self.path = path

#     def read(self):
#         with open(self.path) as f:
#             return f.read()

#     @classmethod
#     def generate_input(cls, config):
#         data_dir = config['data_dir']
#         for name in os.listdir(data_dir):
#             yield cls(os.path.join(data_dir, name))


# class LineCountWorker(GenericWorker):
#     def map(self):
#         data = self.input_data.read()
#         self.result = data.count('a')

#     def reduce(self, other):
#         self.result += other.result


# def execute(workers):
#     threads = [Thread(target=w.map) for w in workers]
#     for thread in threads:
#         thread.start()
#     for thread in threads:
#         thread.join()

#     first, *rest = workers
#     for worker in rest:
#         first.reduce(worker)
#     return first.result


# def mapreduce(worker_class, input_class, config):
#     workers = worker_class.create_workers(input_class, config)
#     return execute(workers)


# def writet_test_files(tmpdir):
#     os.makedirs(tmpdir)
#     for i in range(100):
#         with open(os.path.join(tmpdir, str(i)), 'w') as f:
#             f.write('a'*random.randint(0, 100))


# tmpdir = 'test_input'
# config = {'data_dir': 'test_input'}
# writet_test_files(tmpdir)
# result = mapreduce(LineCountWorker, PathInputData, config)
# print(f'There are {result} lines')


# from collections import defaultdict


# def log_missing():
#     print('Key added')
#     return 0


# current = {'green': 12, 'blue': 3}
# increments = [('red', 5), ('blue', 17), ('orange', 9)]
# result = defaultdict(log_missing, current)
# print('Before:', dict(result))
# for key, amount in increments:
#     result[key] += amount
# print('After:', dict(result))


# from collections import namedtuple, defaultdict
# Grade = namedtuple('Grade', ('score', 'weight'))


# class Subject:
#     def __init__(self):
#         self._grades = []

#     def report_grade(self, score, weight):
#         self._grades.append(Grade(score, weight))

#     def average_grade(self):
#         total, total_weight = 0, 0
#         for grade in self._grades:
#             total += grade.score * grade.weight
#             total_weight += grade.weight
#         return total/total_weight


# class Student:
#     def __init__(self):
#         self._subjects = defaultdict(Subject)

#     def get_subject(self, name):
#         return self._subjects[name]

#     def average_grade(self):
#         total, count = 0, 0
#         for subject in self._subjects.values():
#             total += subject.average_grade()
#             count += 1
#         return total/count


# class Gradebook:
#     def __init__(self):
#         self._students = defaultdict(Student)

#     def get_student(self, name):
#         return self._students[name]


# book = Gradebook()
# albert = book.get_student('Albert Einstein')
# math = albert.get_subject('Math')
# math.report_grade(75, 0.05)
# math.report_grade(65, 0.15)
# math.report_grade(70, 0.8)

# gym = albert.get_subject('Gym')
# gym.report_grade(100, 0.4)
# gym.report_grade(85, 0.6)

# print(albert.average_grade())


# class SimpleGradebook:
#     def __init__(self):
#         self._grades={}

#     def add_student(self,name):
#         self._grades[name]=[]

#     def report_grade(self,name,score):
#         self._grades[name].append(score)

#     def average_grade(self,name):
#         grades=self._grades[name]
#         return sum(grades)/len(grades)
# book=SimpleGradebook();
# book.add_student('Isaac Newton')
# book.report_grade('Isaac Newton',90)
# book.report_grade('Isaac Newton',95)
# book.report_grade('Isaac Newton',85)

# print(book.average_grade('Isaac Newton'))


# import math

# def wave(ampliltude,steps):
#     step_size=2*math.pi/steps
#     for step in range(steps):
#         radians=step*step_size
#         fraction=math.sin(radians)
#         output=ampliltude*fraction
#         yield output

# def transmit(output):
#     if output is None:
#         print(f'Output is None')
#     else:
#         print(f'Output:{output:>5.1f}')

# def run(it):
#     for output in it:
#         transmit(output)

# # run(wave(3.0,8))

# def my_generator():
#     received= yield 1
#     print(f'received={received}')

# it = iter(my_generator())
# output=next(it)
# print(f'output={output}')
# try:
#     next(it)
# except StopIteration:
#     pass

# it = iter(my_generator())
# output=it.send(None)
# print(f'output={output}')
# try:
#     it.send('hello!')
# except StopIteration:
#     pass


# def move(period,speed):
#     for _ in range(period):
#         yield speed

# def pause(delay):
#     for _ in range(delay):
#         yield 0

# def animate():
#     for delta in move(4,5.0):
#         yield delta
#     for delta in pause(3):
#         yield delta
#     for delta in move(2,3.0):
#         yield delta

# def render(delta):
#     print(f'Dlata:{delta:.1f}')

# def run(func):
#     for delta in func():
#         render(delta)
# def animate_composed():
#     yield from move(4,5.0)
#     yield from pause(3)
#     yield from move(2,3.0)
# # run(animate)
# run(animate_composed)


# path='./test/testfolder/my_numbers.txt'
# it=( len(x) for x in open(path))
# roots=((x,x**0.5) for x in it )
# for n in roots:
#     print(n)
# def normalize(numbers):
#     total=sum(numbers)
#     result=[]
#     for value in numbers:
#         percent=100 * value /total
#         result.append(percent)
#     return result

# # visits=[15,35,80]
# # percentages=normalize(visits)
# # print(percentages)

# def read_visits(data_path):
#     with open(data_path) as f:
#         for line in f:
#             yield int(line)

# def normalize_copy(numbers):
#     numbers_copy=list(numbers)
#     total=sum(numbers_copy)
#     result=[]
#     for value in numbers_copy:
#         percent=100*value/total
#         result.append(percent)
#     return result


# def normalize_func(get_iter):
#     total=sum(get_iter())
#     result=[]
#     for value in get_iter():
#         percent=100* value / total
#         result.append(percent)
#     return result

# class ReadVisits:
#     def __init__(self,data_path):
#         self.data_path=data_path
#     def __iter__(self):
#         with open(self.data_path) as f:
#             for line in f:
#                 yield int(line)

# it =read_visits('./test/testfolder/my_numbers.txt')
# # percentages=normalize_copy(it)
# # print(percentages)
# # percentages=normalize_func(lambda: read_visits('./test/testfolder/my_numbers.txt'))
# percentages=normalize_func(lambda: it)

# print(percentages)
# path='./test/testfolder/my_numbers.txt'
# visits=ReadVisits(path)
# percentages=normalize(visits)
# print(percentages)


# from functools import wraps


# def trace(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         print(f'{func.__name__}({args!r},{kwargs!r})'
#               f'->{result}')
#         return result
#     return wrapper

# @trace
# def fibonacci(n):
#     if n  in (0,1):
#         return n
#     return (fibonacci(n-2) + fibonacci(n-1))

# fibonacci(4)
# print(fibonacci)

# import json
# def decode(data,default=None):
#     try:
#         return json.loads(data)
#     except ValueError:
#         if default is None:
#             default={}
#         return default
# foo=decode('bad data')
# # print('Foo:',foo)
# foo['stuff']=5
# bar=decode('also bad')
# bar['meep']=1
# print('Foo:',foo)
# print('Bar:',bar)


# from time import sleep
# from datetime import datetime

# def log(message,when=None):
#     if when is None:
#         when=datetime.now()
#     print(f'{when}:{message}')

# log('hi three')
# sleep(1)
# log('hi here2')
# def print_parameters(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}={value}')

# print_parameters(alpha=1.5,beta=9,gamma=4)


# def remainder(number,divisor):
#     return number % divisor

# my_kwargs={'number':20,'divisor':7}
# print(remainder(**my_kwargs))


# def my_generator():
#     for i in range(10):
#         yield i

# def my_func(*args):
#     print(args)

# it=my_generator()
# # print(type(it))
# my_func(*it)


# def log(message,*values):
#     if not values:
#         print(message)
#     else:
#         values_str=", ".join(str(x) for x in values)
#         print(f'{message}:{values_str}')

# log('my numbers are',1,2)
# log('hi here')
# favorites=[7,3,99]
# log('favorite colors',*favorites)

# def sort_priority(values,group):
#     def helper(x):
#         if x in group:
#             return (0,x)
#         return (1,x)
#     values.sort(key=helper)

# numbers=[8,3,1,2,5,4,7,6]
# group={2,3,5,7}
# sort_priority(numbers,group)
# print(numbers)


# first,second=1,2
# assert first ==1
# assert second ==2

# def my_function():
#     return 1,2

# first,second = my_function()
# assert first ==1
# assert second ==2

# def get_stats(numbers):
#     minimum=min(numbers)
#     maximum=max(numbers)
#     return minimum,maximum

# lengths=[63,73,72,60,66,71,61,72,70]

# minimum,maximum=get_stats(lengths)
# print(minimum,maximum)


# from collections import defaultdict

# class Visits:
#     def __init__(self):
#         self.data=defaultdict(set)

#     def add(self,country,city):
#         self.data[country].add(city)

# visits=Visits()
# visits.add('england','bath')
# visits.add('england','london')
# print(visits.data)


# visits={'Mexico':{'Tulum','puerie'},'Japan':{'hakon'}}
# visits.setdefault('Mexico',set()).add('Alertd')
# print(visits)

# votes={'baguette':['Bob','Alice'],
#        'ciabatta':['Coco','Deb']}

# key='brioche'
# who='Elmer'

# # if key in votes:
# #     names=votes[key]
# # else:
# #     votes[key]=names=[]

# # names.append(who)
# # print(votes)
# names=votes.get(key)
# if names is None:
#     votes[key]=names=[]

# names.append(who)
# print(votes)


# from collections.abc import MutableMapping
# class SortedDict(MutableMapping):
#     def __init__(self):
#         self.data={}

#     def __getitem__(self, key):
#         return self.data[key]

#     def __setitem__(self, key, value):
#         self.data[key]=value

#     def __delitem__(self, key):
#         del self.data[key]

#     def __iter__(self):
#         keys=list(self.data.keys())
#         keys.sort()
#         for key in keys:
#             yield key

#     def __len__(self):
#         return len(self.data)

# votes = {'otter': 1281, 'polar bear': 587, 'fox': 863}


# def populate_ranks(votes, ranks):
#     names = list(votes.keys())
#     names.sort(key=votes.get, reverse=True)
#     for i, name in enumerate(names, 1):
#         ranks[name] = i
#         # print(ranks)


# def get_winner(ranks):
#     if not isinstance(ranks,dict):
#         raise TypeError('must provide a dict instance')
#     return next(iter(ranks))


# ranks = {}
# populate_ranks(votes, ranks)
# print(ranks)
# winner=get_winner(ranks)
# print(winner)


# sorted_ranks=SortedDict()
# populate_ranks(votes,sorted_ranks)
# print(sorted_ranks.data)
# winner=get_winner(sorted_ranks)
# print(winner)


# baby_names={'cat':'kitten','dog':'puppy'}
# print(baby_names)


# class Tool:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight

#     def __repr__(self):
#         return f'Tool({self.name!r},{self.weight})'


# tools = [
#     Tool('level', 0.5),
#     Tool('level', 1.25),
#     Tool('scredwdriver', 1.35),
#     Tool('chisel', 0.25)
# ]

# # print('unsorted:', tools)
# # tools.sort(key=lambda x: x.weight)
# # print('sorted:', tools)

# # saw=(40,'circular saw')
# # jackhammer=(40,'jackhammer')
# # assert saw < jackhammer

# tools.sort(key=lambda x:(x.weight,x.name))
# tools.sort(key=lambda x:x.name)
# tools.sort(key=lambda x:x.weight,reverse=True)

# print(tools)


# from random import randint

# random_bits=0
# for i in range(32):
#     a=randint(0,1)
#     print('a=',a)
#     if a:
#         random_bits |=1<<i
#         print('random_bits:',random_bits)
# print(bin(random_bits))


# snacks=[('bacon',350),('donut',240),('muffin',190)]
# for rank,(name,calories) in enumerate(snacks):
#     print(f'{rank}:{name} has {calories} calories')


# snack_calories={'chips':140,'popcorn':80,'nuts':190}
# items=tuple(snack_calories.items())
# print(items)

# item=('peanut butter','jelly')
# first,second=item
# print(first,second)

# from urllib.parse import parse_qs

# my_values=parse_qs('red=5&blue=0&green=',keep_blank_values=True)
# print(repr(my_values))

# print(my_values.get('red'))
# print(my_values.get('green'))
# print(my_values.get('opacity'))

# # red=my_values.get('red',[''])[0] or 0
# red=my_values.get('red')[0] or 0

# green=my_values.get('green',[''])[0] or 0
# opacity=my_values.get('opacity',[''])[0] or 0
# print(red)
# print(green)
# print(opacity)


# def get_first_int(values,key,default=0):
#     found=values.get(key,[''])
#     if found[0]:
#         return int(found[0])
#     return default

# green=get_first_int(my_values,'green')
# red=get_first_int(my_values,'red')
# opacity=get_first_int(my_values,'opacity')

# print(red)
# print(green)
# print(opacity)
