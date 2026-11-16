#!/usr/bin/env python3
"""Bundle template + libraries + data into one self-contained index.html."""
import json, glob, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ORDER = ["g7", "g20", "apec", "oecd", "wto", "brics", "rcep", "cptpp", "usmca", "opec",
         "un", "nato", "eu", "sco",
         "asean", "au", "arab_league", "mercosur",
         "imf", "aiib", "taiwan_allies"]

def rd(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()

orgs = {}
for f in glob.glob(os.path.join(ROOT, "data/orgs/*.json")):
    o = json.load(open(f, encoding="utf-8"))
    o.setdefault("non_state_members", [])
    orgs[o["id"]] = o
missing = [i for i in ORDER if i not in orgs]
if missing: print("WARNING missing orgs:", missing, file=sys.stderr)
org_list = [orgs[i] for i in ORDER if i in orgs] + [o for k, o in orgs.items() if k not in ORDER]

cdata = json.load(open(os.path.join(ROOT, "data/countries.json"), encoding="utf-8"))
countries = cdata["countries"]
iso_set = {c["iso3"] for c in countries}
for o in org_list:
    bad = [m["iso3"] for m in o["members"] if m["iso3"] not in iso_set]
    if bad: print(f"WARNING {o['id']}: iso3 not in countries.json: {bad}", file=sys.stderr)
    for m in o["members"]:
        if m["status"] not in o["status_labels"]:
            print(f"WARNING {o['id']}: status {m['status']} has no label", file=sys.stderr)

as_of = max(o.get("as_of", "") for o in org_list) or cdata.get("as_of", "")
topo = json.load(open(os.path.join(ROOT, "node_modules/world-atlas/countries-50m.json")))
flags = {}
fdir = os.path.join(ROOT, "node_modules/country-flag-icons/3x2")
for c in countries:
    f = os.path.join(fdir, (c.get("iso2") or "").upper() + ".svg")
    if c.get("iso2") and os.path.exists(f): flags[c["iso2"].upper()] = open(f, encoding="utf-8").read().strip()
print("flags:", len(flags), "missing:", [c["iso3"] for c in countries if (c.get("iso2") or "").upper() not in flags], file=sys.stderr)
extras = {}
for f in glob.glob(os.path.join(ROOT, "data/extras/*.json")):
    try:
        x = json.load(open(f, encoding="utf-8")); extras[x["id"]] = x
    except Exception as e:
        print("WARNING bad extras", f, e, file=sys.stderr)
print("extras:", sorted(extras), file=sys.stderr)
data = {"extras": extras, "flags": flags, "orgs": org_list, "countries": countries, "topo": topo, "asOf": as_of,
        "extraPoints": [{"iso3": "TUV", "lat": -8.52, "lon": 179.2}]}

libs = rd("node_modules/d3/dist/d3.min.js") + "\n" + rd("node_modules/topojson-client/dist/topojson-client.min.js")
html = rd("src/template.html").replace("/*__LIBS__*/", libs.replace("</script", "<\\/script"))
html = html.replace("/*__DATA__*/", json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
open(os.path.join(ROOT, "dist/index.html"), "w", encoding="utf-8").write(html)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)  # served by GitHub Pages
print(f"Built dist/index.html: {len(html)/1024:.0f} KB, {len(org_list)} orgs, {len(countries)} countries")
