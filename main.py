from file_handling import file_import, test_import
from algo import max_wood, max_wood_bu
from generate_tests import gen_tests
import time
import sys

def run_tests():
    # logs = test_import("test1.txt")
    gen_tests()
    for i in range(1, 51):
        logs = test_import("./arrays/array_" + str(i) + ".txt")
        start_time = time.time()
        # print("Test", str(i), max_wood(logs, 0, len(logs) - 1))
        result = max_wood(logs, 0, len(logs) - 1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Test", str(i), "with length", len(logs), "Result:", result, "Time:", elapsed_time)

def run_tests_bu():
    gen_tests()
    for i in range(1, 51):
        logs = test_import("./arrays/array_" + str(i) + ".txt")
        start_time = time.time()
        # print("Test", str(i), max_wood(logs, 0, len(logs) - 1))
        result = max_wood_bu(logs)
        # print(result)
        end_time = time.time()
        elapsed_time = end_time - start_time
        # print("Test", str(i), "with length", len(logs), "Result:", result, "Time:", elapsed_time)
        print(len(logs), ",", elapsed_time)

    # print(max_wood(logs, 0, len(logs) - 1))
def run_both():
    gen_tests()
    for i in range(1, 51):
        logs = test_import("./arrays/array_" + str(i) + ".txt")

        start_time = time.time()
        result_1 = max_wood(logs, 0, len(logs) - 1)
        end_time = time.time()
        elapsed_time_basic = end_time - start_time
        #
        start_time = time.time()
        result_2 = max_wood_bu(logs)
        end_time = time.time()
        elapsed_time_bu = end_time - start_time
        #
        print("Test", str(i), "with length", len(logs))
        # print("Basic recursion result: ", result_1)
        # print("BU recursion result: ", result_2)

        # print("Basic recursion: ", elapsed_time_basic)
        # print("Bottom-Up recursion: ", elapsed_time_bu)





def run_final():
    logs = file_import()
    print(max_wood_bu(logs))
    # print(max_wood(logs, 0, len(logs) - 1))




def main():
    sys.setrecursionlimit(4000)
    # run_final()
    # run_both()
    # run_tests_bu()
    run_final()

"""
MAIN
"""
if __name__ == '__main__':
    main()
    # run_tests()

