# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:49:47 2019

@author: Sami
"""

import json
import pickle
import time
import yaml
import xmltodict
import msgpack

o = {
 "string": "This is a string",
 "integer": 51234,
 "float": 6.324234,
 "array": ["a", "b", "c"],
 "object": {"prop": "value", "arr": [1,2,3]},
 }

times = {}

# Native

start = time.time()
serialized = pickle.dumps(o)
end1  = time.time()
deserialized = pickle.loads(serialized)
end2 = time.time()
times["native"] = {"serialization": end1 - start, "deserialization": end2 - end1}

# XML
start = time.time()
serialized = xmltodict.unparse(o, pretty=True)
print(serialized)
end1  = time.time()
deserialized = xmltodict.parse(serialized)
end2 = time.time()
times["xml"] = {"serialization": end1 - start, "deserialization": end2 - end1}

# JSON
start = time.time()
serialized = json.dumps(o)
end1  = time.time()
deserialized = json.loads(serialized)
end2 = time.time()
times["json"] = {"serialization": end1 - start, "deserialization": end2 - end1}

# MessagePack
start = time.time()
serialized = msgpack.packb(o, use_bin_type=True)
end1  = time.time()
deserialized = msgpack.unpackb(serialized, raw=False)
print(deserialized)
end2 = time.time()
times["msgpack"] = {"serialization": end1 - start, "deserialization": end2 - end1}


# YAML
start = time.time()
serialized = yaml.dump(o)
end1  = time.time()
deserialized = yaml.load(serialized)
end2 = time.time()
times["yaml"] = {"serialization": end1 - start, "deserialization": end2 - end1}

# plot
import matplotlib.pyplot as plt
import numpy as np

