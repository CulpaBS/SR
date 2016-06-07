import json, sys

def flatten(unflattened):
    for l in unflattened:
        if type(l) is list:
            for sub in l:
                yield sub
        else:
            yield l
        

if len(sys.argv) < 2:
    print "usage: python flatten <file>.json"
    sys.exit(-1)
else:
    filename = sys.argv[1]


with open(filename, "r") as f:
    unflat = json.load(f)
    flat = {}
    for k in unflat.keys():
        flat[k] = list(flatten(unflat[k]))


with open(filename[0:-5] + "_fixed.json", "w") as f:
    json.dump(flat, f)