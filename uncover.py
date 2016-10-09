import sys
import getpass
import Encode

in_image = sys.argv[1]
pwd= getpass.getpass('Password:')

message = Encode.decode(in_image, pwd)
print(message)
to_save = input('Save Message?')
if to_save in ['Y', 'y']:
	file_name = input('File Name:')
	with open(file_name, 'w') as f:
		f.write(message)