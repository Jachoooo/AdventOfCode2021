#!/usr/bin/env python3
"""
Advent of Code 2021
"""
__author__ = "Jachoooo"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import time
DAY = 0
FPATH = __file__.rstrip(__file__.split('/')[-1])
if FPATH == "" : FPATH = __file__.rstrip(__file__.split('\\')[-1])



def Part1(args):
    if args.test:
        data=inputreader(FPATH+"test"+args.test+".txt")
    else:
        data=inputreader(FPATH+"input.txt")
    
    result=0
    
    if args.debug: print('[d]',data)
    if args.verbose: print('Part_1 result = ',end='')
    print(result)

def Part2(args):
    if args.test:
        data=inputreader(FPATH+"test"+args.test+".txt")
    else:
        data=inputreader(FPATH+"input.txt")

    result=0

    if args.debug: print('[d]',data)
    if args.verbose: print('Part_2 result = ',end='')
    print(result)

def inputreader(name):
    inputFile=open(name,'r')
    ret=[]
    for line in inputFile:
        ret.append(line.rstrip())
    inputFile.close()
    return ret

def main(args):
    """ Main entry point of the app """
    
    if args.verbose: print("\nAdvent of Code 2021 - Day",DAY,'\n')
    if args.debug: print("[d]",args)
    if args.debug: print("[d]",FPATH)
    starttime=time.time()
    if args.part!='2':Part1(args)
    halftime=time.time() 
    if args.part!='1':Part2(args)
    if args.verbose:
        print('')
        if args.part==0: 
            print("Part 1 execution time = {:.6f} s".format(halftime-starttime))
            print("Part 2 execution time = {:.6f} s".format(time.time()-halftime))
        print("Total execution time  = {:.6f} s".format(time.time()-starttime))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Optional argument debug which defaults to False
    parser.add_argument("-d",
                        "--debug",
                        action="store_true", 
                        default=False,
                        help="Enables debug messages")

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-t",
                        "--test",
                        action="store",
                        default="",
                        dest="test",
                        help='Enables test input file')


    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="Enables verbose output")

    # Optional part selection
    parser.add_argument(
        "-p",
        "--part",
        action="store",
        default=0,
        dest="part",
        help="Select part")

    # Specify output of "--version"
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="Version {version}".format(version=__version__))

    args = parser.parse_args()
    main(args)

