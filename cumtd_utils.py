import json

from cumtd import CUMTD

mtd = CUMTD()

a = mtd.get_stops()
print(json.dumps(a, indent=4))
