import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def get_file_data():
	print('INSIDEEEEEEEEEEEEEEEEEEEEEEEE get_file_data')
	with open(storage_path, 'r') as f:
		raw_data = f.read()
		if raw_data:
			return json.loads(raw_data)

		return {}

def place_key_val_in_file(key, val):
	print('Placing key-val in the file')
	data = get_file_data()
	print('Here is the data: ', data)
	if key in data:
		data[key].append(val)
	else:
		data[key] = [val]

	with open(storage_path, 'w') as f:
		f.write(json.dumps(data))

	print('Think i placed ...')

def print_val_by_key(key):
	print('Later i will search the file for this key: ', key)

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')

args = parser.parse_args()

if args.key and args.val:
	place_key_val_in_file(args.key, args.val)
#elif args.key:
#	#print_val_by_key(args.key)
#else:
#	print('Error: there is no arguments!')

print(args)
