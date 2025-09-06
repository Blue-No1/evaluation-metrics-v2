import json, glob
vals = []
for p in glob.glob("results/*.json"):
    with open(p) as f: vals.append(json.load(f))
print("Summary:")
for v in vals:
    print(f"- {v['task']} {v['metric']}: {v['value']}")
