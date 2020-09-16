importScripts("../../Library/SW/SW.js");

let img=["Wikipedia.svg","Wiktionary.svg","Wikibooks.svg","Wikisource.svg","Wikiversity.svg","Wikinews.svg","Wikiquote.svg","Wikivoyage.svg","Wikispecies.svg","Wikidata.svg","Meta-Wiki.svg","Commons.svg"];
cacheManager({
	name:"Search - Wikipedia",
	build:[2020,9,16],
	list:["index.html"].concat(img.map(i=>"images/"+i))
});