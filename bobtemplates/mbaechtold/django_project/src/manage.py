#!/usr/bin/env python
import envdir
import os
import sys

if __name__ == "__main__":
    # Load the environment variables in the folder ``./envs/`` with *envdir*.
    envdir.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'envs'))

    # Please note that this is *django-configurations* and not *Django*.
    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
