#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import re

os.chdir(os.path.dirname(os.path.join(os.getcwd(),__file__)))

def main():
	i=open("data.tsv","r")
	reader=csv.reader(i,delimiter="\t")
	for d in reader:
		if d[4]!="○": continue
		src=openSearch(d[3])
		o=open(f"../../Google/opensearch-domains/{d[3].lower()}.xml","w")
		o.write(src)
		o.close()
	i.close()

def openSearch(domain):
	src=f"""
		<?xml version="1.0" encoding="utf-8"?>
		<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/" xmlns:moz="http://www.mozilla.org/2006/browser/search/">
			<ShortName>{domain}</ShortName>
			<LongName>Google Search</LongName>
			<Description>Search on {domain}</Description>
			<InputEncoding>UTF-8</InputEncoding>
			<OutputEncoding>UTF-8</OutputEncoding>
			<Image height="16" width="16" type="image/x-icon">../images/google.ico</Image>
			<Image height="64" width="64" type="image/png">../images/google.png</Image>
			<Url type="text/html" rel="results" method="get" template="https://www.{domain.lower()}/search">
				<Param name="q" value="{{searchTerms}}" />
				<Param name="ie" value="utf-8" />
				<Param name="oe" value="utf-8" />
				<Param name="hl" value="ja" />
				<Param name="gl" value="ja" />
			</Url>
			<Url type="application/x-suggestion+json" method="get" template="https://suggestqueries.{domain.lower()}/complete/search">
				<Param name="q" value="{{searchTerms}}" />
				<Param name="ie" value="utf-8" />
				<Param name="oe" value="utf-8" />
				<Param name="hl" value="ja" />
				<Param name="output" value="firefox" />
			</Url>
			<Url type="application/opensearchdescription+xml" rel="self" template="https://akimikimikimikimikimikimika.github.io/Search/Google/opensearch-domains/{domain.lower()}.xml" />
			<moz:SearchForm>https://www.{domain.lower()}/webhp?ie=utf-8&amp;oe=utf-8&amp;hl=ja&amp;gl=ja</moz:SearchForm>
		</OpenSearchDescription>
	"""
	src=re.sub(r"(?m)^\t{1,2}","",src)
	src=re.sub(r"^\n+","",src)
	src=re.sub(r"\n+$","",src)
	return src

main()