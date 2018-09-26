#
# simple commands
# (c) 2018 ISC Clemenz & Weinbrecht GmbH
#

import argparse


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="simple command executor")
    arg_parser.add_argument('--conf', type=str, default='aloga.ini')
