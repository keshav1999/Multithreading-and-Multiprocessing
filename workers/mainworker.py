import time
from workers.SquaredSumWorkers import SquaredSumWorkers
from workers.SleepyWorkers import SleepyWorker


def main():
    cal_start_time = time.time()

    current_threads = []
    for i in range(5):
        max_value = (i + 1) * 10000000
        squaredWorker = SquaredSumWorkers(n=max_value)
        current_threads.append(squaredWorker)

        # calculate_sum_squares((i+1)*10000000)
    for i in range(len(current_threads)):
        current_threads[i].join()

    print("Calculating sum of squares took:", round(time.time() - cal_start_time, 1))

    sleep_start_time = time.time()
    current_threads = []
    for i in range(1, 6):
        sleepyWorker = SleepyWorker(seconds=i)
        current_threads.append(sleepyWorker)
        # sleep_a_little(i)
    for i in range(len(current_threads)):
        current_threads[i].join()
    print("Calculating sleep time took:", round(time.time() - sleep_start_time, 1))

if __name__ == "__main__":
    main()