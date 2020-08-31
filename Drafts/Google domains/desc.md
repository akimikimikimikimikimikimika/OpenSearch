# `data.tsv` の説明

## 公式
- [supported domains](https://www.google.com/supported_domains) に掲載されているものを○にしている

## 検索
- 検索サービスを提供しているものを ○ としている。そのドメインで検索サービスが提供されていない場合 (別ドメインに転送される場合) は △ としている。

- 検索URLの基本形
	```
	https://www.google.com/webhp?gws_rd=cr&hl=ja&gl=ja
	https://www.google.com/search?q=検索キーワード&gws_rd=cr&hl=ja&gl=ja
	```
	`google.com` の箇所をそれぞれのドメインに置き換えたものになる

- △ の場合の用語解説

	* `転送 (google.*)`  
	当該ドメインで検索しようとすると別ドメインのページに転送される。括弧内に転送先のドメインを表示している

	* `search不可`  
	下段のように `search` で検索ができない

	* `webhp不可`  
	上段のように `webhp` でアクセスができない (エラーページ)。この場合は次のように `webhp` を消す
		```
		https://www.google.com/?gws_rd=cr&hl=ja&gl=ja
		```

	* `パラメタ削除`  
	上段のようにパラメタ付きでアクセスしても転送先で消えるので付ける意味がない

	* `www不可`  
	ドメインを `www.google.com` の代わりに `google.com` とする

	* `SSL不可`  
	HTTPSではアクセスできないので `http://` とする

	* `リンク`  
	`google.cn` は `google.co.hk` へのリンクのみが存在している

## ログイン

* ドメインごとにCookieは別なので、ログイン情報も別。それぞれに対するログインページがある。

* しかし、1度どこかでログインしていれば他のドメインへのログインは、そのドメインのログインページを開くだけでログインが完了する。

* ログインページのURLの基本形
	```
	https://accounts.google.com/ServiceLogin?hl=ja&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fwebhp%3Fgws_rd%3Dcr%26hl%3Dja%26gl%3Dja
	```
	- `continue` パラメタでログイン成功時に移動する先のアドレスを指定する。ここでは、検索のページに遷移するように指定している
	- `continue` の `www.google.com` をドメインごとに変更すれば、それぞれのドメインでのログインリンクが作成できる。
	- 一応 `continue` の遷移先が適切なリンクであるかは確認される模様。
	- `accounts.google.com` も `accounts.google.co.jp` のように変化させられるので、変化させる。

* ○ の付いたものはログイン可能である。然もなくば、ログインページにアクセスできないとか、ページにはアクセスできてもログインに失敗するとか。

## 地図

* 地図URLの基本形
	```
	https://maps.google.com/?hl=ja&q=キーワード
	https://www.google.com/maps?hl=ja&q=キーワード
	```
	どちらも `google.com` の箇所をそれぞれのドメインに置き換えたものになる

* 地図ページが存在するものを ○ としている

* `maps.*使用不可` というのは、上段のような `maps.google.com` のドメインは使用できないことを表す

* 現在 `maps.google.*` 系のドメインは全て `www.google.*/maps` に転送される

## 翻訳

* Google翻訳URLの基本形
	```
	https://translate.google.com/?hl=ja#view=home&op=translate&sl=auto&tl=ja&text=翻訳テキスト
	```
	- `google.com` の箇所をそれぞれのドメインに置き換えたものになる
	- `hl` はGoogle翻訳ページの表示言語、 `sl` は翻訳元の言語 (`auto` は自動検出)、 `tl` は翻訳先の言語
	- `op` を `translate` から `docs` にすれば書類の翻訳メニューを表示する

* 翻訳ページが存在するものを ○ としている

## ニュース

* ニュースURLの基本形
	```
	https://news.google.com/topstories?hl=ja&gl=JP&ceid=JP:ja
	https://www.google.com/topstories?hl=ja&gl=JP&ceid=JP:ja
	```
	どちらも `google.com` の箇所をそれぞれのドメインに置き換えたものになる

* ニュースページが存在するものを ○ としている

* `news.*使用不可` というのは、上段のような `news.google.com` のドメインは使用できないことを表す

* 現在は全て `news.google.com` にリダイレクトされる

## フライト検索

* Googleフライト検索URLの基本形
	```
	https://flights.google.com/?hl=ja
	```
	- `google.com` の箇所をそれぞれのドメインに置き換えたものになる