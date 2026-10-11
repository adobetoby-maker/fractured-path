import re
L='/Users/drive/fractured-path-monroe13/editions/monroe-1.3/book-07-void-roads/state/completion/laneB/'
def load(f):
    out={}; ch=None
    for l in open(L+f):
        m=re.match(r'(chapter-\d+)\.md\tsentences=(\d+)',l)
        if m: ch=m.group(1); out[ch]=[int(m.group(2)),0,0,[]]; continue
        m=re.match(r'\s+scene (\d+)\tn=(\d+)\tskeleton=(\d+)%\tclose=(\d+)%',l)
        if m and ch:
            n=int(m.group(2)); sk=round(int(m.group(3))*n/100); cl=round(int(m.group(4))*n/100)
            out[ch][1]+=sk; out[ch][2]+=cl; out[ch][3].append((n,sk,cl))
    return out
a=load('probe-scenes-pre-lanes.txt'); b=load('probe-scenes-manuscript.txt')
bad=0
for ch in sorted(a):
    x,y=a[ch],b[ch]
    rose = y[1]>x[1] or y[2]>x[2]
    bad+=rose
    print(ch,'sent',x[0],'->',y[0],'| skeleton',x[1],'->',y[1],'| close',x[2],'->',y[2],'  <-- numerator rose' if rose else '')
    if rose:
        for i,(p,q) in enumerate(zip(x[3],y[3]),1): print('     scene',i,p,'->',q)
print('chapters with a risen count:',bad)
