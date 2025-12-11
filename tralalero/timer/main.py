from timer import timer
import time

@timer
def slow_function():
    time.sleep(3)
    return "Done"

if __name__ == "__main__":
    print(slow_function())



