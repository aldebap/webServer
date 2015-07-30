#!	/usr/bin/python

################################################################################
#	configuration.py  -  Oct-3-2014 by aldeba
#
#	Class for the webServer's configuration attributes
################################################################################

import	json

#	Configuration attributes class

class Configuration:

	def __init__( self, name, description, portNumber ):
		self.name = name
		self.description = description
		self.portNumber = portNumber

	def __str__( self ):
		return '{0.name!s}: {0.description!s}\nListening Port: {0.portNumber!s}'.format( self )

	@classmethod
	def serialize( cls, ref ):
		attributes = {
			'name': ref.name
			, 'description': ref.description
			, 'portNumber': ref.portNumber
		}

		return json.dumps( attributes )

	@classmethod
	def unserialize( cls, stream ):
		attributes = json.loads( stream )
		name = attributes[ 'name' ]
		description = attributes[ 'description' ]
		portNumber = attributes[ 'portNumber' ]

		configurationAux = Configuration( name, description, portNumber )

		return configurationAux

#	ConfigurationFile  class

class ConfigurationFile:

	def __init__( self, fileName ):
		self.fileName = fileName

	def load( self ):
		with open( self.fileName, 'r' ) as fileHandler:
			attributes = json.load( fileHandler )

		return Configuration.unserialize( attributes )

	def save( self, configurationRef ):
		with open( self.fileName, 'w' ) as fileHandler:
			json.dump( Configuration.serialize( configurationRef ), fileHandler )

#	unit test code

if( __name__ == '__main__' ):

#	Configuration class unit test 

	print '[Configuration] unit test'

	myConfiguration = Configuration( 'unit', 'Unit test configuration', 8080 )

	print myConfiguration
	print

	attributes = Configuration.serialize( myConfiguration )

	print attributes
	print

	myConfigurationAux = Configuration.unserialize( attributes )

	print myConfigurationAux
	print

#	ConfigurationFile class unit test 

	print '[ConfigurationFile] unit test'

	myConfigurationFile = ConfigurationFile( 'unitTest.config' )

	myConfigurationFile.save( myConfiguration )

	print 'Configuration file saved'

	myConfigurationAux = myConfigurationFile.load()

	print 'Configuration file loaded'

	print myConfigurationAux
	print

