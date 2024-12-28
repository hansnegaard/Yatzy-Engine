def score_cat(cat,d):
 d=sorted(d)
 if cat=='1':return d.count(1)*1
 if cat=='2':return d.count(2)*2
 if cat=='3':return d.count(3)*3
 if cat=='4':return d.count(4)*4
 if cat=='5':return d.count(5)*5
 if cat=='6':return d.count(6)*6
 if cat=='p':
  mx=0
  for i in range(1,7):
   if d.count(i)>=2 and i*2>mx:mx=i*2
  return mx
 if cat=='2p':
  pairs=[]
  for i in range(1,7):
   if d.count(i)>=2:pairs.append(i)
  if len(pairs)<2:return 0
  pairs=sorted(pairs)[-2:]
  return pairs[0]*2+pairs[1]*2
 if cat=='3k':
  for i in range(6,0,-1):
   if d.count(i)>=3:return i*3
  return 0
 if cat=='4k':
  for i in range(6,0,-1):
   if d.count(i)>=4:return i*4
  return 0
 if cat=='fh':
  has3=0
  has2=0
  three_val=0
  pair_val=0
  for i in range(1,7):
   if d.count(i)==3:has3=1;three_val=i*3
   if d.count(i)==2:has2=1;pair_val=i*2
  if has3 and has2:return three_val+pair_val
  return 0
 if cat=='s':return 15 if d==[1,2,3,4,5]else 0
 if cat=='l':return 20 if d==[2,3,4,5,6]else 0
 if cat=='c':return sum(d)
 if cat=='y':return 50 if len(set(d))==1 else 0
 return 0

def best_move(cat,d,rolls_left,memo):
 key=(cat,tuple(sorted(d)),rolls_left)
 if key in memo:return memo[key]
 if rolls_left==1:
  val=score_cat(cat,d)
  memo[key]=(val,tuple(d))
  return memo[key]
 best=-1
 keep=None
 from itertools import product
 for mask in range(1<<5):
  kept=[]
  idxs=[]
  for i in range(5):
   if mask&(1<<i):kept.append(d[i])
   else:idxs.append(i)
  ev=0
  total_outcomes=6**len(idxs)
  for outcome in product(range(1,7),repeat=len(idxs)):
   nd=sorted(kept+list(outcome))
   nxt=best_move(cat,nd,rolls_left-1,memo)[0]
   ev+=nxt
  ev/=total_outcomes
  if ev>best:
   best=ev
   keep=tuple(sorted(kept))
 memo[key]=(best,keep)
 return memo[key]

def main():
 cats={
 '1':'Ones','2':'Twos','3':'Threes','4':'Fours','5':'Fives','6':'Sixes','p':'One Pair','2p':'Two Pairs','3k':'Three of a Kind','4k':'Four of a Kind','fh':'Full House','s':'Small Straight','l':'Large Straight','c':'Chance','y':'Yahtzee'
 }
 for k in cats:print(cats[k]+': '+k)
 cat=input()
 memo={}
 rolls_left=3
 final_dice=[]
 for i in range(3):
  dice=input()
  d=[int(x) for x in dice]
  val,kept=best_move(cat,d,rolls_left,memo)
  print('Keep:',kept,'Expected:',round(val,2))
  final_dice=d
  rolls_left-=1
 print('Final Score:',score_cat(cat,final_dice))

if __name__=='__main__':
 main()
