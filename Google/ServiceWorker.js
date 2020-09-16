importScripts("../../Library/SW/SW.js");

let img=["google.svg","googlemaps.svg","googlenews.svg","googletranslate.svg"];
cacheManager({
	name:"Search - Google",
	build:[2020,9,16],
	list:["index.html"].concat(img.map(v=>"images/"+v))
});