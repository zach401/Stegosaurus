import sys
import getpass
import Stegosaurus

in_image = sys.argv[1]
out_image = sys.argv[2]
message_file = sys.argv[3]

print(str(sys.argv))

pwd= getpass.getpass('Password:')

with open(message_file, 'r') as f:
	message = f.read()
	Stegosaurus.encode(in_image, out_image, message, pwd)
