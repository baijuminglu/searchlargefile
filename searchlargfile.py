#!/usr/bin/env python

import json
import subprocess
from optparse import OptionParser
from ListFile import ListFile

# help info
helptext = "this program is to searh the large file of dir"                                                                                                               
sversion = "v1.0"                                                                                                                                                         
usage = ("%prog [OPTION]... [DIR]" + '\n' + helptext)                                                                                                                     
parser = OptionParser(usage, version='%prog ' + sversion)                                                                                                                 

parser.add_option("-d", "--dir", type="string", action="store", dest="dir", default="/", help="choose dir defaul:t is /")                                               
parser.add_option("-n", "--num", type="int", action="store", dest="num", default=5, help='choose the num of largest file defalt is 5, if the file num of dir is less the num, return real num of file');                                                                                                                                       
                                                                                                                                                                          
(options,largs) = parser.parse_args();                                                                                                                                    
if __name__ == "__main__":
    try:
        out_bytes = subprocess.check_output(['ncdu', '-o', '-', options.dir])
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        code      = e.returncode
        print('excute \"ncdu -x - %s\" fail' % options.dir)
        print(out_bytes)
        sys.exit(code)
    handle = ListFile(json.loads(out_bytes))
    handle.getlargefile(options.num)   
