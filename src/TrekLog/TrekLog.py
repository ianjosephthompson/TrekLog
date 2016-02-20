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
The TrekLog.py module is the entry point for the TrekLog application.
"""

__version__ = "0.0.0-dev"
__version_info__ = ( 0, 0, 0, "dev" )
"""
Version: 0.0.0-dev
"""


class HelloWorld():
    """
    A simple class which prints: \"Hello World!\"
    """
    
    def __init__( self ):
        """
        Initialize the class and print \"Hello World!\"
        """
        
        print( "Hello World!" )
        input()

HelloWorld()
