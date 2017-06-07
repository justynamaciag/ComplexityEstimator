import logging
import importlib
from zad2_justynamaciag import estimation
import time
import signal

tmp = 10
times = []
numbers = []

class Timeout():
    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)

    def raise_timeout(self, *args):
        raise Timeout.Timeout()

def get_log():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def manage(file_name, function, structure_fun, cleaner, given_time, given_n, timeout):

    def handler(signum, frame):
        get_log().warn("It seems that times out, we will count complexity based on measurments already taken")
        estimation.estimate_complexity_manager(times, numbers, given_time, given_n)
        raise Exception("Error: End of time")


    get_log().info('We are in module file_handler')

    try:
        module = importlib.import_module(file_name)
    except ImportError:
        get_log().error("An error occured while opening given file")
    else:
        for i in range(3):

            start_time = time.time()

            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout)

            structure = None
            global tmp
            if structure_fun != 'None':
                structure = get_structure(module, structure_fun)
            open_function(module, function, structure)
            structure = None
            open_function(module, cleaner, structure)
            tmp = tmp * 10

            end_time = time.time()
            time_measured = (end_time - start_time)

            times.append(time_measured * 1000000)
            numbers.append(tmp)

        estimation.estimate_complexity_manager(times, numbers, given_time, given_n)

def manage_decorator(function):

    try:
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
    except TypeError:
        get_log.error("An error connected with uncorrect calling function (probably problem with given parameters) in function  %s", function)
        exit()


@manage_decorator
def open_function(module, function, structure):

    try:
        method = getattr(module, function)
    except AttributeError:
        get_log().error("An error while calling function from file (probably given function doesn't exist)- %s", function)
        exit()
    else:
        try:
            if structure is None:
                method()
            else:
                method(structure)

        except NameError as e:
            get_log.error("ERROR: Probably function that you want to test doesn't work properly %s", e.args)
            exit()


@manage_decorator
def get_structure(module, function):

    try:
        str_method = getattr(module, function)
        structure = str_method()
    except AttributeError:
        get_log.error("An error while calling function from file (probably given function doesn't exist) - %s", function )
        exit()
    else:
        return structure
