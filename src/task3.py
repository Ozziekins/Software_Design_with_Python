import time
import io
from contextlib import redirect_stdout
import inspect

global ranks
ranks = dict()


class ClassFuncDecorator:
    counter = 0

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()

        # capture the output from stdout
        f = io.StringIO()
        with redirect_stdout(f):
            self.func(*args, **kwargs)
        returned_value = f.getvalue()

        # increase the count of function call
        self.counter += 1

        end_time = time.time()

        # calculate execution time by subtracting start time from end time
        exec_time = end_time - start_time

        # add the function, and it's execution time to the global rankings dictionary
        ranks[self.func.__name__] = exec_time

        # dump the program output in a txt file named after the function
        with open(self.func.__name__+".txt", "w") as f:
            f.write(self.func.__name__ + " call " + str(self.counter) + " executed in " + str(exec_time) + " sec\n" +
                    "Name: \t" + self.func.__name__ + "\n" +
                    "Type: \t" + str(type(self.func)) + "\n" +
                    "Sign: \t" + str(inspect.signature(self.func)) + "\n" +
                    "Args: \tpositional " + str(args) + "\nkey=worded " + str(kwargs) + "\n" +
                    "Doc: \t" + inspect.getdoc(self.func) + "\n" +
                    "Source: \t" + inspect.getsource(self.func) + "\n" +
                    "Output: \t" + str(returned_value) + "\n")
            f.close()


# function to sort and print the functions and execution time by their ranks
def rankings():
    sorted_ranks = dict(sorted(ranks.items(), key=lambda item: item[1]))
    print("PROGRAM \t  \t | \t RANK \t | \t TIME ELAPSED")
    i = 1
    for k, v in sorted_ranks.items():
        sep_1 = 20 - len(k)
        sep_2 = 10
        print(k + sep_1 * ' ' + str(i) + sep_2 * ' ' + str(v))
        i += 1
