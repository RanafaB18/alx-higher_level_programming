#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except ZeroDivisionError as err:
        print("Exception: {}".format(err.args[0]), file=sys.stderr)
    except IndexError as err:
        print("Exception: {}".format(err.args[0]), file=sys.stderr)
    except ValueError as err:
        print("Exception: {}".format(err.args[0]), file=sys.stderr)
