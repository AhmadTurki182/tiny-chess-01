import os,json,urllib.request as u
# v15 NB135k D6
VL=(0,100,320,330,500,900,0)
KN=(-33,-31,-18,-14,14,18,31,33)
KG=(-17,-16,-15,-1,1,15,16,17)
R0=(-16,-1,1,16);DQ=(-17,-15,15,17);Q0=R0+DQ
T=[[0]*128 for _ in range(7)]
for i in range(128):
 f=i&7;r=i>>4;c=7-abs(2*f-7)-abs(2*r-7)
 T[1][i],T[2][i],T[3][i],T[4][i],T[5][i]=100+6*r+(8 if 2<f<5 else 0),320+5*c,330+3*c,500+3*c,900+2*c
M=[15]*128;M[4]=12;M[7]=14;M[0]=13;M[116]=3;M[119]=11;M[112]=7
B=[0]*128;C=0;W=1;KS=[0,0]
U=[];TT={};KL=[0]*256
ND=0;NB=135000;BM=0
O=os.environ.get('MAKEFUN_ENV_URL','')
s='abcdefgh'
def F(g):
 global B,C,W,KS
 B=[0]*128
 a=g.split();W=a[1]=='w'
 i=112
 for ch in a[0]:
  if ch=='/':i-=24
  elif ch.isdigit():i+=int(ch)
  else:
   k='PNBRQKpnbrqk'.index(ch);p=k%6+1
   if k>5:p=-p
   B[i]=p
   if abs(p)==6:KS[p>0]=i
   i+=1
 C=sum(1<<'KQkq'.index(c)for c in a[2]if c in'KQkq')
def A(s,w):
 q=2*w-1
 for d in KN:
  t=s+d
  if not t&136 and B[t]==2*q:return 1
 for d in KG:
  t=s+d
  if not t&136:
   v=B[t]
   if v==6*q or v==q and abs(d)in(15,17)and d*q<0:return 1
 for d in Q0:
  t=s+d
  while not t&136:
   v=B[t]
   if v:
    if v in(5*q,4*q if d in R0 else 3*q):return 1
    break
   t+=d
 return 0
def G(w):
 Y=[]
 for s in range(128):
  p=B[s]
  if not p or(p>0)!=w:continue
  a=abs(p)
  if a==1:
   d=32*w-16
   for o in(-1,0,1):
    t=s+d+o
    if t&136:continue
    v=B[t]
    if o==0 and not v or o and v and(v>0)!=w:
     r=81920*((t>>4)%7==0)
     Y.append(s|t<<7|r)
     if o==0 and(s>>4)==6-5*w and not B[s+2*d]:Y.append(s|(s+2*d)<<7)
  else:
   D=(KN,DQ,R0,Q0,KG)[a-2]
   for d in D:
    t=s+d
    while not t&136:
     v=B[t]
     if not v or(v>0)!=w:Y.append(s|t<<7)
     if v or a in(2,6):break
     t+=d
   if a==6 and s==116-112*w:
    v=1-w
    for o in(2,-2):
     b=1<<(2-2*w+(o<0))
     if C&b and not B[s+o//2] and not B[s+o] and(o>0 or not B[s-3]) and not(A(s,v)|A(s+o//2,v)):Y.append(s|s+o<<7)
 return Y
def K(m):
 global C,KS,W
 f=m&127;t=m>>7&127;r=m>>14
 p=B[f];v=B[t]
 U.append((m,v,C))
 q=r*(2*(p>0)-1)or p
 B[t]=q;B[f]=0
 if abs(p)==6:
  KS[p>0]=t
  if abs(t-f)==2:B[t-1 if t>f else t+1]=B[t+1 if t>f else t-2];B[t+1 if t>f else t-2]=0
 C&=M[f]&M[t]
 W=1-W
def N():
 global C,KS,W
 m,v,c0=U.pop()
 f=m&127;t=m>>7&127;r=m>>14
 p=B[t]
 B[f]=r and(2*(p>0)-1)or p
 B[t]=0
 if v:B[t]=v
 if abs(p)==6:
  KS[p>0]=f
  if abs(t-f)==2:B[t+1 if t>f else t-2]=B[t-1 if t>f else t+1];B[t-1 if t>f else t+1]=0
 C=c0;W=1-W
def EV():
 s=0
 for i,p in enumerate(B):
  if p:
   a=abs(p)
   v=T[a][i if p>0 else i^112]
   s+=v*(2*(p>0)-1)
 return s if W else -s
def S(d,a,b,pl):
 global ND,BM
 ND+=1
 if ND>NB:raise TimeoutError
 if d<-10:return EV()
 h=bytes([x+6 for x in B]+[W,C])
 e=TT.get(h)
 if d>0 and e and e[0]>=d and(e[1]==0 or e[1]==1 and e[2]>=b):return e[2]
 ic=A(KS[W],not W)
 if d>0 and ic:d+=1
 if d<=0:
  s=EV()
  if s>=b:return b
  if s>a:a=s
 Y=G(W)
 if d>0:Y.sort(key=lambda m:((e and m==e[3] or 0)<<20)+VL[abs(B[m>>7&127])]+90000*(m>>14>0)+(m in KL[pl*2:pl*2+2]),reverse=True)
 bs=-10**6;bm=0;fl=2
 for m in Y:
  if d<=0:
   t=m>>7&127;v=B[t]
   if not v and not m>>14:continue
   c=VL[abs(v)]+800*(m>>14>0)
   if s+c<a:continue
  K(m)
  if A(KS[not W],W):N();continue
  x=-S(d-1,-b,-a,pl+1)
  N()
  if x>bs:bs=x;bm=m
  if x>a:
   a=x;fl=0
   if a>=b:
    fl=1
    if not B[m>>7&127]:KL[pl*2+1]=KL[pl*2];KL[pl*2]=m
    break
 if bs==-10**6:return a if d<=0 else(pl-99999 if ic else 0)
 if pl==0:BM=bm
 if d>0:TT[h]=(d,fl,bs,bm)
 return a if d<=0 else bs
def UC(m):
 f=m&127;t=m>>7&127
 return s[f&7]+str((f>>4)+1)+s[t&7]+str((t>>4)+1)+('q' if m>>14 else '')
def RT(lm):
 global ND,BM
 BM=0;ND=0
 for d in range(1,7):
  try:S(d,-10**6,10**6,0)
  except TimeoutError:break
 return UC(BM)if BM else lm[0]
def PO(p,d):
 return json.load(u.urlopen(O+p,json.dumps(d).encode()))
def main():
 while 1:
  g=PO('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   try:F(g['fen']);L=g['legal_moves'];g=PO('/move',{'game':g['game'],'move':RT(L)})
   except Exception:g=PO('/move',{'game':g['game'],'move':L[0]})
if __name__=='__main__':main()
