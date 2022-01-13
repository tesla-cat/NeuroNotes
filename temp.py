with open('temp.txt','r', encoding='utf8') as f:
    x = f.read()

words = x.split(' ')
s = set()
for w in words:
    z = w.lower()
    if 'seq' in z and ' seq' not in z and 'sequ' not in z:
        s.add(w)

for w in s:
    print(w)

"""
FISSEQ
MAPseq
BaristaSeq
MiSeq
scRNA-seq
Perturb-Seq
"""