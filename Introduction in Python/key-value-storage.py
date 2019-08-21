import argparse
import os
import tempfile
import json
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()


temp = tempfile.NamedTemporaryFile(delete=False)
storage_path = os.path.join(tempfile.gettempdir(), 'storage.json')


def keyValue():
    if not os.path.exists(storage_path):
        with open(storage_path, 'w+') as f:
            pass
    if args.value:
        # пишем в базу если есть вэлью
        jsonRead = open(storage_path, 'r')
        try:
            data = json.load(jsonRead)
        except:
            data = {}
        jsonRead.close()
        with open(storage_path, 'w') as f:
            if args.key in data:
                data[args.key] = data[args.key] + ', ' + args.value
            else:
                data[args.key] = args.value
            json.dump(data, f)
    elif args.key:
        try:
            with open(storage_path, 'r') as f:
                data = json.load(f)
                if args.key in data:
                    print(data[args.key])
                else:
                    print(None)
        except:
            print(None)


keyValue()
