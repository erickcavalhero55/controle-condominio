import argparse

import application.ports.cmd.runner
import application.ports.api.runner

parser=argparse.ArgumentParser()

parser.add_argument("--mode", help="api | cmd")
args=parser.parse_args()

if __name__ == '__main__':
    if args.mode == 'cmd':
        application.ports.cmd.runner.start()
    else:
        application.ports.api.runner.start()
