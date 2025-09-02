import json, sys
preds = ["82", "132"]  # placeholder; later read from a file
with open("probes/simple_math.jsonl") as f:
    gold = [json.loads(x)["target"] for x in f]
em = sum(p.strip()==g.strip() for p,g in zip(preds,gold)) / len(gold)
print(f"Exact match: {em:.2f}")
