import json, sys

result = {"vulnerabilities":[]}

with open(sys.argv[1], "r") as f:
    vulns = json.load(f)
    for i in vulns["site"][0]["alerts"]:
        result["vulnerabilities"].append({"name": i["alert"], "count":i["count"]})

with open("output.json", "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

#python3 jsonparse.py ./2023-12-16-ZAP-Report-.json