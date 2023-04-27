import argparse

import application.ports.cmd.command_line
import application.ports.api

parser=argparse.ArgumentParser()

parser.add_argument("--mode", help="api | cmd")
args=parser.parse_args()

if __name__ == '__main__':
    if args.mode == 'cmd':
        application.ports.cmd.command_line.start()
    else:
        application.ports.api.api.start()

