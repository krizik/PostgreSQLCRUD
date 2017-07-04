from ConfigParser import ConfigParser
import sys
sys.dont_write_bytecode = True
 
def config(filename='database.ini', section='postgresql'):
	""" Parse database configuration 
	
	Args:
		filename (str): configuration file with connect credentials
		section (str): section name in configuration file

	Return:
		dict: keys are configuration variables names, 
		values are configuration variables vals

	"""
	# create a parser
	parser = ConfigParser()

	# read config file
	parser.read(filename)
 
	# get section, default to postgresql
	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
	return db