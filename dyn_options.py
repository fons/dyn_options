#!/usr/bin/env python
import sys
import string
import types

class dyn_options :

    def __init__(self, d) :
        self.__dict__   = d
        self._freeze    = False
        self._internals = ["_internals","_freeze", "defaults"] 

    def __repr__(self) :
        return self.__make_str(self.__id)

    def __str__(self) :
        return self.__make_str(self.__excl_internal_symbols)

    def __id(self, k) :
        return True

    def __excl_internal_symbols(self, k) :
        return k not in self._internals
        
    def __make_str(self, fn) :
        L = ["options :"]
        L = L + map(self.__make_rep, filter(fn, self.__dict__))
        return string.join(L,"\n")
        
    def __make_rep(self, key) :
        return "\t#) " + str(key) + " ==> " + str(self.__dict__[key]) 


    def __getattr__(self, attrname) :
        return False 
    
    def freeze(self) :
        self._freeze = True
        return self._freeze

    def __setattr__(self, attr, value) :

        def _set_default(p) :
            if not self.__dict__.has_key(p[0]) :
                self.__dict__[p[0]] = p[1]
            return p

        def _is_frozen() :
            if self.__dict__.has_key("_freeze") and self.__dict__["_freeze"] == True :
                return True
            return False

        if attr == "_freeze" and value == True :
            self.__dict__[attr] = value
            return 

        if attr != "defaults" and not self.__dict__.has_key(attr) and not _is_frozen():
            self.__dict__[attr] = value
            return

        if  self.__dict__.has_key(attr) :
            return
        
        if attr == "defaults" and type(value) == types.DictType :
            map(_set_default, value.iteritems())
            self.__dict__[attr] = value
            
        if attr == "defaults" and type(value) == types.ListType :
            try :
                map(_set_default, dict(value).iteritems())
                self.__dict__[attr] = dict(value)
            except :
                if self.__dict__.has_key("defaults") :
                    del self.__dict__["defaults"]
        
        return

def create_option(argv, defaults=[]) :

    def parse_argv(l, r) :
        

        def starts(s) :
            def starts_with(pat, s) :
                return (pat == s[0:len(pat)])
            return starts_with("-", s) or starts_with("--", s)

        def start(l, r) :
            """
            start state
            """

            if len(l) == 0 :
                return ([["--program", r ]], "")

            if len(l) == 1 and len(l[0]) == 0 :
                return ([["--program", r ]], "")
            
            return (l, r)
        
        def pattern1(l, r) :
            """
            last argument started with a -- and the next one as well e.g [..] --opt1 --opt2 [..] 
            """
            if (len(r) == 0) :
                return (l, r)
        
            le = len(l) - 1
            if (len(l[le]) == 1) and starts(l[le][0]) and starts(r) :
                l[le].append(True) 
                l.append([r])
                return (l,"")
            return (l,r)

        def pattern2(l, r) :
            """
            last argument started with a -- and the next one doesn't [..] --opt1 value1 [..]
            or
            last argument didn't start with a -- and neither does the next one [..] value1 value2 [..] 
            """
            if (len(r) == 0) :
                return (l, r)
        
            le = len(l) - 1
            if (len(l[le]) > 0) and starts(l[le][0]) and (not starts(r) ) :
                l[le].append(r) 
                return (l,"")
            return (l,r)

        def pattern3(l, r) :
            """
            last argument didn't start with a -- and the next one does [..] value1 --opt2 [..] 
            """
            if (len(r) == 0) :
                return (l, r)

            le = len(l) - 1
            if (len(l[le]) > 1) and starts(l[le][0]) and starts(r)  :
                l.append([r]) 
                return (l,"")
            return (l,r)


        (l, r) = start(l, r)
        (l, r) = pattern1(l, r)
        (l, r) = pattern2(l, r)
        (l, r) = pattern3(l, r)

        return l

    def clean_args(l) :

        def strip_dash(s) :
            if "--" == s[0:2] :
                return s[2:]

            if "-" == s[0:1] :
                return s[1:]

            return s

        if len(l) == 0 :
            return l

        if len(l) == 1 :
            l.append(True)
    
        if len(l) < 3:
            return [strip_dash(l[0])] + l[1:]
        
        return [strip_dash(l[0]), string.join(l[1:]," ")]

    opt = dyn_options( dict(map(clean_args, reduce(parse_argv, argv, [ [] ] ))))
    opt.defaults = defaults
    opt.freeze()
    return opt

