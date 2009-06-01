#!/usr/bin/python
"""
Copyright (c) 2009, John D'Agostino
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, 
       this list of conditions and the following disclaimer.
    
    2. Redistributions in binary form must reproduce the above copyright 
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. Neither the name of trml2pdf nor the names of its contributors may be used
       to endorse or promote products derived from this software without
       specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import sys
import os
from optparse import OptionParser

from trml2pdf import get_version_string
from trml2pdf import parse_string, ParserError

def help():
    print 'rml2pdf.py %s' % get_version_string()
    print 'Render RML and output to a PDF file'
    print 'Usage: trml2pdf.py input.rml output.pdf'
    sys.exit(0)

def write_to_output(output_filename, content):
    output_file = None
    try:
        output_file = file(output_filename, 'wb')
        output_file.write(content)
    except IOError:
        print 'failed to open output file %s' % output_filename
    finally:
        if output_file:
            output_file.close()

def main():
    # This replaces the former method of trml2pdf.py input.rml > output.pdf
    # It also allows for more robust customization in the future.
    # because trml2pdf is the name of the module, the cli script 
    # cannot be also called trml2pdf.
    
    # No need for options currently, use this for --help, --version
    parser = OptionParser(usage="%prog [options] input_file output_file", 
                          version="%%prog %s" % get_version_string())    
    options, args = parser.parse_args()
    
    if len(args) < 2:
        return help()
    
    input_filename = args[0]
    output_filename = args[1]
    
    if not os.path.exists(input_filename):
        print 'input file does not exist'
        sys.exit(0)
    
    input_file = None
    try:
        input_file = open(input_filename, 'r')
        input_data = input_file.read()
    except IOError, e:
        print 'failed to open input file %s' % input_filename
        sys.exit(0)
    finally: 
        if input_file:
            input_file.close()

    try:
        write_to_output(output_filename, parse_string(input_data))
    except ParserError, e:
        print 'parsing rml failed with the following error'
        print e

if __name__=="__main__":
    main()