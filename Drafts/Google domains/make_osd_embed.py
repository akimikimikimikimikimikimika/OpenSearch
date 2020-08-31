#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import re

os.chdir(os.path.dirname(os.path.join(os.getcwd(),__file__)))

i=open("data.tsv","r")
reader=csv.reader(i,delimiter="\t")
o=[]
for d in reader:
	if d[4]!="○": continue
	o.append(f"<link rel=\"search\" type=\"application/opensearchdescription+xml\" title=\"{d[3]}\" href=\"opensearch-domains/{d[3].lower()}.xml\" />")
print("\n".join(o),end="")