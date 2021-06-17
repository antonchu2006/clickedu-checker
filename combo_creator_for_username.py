#!/usr/bin/env python
import sys

if len(sys.argv) != 3:
    print("\n[!] Uso: " + sys.argv[0] + " <combo-file> <username to bruteforce>")
    sys.exit(1)

filename = sys.argv[1]
output_fname = "combo_" + sys.argv[2] + ".txt"
output = open(output_fname, 'w')

with open(filename) as f:
    content = f.readlines()

for line in content:
    line = line.strip("\n")
    l = line.split(":")
    passwd = str(l[1])
    user = sys.argv[2]

    line_parsed = str(user +  ":" + passwd)
    print(line_parsed)
    output.write(line_parsed + "\n")
output.close()
