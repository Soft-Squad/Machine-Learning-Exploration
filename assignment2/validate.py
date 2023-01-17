# Run as python3 validate.py assignment1.zip

import zipfile, sys, os, re
from pathlib import Path

def check_name(name):
	pattern = r'(V[0-9]{8})_([A-Za-z].+)_([0-9]{2}).ipynb'
	m = re.match(pattern, name)
	if m:
		return (m[1], m[2], int(m[3]))
	return None

total_problems = 4
probs = [False] * total_problems
try:
	f = sys.argv[1]
	zip = zipfile.ZipFile(f)
	vids, names, ignored = set(), set(), set()
	for i in zip.namelist():
		p = Path(i)
		if str(p.parent) == "." and p.suffix.lower() == ".ipynb":
			m = check_name(str(p.name))
			if m:
				vid, name, pnum = m
				vids.add(vid)
				names.add(name)
				probs[pnum-1] = True
				if 1 <= pnum <= total_problems:
					print(f"OK: Found problem {pnum}: {p.name}")
					continue
		ignored.add(i)
	print()

	if len(vids) > 1:
		print(f"ERROR: Inconsistent V number: provided {vids}")
	if len(names) > 1:
		print(f"ERROR: Inconsistent student name: provided {names}")
	for i in ignored:
		print(f"WARNING: Ignoring file {i}")
except:
	print(f"ERROR: file not found and/or no zip file found")

print()
if sum(probs):
	print(f"OK: Sumbitted {sum(probs)} / {total_problems} problems:", end=' ')
	print(f"[{', '.join(str(i+1) for i in range(total_problems) if probs[i])}]")
else:
	print(f"ERROR: No submissions found. DO NOT SUBMIT.")
