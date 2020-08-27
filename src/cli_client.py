#!/usr/bin/env python

import argparse
import re
import sys
from datetime import datetime

from clock import talk


def main():
    parser = argparse.ArgumentParser(description="Convert a numeric time to words")
    parser.add_argument(
        "-t", "--numeric_time", type=str, default=datetime.now().strftime("%H:%M"), help="The time to convert to words"
    )
    args = parser.parse_args()

    if re.search('[a-zA-Z]', args.numeric_time):
        sys.stderr.write("Error: Provided time [{}] contains non numeric characters".format(args.numeric_time))
        sys.exit(1)

    try:
        human_time = talk(args.numeric_time)
        sys.stdout.write(human_time)
        sys.exit(0)
    except ValueError:
        sys.stderr.write("Error: Numeric time [{}] is not in a valid format".format(args.numeric_time))
        sys.exit(1)
