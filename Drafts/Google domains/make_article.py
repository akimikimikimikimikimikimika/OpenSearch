#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re

os.chdir(os.path.dirname(os.path.join(os.getcwd(),__file__)))

io=open("data.tsv","r")
raw=io.read().split("\n")[1:]
io.close()

# 🔍🔓🗺🔄

data="""
Google検索で使われているccTLD (国別コードドメイン) の一覧。それぞれのページへのリンクも貼ってある。

- 現在分かっている範囲内で記した。
- ccTLDが割り当てられた国から「想定される地域」を表記したが、必ずそれが正しいとは言えない。
- 各々「ドメイン」にはGoogle検索のページへのリンクが貼ってある
	* 使用言語も検索結果も日本語になるようにパラメタを指定してある。つまりどれを使っても同じ挙動を示す。
	* Googleは [supported domains](https://www.google.com/supported_domains) なるページを用意しており、そこに掲載されているドメインであれば太字にしている。太字でないものの中にはGoogleがホストしているかどうか怪しいものもある。
- 「実在」が ○ のものはそのドメインのページがあることを示す。 × の場合は別のドメインへのリダイレクトである。
- ブラウザのCookieの特性上、特定のドメインでGoogleアカウントにログインしても、他のドメインではログインされていない。
	* 例えば、google.comでログインしても、そのままではgoogle.co.ukではログインされていない。
	* 日本ではgoogle.comにログインすればgoogle.co.jpにもログインされる。
	* 表中の 「🔓」 のリンクを開けば、Googleアカウントへのログインが要求される。既にgoogle.comでログインしている場合にはそのドメインにすぐログインされる。リンクがないものはログインができない模様。
- 検索以外にもGoogleマップやGoogle翻訳もドメイン固有になっており「🗺」や「🔄」にリンクを貼っている
- リダイレクトされるだけのものも含む
	* google.euは未だにgoogle.co.ukにリダイレクトされている
- google.cn では検索できない。(過去の遺物?) google.com.hk へのリンクがあるのみ。
- 時間が経てばこの情報も変化したり、誤りがある場合もあるので、適宜修正していく。又、間違いがあったら指摘してください。

| 想定される国・地域 | ドメイン | 実在 | | | |
|:--|:--|:-:|:-:|:-:|:-:|
"""
for r in raw:
	r=r.split("\t")
	tld=re.search(r"(?i)[a-z]{5,}\.([a-z\.]+)$",r[3]).group(1)

	s="https" if "SSL不可" not in r[5] else "http"
	s+="://"
	if "www不可" not in r[5]: s+="www."
	s+=r[3].lower()+"/"
	if "webhp不可" not in r[5]: s+="webhp"
	if ("リンク" not in r[5]) and ("パラメタ削除" not in r[5]): s+="?gws_rd=cr&hl=ja&gl=ja"

	if r[6]=="×": l=""
	else:
		l="com" if ".comでログイン" in r[6] else tld
		l=f"""[🔓](https://accounts.google.{l}/ServiceLogin?hl=ja&passive=true&continue=https%3A%2F%2Fwww.{r[3].lower()}%2F{"webhp" if "webhp不可" not in r[5] else ""}%3Fgws_rd%3Dcr%26hl%3Dja%26gl%3Dja "{r[3]}")"""

	if r[7]=="×": m=""
	else:
		m=f"www.google.{tld}/maps" if "maps.*使用不可" in r[7] else f"maps.google.{tld}/"
		m=f"""[🗺](https://{m}?hl=ja "{r[3]}")"""

	if r[8]=="×": t=""
	else:
		t=f"www.google.{tld}/translate" if "translate.*使用不可" in r[7] else f"translate.google.{tld}/"
		t=f"""[🔄](https://{t}?hl=ja "{r[3]}")"""

	data+=f"""| {r[0]} {r[1]} | [{f"**{r[3]}**" if "○" in r[4] else r[3]}]({s} "{r[3]}") | {f"×" if "転送" in r[5] else "○"} | {l} | {m} | {t} |\n"""

data.replace("   "," ")

data+="""
参考
- [Google公式のドメイン一覧](https://www.google.com/supported_domains)
- [Infogalacticのページ](https://infogalactic.com/info/List_of_Google_domains)
"""

io=open("article.md","w")
io.write(data)
io.close()