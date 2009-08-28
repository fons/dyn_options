#!/usr/bin/env python


import sys
import traceback
import string
import dyn_options


def option_defaults() :
    return dict( [("opt1", "opt1_default"), ("help", False)])


def test1() :

    """
    Test of general use.
    - use default if option is not supplied on the command line.
    - option by itself becomes a boolean. 
    """

    L=['./dyn_options.py', '--opt2', 'opt2_value', '--opt3']
    option = dyn_options.create_option(L, option_defaults())
    try :
        assert option.opt1 == "opt1_default"
        assert option.opt2 == "opt2_value"
        assert option.opt3 == True
    except AssertionError :
        traceback.print_exc()
        
        print "Failed test1 : parsing ", str(L)
        print "generated : ", option
        print "internals : ", option.__repr__()
        return -1

    print "pass test1"

    return 0

def test2() :

    """
    Same as test1, but now start with a single -
    """

    L=['./dyn_options.py', '-opt2', 'opt2_value', '-opt3']
    option = dyn_options.create_option(L, option_defaults())
    try :
        assert option.opt1 == "opt1_default"
        assert option.opt2 == "opt2_value"
        assert option.opt3 == True
    except AssertionError :
        traceback.print_exc()
        
        print "Failed test2 : parsing ", str(L)
        print "generated : ", option
        print "internals : ", option.__repr__()
        return -1

    print "pass test2"

    return 0

def test3() :

    """
    Override default on the command line
    """

    L=['./dyn_options.py', '--opt1', 'opt1_value', '-opt2', 'opt2_value', '-opt3', '--help']
    option = dyn_options.create_option(L, option_defaults())
    try :
        assert option.opt1 == "opt1_value"
        assert option.opt2 == "opt2_value"
        assert option.opt3 == True
        assert option.help == True
    except AssertionError :
        traceback.print_exc()
        
        print "Failed test3 : parsing ", str(L)
        print "generated : ", option
        print "internals : ", option.__repr__()
        return -1

    print "pass test3"

    return 0

def test4() :

    """
    option is immutable
    """

    L=['./dyn_options.py', '--opt1', 'opt1_value', '-opt2', 'opt2_value', '-opt3']
    option = dyn_options.create_option(L, option_defaults())
    try :
        assert option.opt1 == "opt1_value"
        assert option.opt2 == "opt2_value"
        assert option.opt3 == True
        assert option.help == False

        #Try to override...
        option.help = True
        assert option.help == False

        option.opt2 == "new_opt2_value"
        assert option.opt2 == "opt2_value"


        #Try to add new attribute
        option.opt55 = "opt55_value"
        assert option.opt55 == False
        
    except AssertionError :
        traceback.print_exc()
        
        print "Failed test4 : parsing ", str(L)
        print "generated : ", option
        print "internals : ", option.__repr__()
        return -1

    print "pass test4"
    return 0


def test5() :

    """
    Test to see if option is set...
    """

    L=['./dyn_options.py', '--opt1', 'opt1_value', '-opt2', 'opt2_value', '-opt3']
    option = dyn_options.create_option(L, option_defaults())
    try :
        assert option.opt1 == "opt1_value"
        assert option.opt2 == "opt2_value"
        assert option.opt3 == True
        assert option.help == False

        is_set = False
        if option.opt1 :
            is_set = True
        assert is_set == True

        is_set = True
        if not option.opt1 :
            is_set = False
        assert is_set == True

        is_set = False
        if option.opt1000 :
            is_set = True
        assert is_set == False

        is_set = True
        if not option.opt1000 :
            is_set = False
        assert is_set == False


    except AssertionError :
        traceback.print_exc()
        
        print "Failed test5 : parsing ", str(L)
        print "generated : ", option
        print "internals : ", option.__repr__()
        return -1

    print "pass test5"
    return 0

def test6() :

    """
    Test to see if option prints...
    """

    L=['./dyn_options.py', '--opt1', 'opt1_value', '-opt2', 'opt2_value', '-opt3']
    option = dyn_options.create_option(L, option_defaults())
    try :
        print "The command line is : ", L, " with defaults :", option_defaults()
        print "You should see the option print it's 'public' members:" 
        print option
        print "You should see the option print all its members:" 
        option.__repr__()

    except :
        traceback.print_exc()
        
        print "Failed test : parsing ", str(L)
        print "this is the print test; so I can't print out the option object"
        return -1
    print "pass test6"
    return 0


def main(argv) :
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

if __name__ == '__main__':
    sys.exit(main(sys.argv)) 
