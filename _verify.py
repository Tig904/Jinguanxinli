import re, io

path = r"C:\Users\70073\Desktop\锦观心理测评\锦观心理测评.html"
html = io.open(path, encoding="utf-8").read()

m = re.search(r"/\* ====BANK_START==== \*/(.*?)/\* ====BANK_END==== \*/", html, re.S)
bank = m.group(1)

groups = ["teen", "young", "mid", "midold", "elder"]
total_ok = True
for g in groups:
    gm = re.search(r'key:"%s".*?q:\[(.*?)\]' % g, bank, re.S)
    if not gm:
        print("MISSING group:", g); total_ok=False; continue
    qstr = gm.group(1)
    qs = re.findall(r'^\s*"[^"]*",?\s*$', qstr, re.M)
    print(f"{g}: {len(qs)} 题")
    if len(qs) != 60:
        total_ok = False

for g in groups:
    gm = re.search(r'key:"%s".*?dims:\[(.*?)\].*?q:' % g, bank, re.S)
    if gm:
        d = re.findall(r'"[^"]*"', gm.group(1))
        print(f"{g}: dims = {len(d)}")
        if len(d) != 5: total_ok=False

print("ALL_OK" if total_ok else "HAS_ISSUE")
