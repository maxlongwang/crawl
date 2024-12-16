from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time
# def test(num):
#     print(num)
    
# with ThreadPoolExecutor(max_workers=5) as executor:
#     future1=executor.submit(test,1)
#     future2=executor.submit(test,2)
#     future3=executor.submit(test,3)
#     print(future1.result())

# def callback(future):
#     print("task done ",future.done())
#     print("result ",future.result())
    
# with ThreadPoolExecutor(max_workers=3) as executor:
#     future_1=executor.submit(pow,2,4)
#     future_2=executor.submit(pow,3,4)
#     callback_future_1=executor.submit(callback,future_1)    
#     print(callback_future_1)
    
    
# def square(x):
#     return x*x

# def cube(x):
#     return x*x*x

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results=executor.map(square,[1,2,3,4,5])
#     for square_result in results:
#         print(square_result)
    
#     results=executor.map(cube,[1,2,3,4,5])
#     for cube_result in results:
#         print(cube_result)
        

def task(num):
    print("task {} is runing".format(num))
    time.sleep(1)
    return "task {} is complete".format(num)

with ThreadPoolExecutor(max_workers=3) as executor:
    futures=[executor.submit(task,i) for i in range(1,4)] 
    executor.shutdown()   
        