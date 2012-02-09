#  Copyright 2008-2012 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import with_statement

USAGE = """Robot Framework Library and Resource File Documentation Generator

TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

Usage:  libdoc.py [options] library_or_resource

This script can generate keyword documentation in HTML and XML formats. The
former is suitable for humans and the latter for RIDE, RFDoc, and other tools.
This script can also upload XML documentation to RFDoc system.

Documentation can be created for both test libraries and resource files. All
library and resource file types are supported, and also earlier generated
documentation in XML format can be used as input.

Options:
 -a --argument value *    Possible arguments that a library needs.
 -f --format HTML|XML     Specifies whether to generate HTML or XML output.
                          The default value is got from the output file
                          extension and if the output is not specified the
                          default is HTML.
 -o --output path         Where to write the generated documentation. Can be
                          either a directory or a file, or a URL pointing to
                          RFDoc system's upload page. The default value is the
                          directory where the script is executed from. If
                          a URL is given, it must start with 'http://'.
 -N --name newname        Sets the name of the documented library or resource.
 -V --version newversion  Sets the version of the documented library or
                          resource.
                          TODO: ArgumentParser has special handling for this.
                                That needs to be somehow configurable.
 -T --title title         Sets the title of the generated HTML documentation.
                          Underscores in the given title are automatically
                          converted to spaces.
 -P --pythonpath path *   Additional path(s) to insert into PYTHONPATH.
 -E --escape what:with *  Escapes characters which are problematic in console.
                          'what' is the name of the character to escape and
                          'with' is the string to escape it with.
                          <-------------------ESCAPES------------------------>
 -h --help                Print this help.

For more information see either the tool's wiki page at
http://code.google.com/p/robotframework/wiki/LibraryDocumentationTool
or tools/libdoc/doc/libdoc.html file inside source distributions.

TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
"""

import sys

if 'robot' not in sys.modules:
    import pythonpathsetter   # running libdoc.py as script

from robot.utils import Application

from robot.doctools import LibraryDoc, LibraryDocOutput, LibraryDocWriter


class LibDoc(Application):

    def __init__(self):
        Application.__init__(self, USAGE, auto_version=False)

    def main(self, library_or_resource, argument=None, name='', version='',
             format='HTML', output=None, title='', styles=None):
        libdoc = LibraryDoc(library_or_resource[0], argument, name, version)
        with LibraryDocOutput(output) as outfile:
            LibraryDocWriter(format, title).write(libdoc, outfile)


def libdoc_cli(args):
    LibDoc().execute_cli(args)


if __name__ == '__main__':
    libdoc_cli(sys.argv[1:])