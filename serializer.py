# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:49:47 2019

@author: Sami
"""
N = 1000

import json
try:
    import pickle
except ModuleNotFoundError:
    print("Install pickle first using pip install pickle\n")
    exit(0)

import time

try:
    import yaml
except ModuleNotFoundError:
    print("Install PyYAML first using pip install PyYAML\n")
    exit(0)
try:
    import xmltodict
except ModuleNotFoundError:
    print("Install xmltodict first using pip install xmltodict\n")
    exit(0)
try:
    import msgpack
except ModuleNotFoundError:
    print("Install msgpack first using pip install msgpack\n")
    exit(0)


o = {
    "root": {
        "string": "This is a string",
        "integer": 51234,
        "float": 6.324234,
        "array": ["a", "b", "c"],
        "object": {
            "prop": "value",
            "arr": [1, 2, 3]
        },

    }
}

times = {}

# Native

start = time.time()
for i in range(0,N):
    serialized = pickle.dumps(o)
end1  = time.time()
for i in range(0,N):
    deserialized = pickle.loads(serialized)
end2 = time.time()
times["native"] = {"serialization": (end1 - start) / N, "deserialization": (end2 - end1) / N}

# XML
start = time.time()
for i in range(0,N):
    serialized = xmltodict.unparse(o, pretty=True)
end1  = time.time()
for i in range(0,N):
    deserialized = xmltodict.parse(serialized)
end2 = time.time()
times["xml"] = {"serialization": (end1 - start) / N, "deserialization": (end2 - end1) / N}

# JSON
start = time.time()
for i in range(0,N):
    serialized = json.dumps(o)
end1  = time.time()
for i in range(0,N):
    deserialized = json.loads(serialized)
end2 = time.time()
times["json"] = {"serialization": (end1 - start) / N, "deserialization": (end2 - end1) / N}

# MessagePack
start = time.time()
for i in range(0,N):
    serialized = msgpack.packb(o, use_bin_type=True)
end1  = time.time()
for i in range(0,N):
    deserialized = msgpack.unpackb(serialized, raw=False)
end2 = time.time()
times["msgpack"] = {"serialization": (end1 - start) / N, "deserialization": (end2 - end1) / N}


# YAML
start = time.time()
for i in range(0,N):
    serialized = yaml.dump(o)
end1  = time.time()
for i in range(0,N):
    deserialized = yaml.load(serialized)
end2 = time.time()
times["yaml"] = {"serialization": (end1 - start) / N, "deserialization": (end2 - end1) / N}

out = json.dumps(times, indent=2)
print(out)

print(times.keys())
print(times.values())

# plot
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

plt.show()