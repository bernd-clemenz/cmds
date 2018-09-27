#
# simple commands
# (c) 2018 ISC Clemenz & Weinbrecht GmbH
#

import argparse
import cmds
import sys

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="simple command executor")
    arg_parser.add_argument('--conf', type=str, default='cmds.ini')
    args = arg_parser.parse_args()

    cmds.init(args.conf)
    # a value of zero indicates 'no error' to fauxmo/alexa
    sys.exit(0)