import time
import io
from contextlib import redirect_stdout
import inspect
from datetime import datetime


class ClassFuncDecorator2:
    counter = 0

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        # block to attempt to carry out the algorithm
        try:
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

            # dump the program output in a txt file named after the function
            with open(self.func.__name__+".txt", "w") as f:
                f.write(self.func.__name__ + " call " + str(self.counter) + " executed in " + str(exec_time) + " sec\n"
                        +
                        "Name: \t" + self.func.__name__ + "\n" +
                        "Type: \t" + str(type(self.func)) + "\n" +
                        "Sign: \t" + str(inspect.signature(self.func)) + "\n" +
                        "Args: \tpositional " + str(args) + "\nkey=worded " + str(kwargs) + "\n" +
                        "Doc: \t" + inspect.getdoc(self.func) + "\n" +
                        "Source: \t" + inspect.getsource(self.func) + "\n" +
                        "Output: \t" + str(returned_value) + "\n")
                f.close()
        # fall back block in case of any error encountered while carrying out the algorithm above
        except Exception as err:
            dt = datetime.now()
            with open(self.func.__name__+"_exception_log.txt", "w") as f:
                f.write(str(dt) + ": in func " + self.func.__name__ +
                        ", " + str(err) + " occurred ")
