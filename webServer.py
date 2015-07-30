#!	/usr/bin/python

################################################################################
#	webServer.py  -  Oct-6-2014 by aldeba
#
#	Class for the webServer's entry point
################################################################################

from	configuration import Configuration
from	configuration import ConfigurationFile
from	listener import Listener

#	configuration attributes class

class WebServer:

	def __init__( self, fileName ):
		self.fileName = fileName

	def start( self ):
		myConfigurationFile = ConfigurationFile( self.fileName )
		myConfiguration = myConfigurationFile.load()

		myListener = Listener( myConfiguration )
		myListener.start()

#	entry point

if( __name__ == '__main__' ):

#	get the configuration file name

	myConfigurationFileName = 'webServer.config'

#	start the web server engine

	print '[WebServer] Starting the Web Server'
	print '[WebServer] configuration file: ', myConfigurationFileName

	myWebServer = WebServer( myConfigurationFileName )

	myWebServer.start()

