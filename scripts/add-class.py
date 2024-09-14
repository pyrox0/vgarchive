#!/usr/bin/env python
import json

classes = json.load(open("./scripts/classes.json"))

to_add = input("Class to add:")

if to_add not in classes:
    classes.append(to_add)
else:
    raise Exception("Class already exists!")

file = open("./scripts/classes.json", "w")

file.write(json.dumps(sorted(classes), sort_keys=True, indent=2).rstrip())
file.close()
