from timer import timer
import time

@timer
def another_task():
    time.sleep(2)
    return "Another task done"

if __name__ == "__main__":
    print(another_task())




