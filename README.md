# dyn_options


## What it is.

*dyn_options* is an easy way to parse command line options.
It creates an options object, with the command line flags as attributes
which the command line values as values.

It allows for defaults, as well as a way to check whether the option has
been set.

 
## How is it used.

Here is how an option object is created

        import dyn_options
	

    	option = dyn_options.create_option(argv, option_defaults())

If you have defaults, have *option_defaults()* should return a dictionary of
key-value pairs. 

A simple flag is specified with a value of True or False.

Anything starting with a - or -- (i.e. a single or double dash) is considered
a flag. Anything following a flag is concatenated until the next flag 
is encountered. So, '--opt hello world' will be converted to an option flag 
called opt4, with a value of 'hello world'.



## An example

 *example.py* has some sample code that you can use to play around with:


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



Here 's the out put for :

    ./example.py --opt2 --opt4 hello world


    using defaults : options :
    	  #) help ==> False
          #) program ==> ./example.py
          #) opt4 ==> hello world
          #) opt1 ==> opt1_default
          #) opt2 ==> True
    no defaults : options :
          #) program ==> ./example.py
          #) opt4 ==> hello world
          #) opt2 ==> True
    opt4 is set : hello world


Here's the output for :

    ./example.py --opt1 new_value 

    using defaults : options :
         #) help ==> False
         #) program ==> ./example.py
         #) opt1 ==> new_value
    no defaults : options :
         #) program ==> ./example.py
         #) opt1 ==> new_value
    opt4 is not set

## License
This is distrubuted under the BSD License. See the LICENSE file for details. 
Obviously the LICENSE needs to be included in any further distribution.


