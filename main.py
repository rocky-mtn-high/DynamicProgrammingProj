from file_handling import file_import, test_import
from algo import max_wood
from generate_tests import gen_tests
import time

def run_tests():
    # logs = test_import("test1.txt")
    gen_tests()
    for i in range(1, 51):
        logs = test_import("array_" + str(i) + ".txt")
        start_time = time.time()
        # print("Test", str(i), max_wood(logs, 0, len(logs) - 1))
        result = max_wood(logs, 0, len(logs) - 1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Test", str(i), "with length", len(logs), "Result:", result, "Time:", elapsed_time)



    # print(max_wood(logs, 0, len(logs) - 1))

def run_final():
    logs = file_import()
    print(max_wood(logs, 0, ln(logs) - 1))




def main():
    run_final()

"""
MAIN
"""
if __name__ == '__main__':
    main()
    # run_tests()

