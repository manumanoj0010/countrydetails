"""
This module provides the command line interface for Countrydetails.
"""

# banner intro is done will do the functionalities in next release

import sys
import json
from argparse import ArgumentParser
from pathlib import Path
from os.path import isfile, realpath, dirname

from Countrydetails import VERSION


# dir_path = dirname(realpath(__file__))
# sys.path.insert(1, dir_path + '/cli_dir')

from .cli_dir.banner import Banner


def main(argv=None):
    _banner = Banner()
    _banner.intro()

if __name__ == '__main__':
    main()
