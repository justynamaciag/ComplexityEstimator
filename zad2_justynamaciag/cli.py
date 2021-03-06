import click
from os.path import isfile
from types import  ModuleType
import logging
import numpy
from zad2_justynamaciag import file_handler
import os
from zad2_justynamaciag.exceptions import NegativeTimeException, NegativeNException



def get_log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger

@click.command()
@click.option('--file_name', prompt='Name of the file (must be with .py extension)',  help = 'Name of the file (must be with .py extension)')
@click.option("--cleaner", default = 'cleaner' , help = "Give cleaner function")
@click.option('--function', default ='quicksort', help = 'Name of the class/function to test')
@click.option('--structure', default='struct', help='Function to make structure')
@click.option('--time',type=int, help = 'Time for option 3.')
@click.option('--n', type = int, help = 'Size of problem for option 2.')
@click.option('--timeout', type = int, default=30, help='Time for running before timeout')
def main(file_name, function, cleaner, structure, time, n, timeout):

    if file_name.endswith('.py'):
        file_name = file_name[:-3]

    if(timeout == 30):
        get_log().warn("Timeout default: 30 sec")

    print("We will test function", function )


    try:
        if time and time<0:
            raise NegativeTimeException('Given time must be above zero')
        if n and n<0:
            raise NegativeNException('Given n must be above zero')
        if timeout<0:
            raise NegativeTimeException('Given timeout must be above zero')
    except NegativeTimeException as e:
        print(e)


    file_handler.manage(file_name, function, structure, cleaner, time, n, timeout)



if __name__ == "__main__":
    main()
