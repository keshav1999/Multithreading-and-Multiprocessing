import time
import threading


def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares+= i**2
    print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)


def main():
    cal_start_time = time.time()

    current_threads = []
    for i in range(5):
        max_value = (i+1)*10000000
        t = threading.Thread(target=calculate_sum_squares,args=(max_value,))
        t.start()
        current_threads.append(t)
        # calculate_sum_squares((i+1)*10000000)
    for i in range(len(current_threads)):
        current_threads[i].join()

    print("Calculating sum of squares took:" , round(time.time()-cal_start_time,1))

    sleep_start_time = time.time()
    current_threads = []
    for i in range(1,6):
        t = threading.Thread(target=sleep_a_little,args=(i,))
        t.start()
        current_threads.append(t)
        # sleep_a_little(i)
    for i in range(len(current_threads)):
        current_threads[i].join()
    print("Calculating sleep time took:", round(time.time() - sleep_start_time, 1))

if __name__ == '__main__':
    main()
