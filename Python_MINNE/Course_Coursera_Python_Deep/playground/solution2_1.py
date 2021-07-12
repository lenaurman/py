import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def get_file_data():
        if not os.path.exists(storage_path):
            return {}
            
        with open(storage_path, 'r') as f:
                raw_data = f.read()
                if raw_data:
                        return json.loads(raw_data)

                return {}

def place_key_val_in_file(key, val):
        data = get_file_data()
        if key in data:
                data[key].append(val)
        else:
                data[key] = [val]

        with open(storage_path, 'w') as f:
                f.write(json.dumps(data))

def print_val_by_key(key):
        data = get_file_data() 
        values = data.get(key)        
        if values is None:
            print('None')
        elif len(values) > 0:
            print(*values, sep = ", ")
        else:
            print(values[0])        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')

    args = parser.parse_args()

    if args.key and args.val:
            place_key_val_in_file(args.key, args.val)
    elif args.key:
            print_val_by_key(args.key)
    else:
        print('Something wrong with your arguments!')

