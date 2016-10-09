import sys
import getpass
import Stegosaurus

in_image = sys.argv[1]
pwd= getpass.getpass('Password:')

message = Stegosaurus.decode(in_image, pwd)
print(message)
to_save = input('Save Message?')
if to_save in ['Y', 'y']:
	file_name = input('File Name:')
	with open(file_name, 'w') as f:
		f.write(message)
