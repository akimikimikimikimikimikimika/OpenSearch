importScripts("../../Library/SW/SW.js");

let img=["JavaScript.svg","Python.svg","Ruby.svg","PHP.svg","Go.svg","Rust,svg","C++.svg","C%23.svg"];
cacheManager({
	name:"Search - Coding",
	build:[2020,9,16],
	list:["index.html"].concat(img.map(i=>"images/"+i))
});