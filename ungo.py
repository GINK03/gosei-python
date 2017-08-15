
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
