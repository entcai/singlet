#!/usr/bin/env python
# vim: fdm=indent
'''
author:     Fabio Zanini
date:       07/08/17
content:    Tests for the library.
'''
# Modules
import os
import sys
import subprocess as sp


# Controlled sp environment
def run(script, **kwargs):
    env = os.environ.copy()
    env['SINGLET_CONFIG_FILENAME'] = 'example_data/config_example.yml'

    # Include local tests
    import platform
    if platform.node() == 'X260':
        singlet_path = os.path.dirname(os.path.dirname(__file__))
        env['PYTHONPATH'] = singlet_path+':'+env['PYTHONPATH']
        print(singlet_path)

    sp.check_call(
        script,
        env=env,
        shell=True,
        **kwargs)



# Script
if __name__ == '__main__':

    # Config

    # IO
    run('test/io/csv_parser.py')
    run('test/io/googleapi_parser.py')
