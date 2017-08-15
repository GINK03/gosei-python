# 五省-蛇

## import thisの哲学
```console
>>> import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## これはシーザ暗号で作られています
まぁかっこいいので私もthisモジュールを変更しようと試みたことがあったのですが、find . | xargs grep foobarをしても一向に見つかりません  
なぜでしょうか。

pythonのソースコードを読む必要があって読んでいたのですが、どうやら、シーザ暗号という暗号が施されたリテラルが記述してあり、それを動的に解析しているらしいとうことが
わかりました。

実際の実装はこのようになっています。
```python
s = """Gur Mra bs Clguba, ol Gvz Crgref
Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
```
うまくやれば日本語で同様の暗号化を利用して、任意のリテラルを表示できそうです

## シーザ暗号とは
アルファベットは26文字しかなく、その位置を数字に対応させることが容易です　　

数字に対応させた文字を任意の数字を足し合わせて26のあまりを求めることにより、任意の文字文だけ、ローテーションできることがわかります　　

日本語は漢字も合わせると膨大ですが、果たして同様の暗号は可能なのでしょうか  

UTF8などは辞書順などで定義されており、一定の順序構造が文字に割り当てられています  

全てを連続値にする必要はなく、暗号化対象の文字のみに限定すれば、暗号化することができます

### 五省の暗号化
暗号化する意味があるのかわからないですが、Pythonのリテラル埋め込み文化に従うのであれば、暗号化しておくことが良さそうです
```python
source = """一、至誠にもとるなかりしか
真心に反する点はなかったか
一、言行に恥はづるなかりしか
言行不一致な点はなかったか
一、気力にかくるなかりしか
精神力は十分であったか
一、努力にうらみなかりしか
十分に努力したか
一、不精にわたるなかりしか
最後まで十分に取り組んだか"""

d = {}
for i,c in enumerate(sorted(list(set(source)))):
  d[i] = c

ungo = {}
for i, c in d.items():
  ungo[c] = d[(i+1)%len(d)]

print( "".join([ungo[c] for c in list(source)]) )
```
### 五省の暗号化の復号化
こんな風に復号します
```python
s = """不あ致
はらなわにくるすく、神恥は取たわ真まにくづだく、不あ誠言は最までわにくるすく、誠言分不行に真まにくづだく、不あ点努はくしわにくるすく、組精努ま反力とうづだく、不あ十努はかりもにくるすく、反力は十努
すだく、不あ分組はんだわにくるすく、気心みと反力は後る至一っく"""

d = {}
for i,c in enumerate(sorted(list(set(s)))):
  d[i] = c

ungo = {}
for i, c in d.items():
  ungo[c] = d[abs(i-1)%len(d)]

print( "".join([ungo[c] for c in list(s)]) )
```

### pythonのソースコードに組み込む
DjangoやいくつかのPurePythonで書かれたモジュールならば、Pythonに組み込むことができます  
例えば、thisモジュールならばここを編集します  
```console
$ ls Python-3.6.2/Lib/this.py
```no```c
pythonのソースコードであるここ
