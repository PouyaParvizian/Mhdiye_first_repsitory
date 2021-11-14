import random as rn
N=5
numY_N= rn.randint(1, 2)
numSH_A=rn.randint(1,2)
numM_CH=5-(numSH_A+numY_N)
Score=0
Correct=0
Wrong=0
out={'Correct':0,'Wrong':0,'Score':0 ,'Remaining':N}
Y_Nd= {'Is yogurt white?(Yes or No)':'Yes', 'Does the snake have armpits?(Yes or No)':'Yes', 'Is it dark at night?(Yes or No)':'No'}
Y_Ndout= {'Is yogurt white?(Yes or No)':'Nooooooo?!!!!!! :@', 'Does the snake have armpits?(Yes or No)':'Why not? If you look more closely, you will find :) ', 'Is it dark at night?(Yes or No)':'No Because you have lamp '}
Y_Nl= ['Is yogurt white?(Yes or No)', 'Does the snake have armpits?(Yes or No)', 'Is it dark at night?(Yes or No)']
SH_Ad={'Why does the penguin not have a knee? ':'Because fat','If you drive on a road that is full of shards of glass on your right, then which tire will never be punctured?':'Spare tire','Where was the signing of the Turkmenchay contract?':'down the page'}
SH_Adout={'Why does the penguin not have a knee? ':'Because fat :(','If you drive on a road that is full of shards of glass on your right, then which tire will never be punctured?':'Spare tire its Very clear','Where was the signing of the Turkmenchay contract?':'down the page ha ha ha'}
SH_Al=['Why does the penguin not have a knee? ','If you drive on a road that is full of shards of glass on your right, then which tire will never be punctured?','Where was the signing of the Turkmenchay contract?']
M_CHl=['What color is a blue car seen under yellow light? (a:Blue b:Green C:Yellow d:White :/ )','Who is our common war with??  a:Dr.Siabi :() b:Spider man c:joker d:Corona ','Which is faster? a:motoGP  b:Formola1 c:F-16 d:Weekend ' ]
M_CHd={'What color is a blue car seen under yellow light? (a:Blue b:Green C:Yellow d:White :/ )':'b','Who is our common war with??  a:Dr.Siabi :() b:Spider man c:joker d:Corona ':'d','Which is faster? a:motoGP  b:Formola1 c:F-16 d:Weekend ':'d' }
M_CHdout={'What color is a blue car seen under yellow light? (a:Blue b:Green C:Yellow d:White :/ )':'Blue is Correct ','Who is our common war with??  a:Dr.Siabi :() b:Spider man c:joker d:Corona ':'Shame on you  its Coronaaaa :/  ','Which is faster? a:motoGP  b:Formola1 c:F-16 d:Weekend ':' Weekend :(' }
class Y_N:
    def yn(self,a):
        self.a=a
        self.j = input(self.a)
        if Y_Nd[self.a]==self.j:
            return 'Correct'
        elif  self.j=='Next':
           return self.j
        else:
            print(Y_Ndout[self.a])
            return  'Wrong'
        del Y_Nl[Y_Nl.index(self.a)]


class SH_A:
    def sh(self,b):
        self.b=b
        self.k = input(self.b)
        if SH_Ad[self.b]==self.k:
            return 'Correct'
        elif  self.k=='Next':
           return self.k
        else:
            print(SH_Adout[self.b]," " )
            return  'Wrong'
        del SH_Al[SH_Al.index(self.b)]


class M_CH:
    def ch(self,t):
        self.t=t
        self.j = input(self.t)
        if M_CHd[self.t]==self.j:
            return 'Correct'
        elif  self.j=='Next':
           return self.j
        else:
            print(M_CHdout[self.t])
            return  'Wrong'
        del M_CHl[M_CHl.index(self.t)]


obY_N=Y_N()
obSH_A=SH_A()
obM_CH=M_CH()
for i in range (numY_N):
    N-=1
    out['Remaining'] = N
    g=rn.choice(Y_Nl)
    h=obY_N.yn(g)
    if h=='Correct':
        Score+=10
        Correct+=1
        out['Score']=Score
        out['Correct'] = Correct
        print(out)
    elif h=='Wrong':
        Score-=3
        Wrong+=1
        out['Score'] = Score
        out['Wrong'] = Wrong
        print(out)
    else:
        print(out)

for i in range (numSH_A):
    N-=1
    out['Remaining'] = N
    v=obSH_A.sh(rn.choice(SH_Al))
    if v=='Correct':
        Score+=10
        Correct+=1
        out['Score']=Score
        out['Correct'] = Correct
        print(out)
    elif v=='Wrong':
        Score-=3
        Wrong+=1
        out['Score'] = Score
        out['Wrong'] = Wrong
        print(out)
    else:
        print(out)

for i in range (numM_CH):
    N-=1
    out['Remaining'] = N
    p=obM_CH.ch(rn.choice(M_CHl))
    if p=='Correct':
        Score+=10
        Correct+=1
        out['Score']=Score
        out['Correct'] = Correct
        print(out)

    elif p=='Wrong':
        Score-=3
        Wrong+=1
        out['Score'] = Score
        out['Wrong'] = Wrong
        print(out)

    else:
        print(out)

if Score>40:
    print('You Win :)')




