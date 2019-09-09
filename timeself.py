import timeit
from os.path import basename, realpath
import sys


def timeself(number=1):
    file_name = realpath(basename(sys.argv[0]))
    file_instance = open(file_name, 'r')
    file_content = file_instance.read().split("\n")
    timeself_call = file_content[-2].split("()")
    if ("timeself" not in timeself_call and
            "timeself.timeself" not in timeself_call):
        print("timeself() function must be called at the end of the script.")
    file_content.pop(-2)
    file_content = "\n".join(file_content)
    print("Execution time:", timeit.timeit(file_content, number=number))
