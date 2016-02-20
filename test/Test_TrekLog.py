# **************************    Begin License Block    *************************
# TrekLog by Ian Joseph Thompson (Copyright 2016, CC BY-NC-SA 4.0)
#     TrekLog, the contents of this file, and other source files are licensed
#     under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
#     International License (https://creativecommons.org/licenses/by-nc-sa/4.0/)
#     as documented in the file LICENSE.txt.
#
# You are free to:
#     Share - copy and redistribute the material in any medium or format
#     Adapt - remix, transform, and build upon the material
#     Independently - The licensor cannot revoke these freedoms as long as you
#         follow the license terms.
#
# Under the following terms:
#     Attribution - You must give appropriate credit, provide a link to the
#         license, and indicate if changes were made. You may do so in any
#         reasonable manner, but not in any way that suggests the licensor
#         endorses you or your use.
#     NonCommercial - You may not use the material for commercial purposes.
#     ShareAlike - If you remix, transform, or build upon the material, you must
#         distribute your contributions under the same license as the original.
#     No additional restrictions - You may not apply legal terms or technological
#         measures that legally restrict others from doing anything the license
#         permits.
#
# Removing this information violates the terms of the license:
#     Source: TrekLog (https://github.com/ianjosephthompson/TrekLog)
#     By:     Ian Joseph Thompson (ian.joseph.thompson@gmail.com)
# ***************************    End License Block    **************************

"""
The Test_TrekLog.py module will discover all modules with TestCases under
test/tests, execute all discovered tests, and output text results in console.

Execute this module directly to instantiate a Test_TrekLog object and call
Test_TrekLog.test() immediately.
"""

import unittest

class Test_TrekLog():
    """
    The Test_TrekLog class
    """

    tests = None
    """
    The tests attribute holds the TestSuite of all discovered TestCases
    """

    def __init__( self ):
        """
        Inits Test_TrekLog and silently searches for tests.
        """

        self.loadTests( silently=True )

    def loadTests( self, silently=False ):
        """
        Recursively searches the test/tests directory for modules containing
        TestCases and stores the resulting TestSuite in the tests attribute.
        
        Args
            silently=False: True to squelch console print statements.
        """

        if not silently:
            print( "Discovering tests..." )

        loader = unittest.TestLoader()
        self.tests = loader.discover( "tests/TrekLog_tests", pattern="*test*.py" )

        if not silently:
            print( "{num} tests discovered.".format( num=self.tests.countTestCases() ) )
            print( "" )

    def test( self ):
        """
        Execute all discovered tests and print the results.
        """

        print( "Beginning test run..." )
        print( "" )

        if not self.tests or not self.tests.countTestCases():
            self.loadTests()

        print( "Running tests..." )

        runner = unittest.TextTestRunner()
        results = runner.run( self.tests )

        print ( "Testing complete!" )
        print ( "" )
        print( results )

if __name__ == "__main__":
    tester = Test_TrekLog()
    tester.test()
