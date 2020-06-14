def compute(line):
    def fcomp(comp):
        a0=['0','1','-1','D','A','!D','!A','-D','-A','D+1','A+1','D-1','A-1','D+A','D-A','A-D','D&A','D|A']
        a1=[None,None,None,None,'M',None,'!M',None,'-M',None,'M+1',None,'M-1','D+M','D-M','M-D','D&M','D|M']
        Binary=['101010',
                '111111',
                '111010',
                '001100',
                '110000',
                '001101',
                '110001',
                '001111',
                '110011',
                '011111',
                '110111',
                '001110',
                '110010',
                '000010',
                '010011',
                '000111',
                '000000',
                '010101']
        
        if comp in a0:
            a='0'
            b=a0.index(comp)
        elif comp in a1:
            a='1'
            b=a1.index(comp)
        Bin=Binary[b]
        return (a+Bin)

    def fdest(dest):
        value=['null','M','D','MD','A','AM','AD','AMD']
        Binary=[
         '000', 
         '001', 
         '010', 
         '011', 
         '100',
         '101',
         '110', 
         '111', 
            ]
        if dest in value:
            Bin=Binary[value.index(dest)]
        return Bin

    def fjump(jump):
        value=['null','JGT','JEQ','JGE','JLT','JNE','JLE','JMP']
        Binary=[
            '000',
            '001',
            '010',
            '011',
            '100',
            '101',
            '110',
            '111',
            ]
        if jump in value:
            Bin=Binary[value.index(jump)]
        return Bin
        
        
        
    if line[0]=='@':
        print('address')

    elif line[0]=='(':
        print('label')
        
    else:
        if '=' in line:
            dest=line[:line.index('=')]
            if ';' in line:
                comp=line[line.index('=')+1:line.index(';')]
                jump=line[line.index(';')+1:]
            else:
                comp=line[line.index('=')+1:]
                jump='null'
        else:
            dest='null'
            comp=line[:line.index(';')]
            jump=line[line.index(';')+1:]
        
        print('111'+fcomp(comp.strip())+fdest(dest.strip())+fjump(jump.strip()))


f=open('file.txt','r')
lines=f.readlines()
lineno=0
for line in lines:
    compute(str(line))
    
    lineno+=1
