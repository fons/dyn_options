#!/usr/bin/env python


import sys

import dyn_options

def option_defaults() :
    return dict( [("opt1", "opt1_default"), ("help", False)])

def main(argv) :
    option = dyn_options.create_option(argv, option_defaults())
    print "using defaults :", option

    option = dyn_options.create_option(argv)
    print "no defaults :", option


    if option.opt4 :
        print "opt4 is set :", option.opt4
    else :
        print "opt4 is not set"

if __name__ == '__main__':
    sys.exit(main(sys.argv)) 
