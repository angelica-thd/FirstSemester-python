import sys

b= open(sys.argv[1], 'r')
brn=b.read()
b.close()

brn_ps=0
m=[0]
m_ps=0

while brn_ps<len(brn):
    if brn[brn_ps]=="+":
        m[m_ps]+=1
        #maximum value of a cell=1byte
        if m[m_ps]>=255:
            m[m_ps]=0
    elif brn[brn_ps]=="-":
        m[m_ps]-=1
        if m[m_ps]<=-1:
            m[m_ps]=255
    elif brn[brn_ps]=="[":
        if m[m_ps]==0:
             openbrckt=0
             brn_ps+=1
             while brn_ps<len(brn):
                 if brn[brn_ps]=="]" and openbrckt==0:
                     break
                 elif brn[brn_ps]=="[":
                     openbrckt+=1
                 elif brn[brn_ps]=="]":
                     openbrckt-=1
                 brn_ps+=1
    elif brn[brn_ps]=="]":
        if m[m_ps]!=0:
            closebrckt=0
            brn_ps-=1
            while brn_ps>=0:
                if brn[brn_ps]=="[" and closebrckt==0:
                    break
                elif brn[brn_ps]=="]":
                    closebrckt+=1
                elif brn[brn_ps]=="[":
                    closebrckt-=1
                brn_ps-=1
    elif brn[brn_ps]==">":
        m_ps +=1
        if len(m)<=m_ps:
            m.append(0)
    elif brn[brn_ps]=="<":
        m_ps -=1
        if m_ps<0:
            print("Error! Brainfuck doesn't understand this...")
            sys.exit(0)
    elif brn[brn_ps]==",":
        x=input("Give me an input:\n")
        m[m_ps]=ord(x[0])
    elif brn[brn_ps]==".":
        print(chr(m[m_ps]), end="")
    brn_ps +=1
