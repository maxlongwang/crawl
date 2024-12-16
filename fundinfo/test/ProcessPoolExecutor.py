from concurrent.futures import ProcessPoolExecutor


def test(num):
    print("process", num)
    
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.submit(test,1)
        executor.submit(test,2)
        executor.submit(test,3)
    
        