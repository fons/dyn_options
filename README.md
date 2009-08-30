# dyn_options


## What it is.

*dyn_options* is an easy way to process command line options.
It creates an *options* object, which has the command line flags as attributes. 
The value of the *option* object attribute is it's value provided on the command line.


It allows for defaults, as well as a way to check whether the option has
been set.

Anything starting with a - or -- (i.e. a single or double dash) is considered
a flag. Anything following a flag is concatenated until the next flag 
is encountered. 

For example, '--opt4 hello world' will be converted to an attribute called opt4, 
which has a value of 'hello world'.


A single flag will have a corresponding attribute value of True or False.
 

## How it is used.

Here is how an option object is created

        import dyn_options
	

    	option = dyn_options.create_option(argv, option_defaults())

If you have defaults, *option_defaults()* should return a dictionary of
key-value pairs. 

The *option* object returned is immutable, so you can't reset the attribute values, 
nor can you add additional attributes. There's no error raised when you try either 
of these things. 


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

## Installation

Run `install` from the command line. 

This will create a subdirectory with the contents of the 
package as well as a build directory. This is then pushed to the site-packages 
directory by running `python setup.py install`
  

## More information

See *dyn_option_test.py* for more examples.

## License


This is distributed under the BSD License. See the LICENSE file for details. 
Obviously the LICENSE needs to be included in any further distribution.


