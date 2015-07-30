#!	/usr/bin/python

################################################################################
#	listener.py  -  Oct-2-2014 by aldeba
#
#	Class for a HTTP connection listener
################################################################################

import	socket

from	configuration import Configuration

#	HTTP connection listener exceptions classes

class missingObjectID( Exception ):
	pass

#	HTTP connection listener class

class Listener:

	def __init__( self, configuration ):
		self.configuration = configuration

	def start( self ):
		print '[Listener] starting listening at port ', self.configuration.portNumber

#	unit test code

if( __name__ == '__main__' ):

#	Listener class unit test 

	print '[Listener] unit test'

