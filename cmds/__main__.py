#
# simple remote commands
# (c) 2018 ISC Clemenz & Weinbrecht GmbH
#

import argparse
import cmds
import sys

if __name__ == '__main__':
    # 0. command parser.
    arg_parser = argparse.ArgumentParser(description="simple command executor")
    arg_parser.add_argument('--conf', type=str, default='cmds.ini')
    args = arg_parser.parse_args()

    # 1. initialize the module.
    cmds.init(args.conf)

    cmds.LOG.info('done.')
    # a value of zero indicates 'no error' to fauxmo/alexa
    sys.exit(0)