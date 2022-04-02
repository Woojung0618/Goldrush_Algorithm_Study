from inspect import stack
import sys

N,P=map(int,sys.stdin.readline().split())
stack1=[]
stack2=[]
stack3=[]
stack4=[]
stack5=[]
stack6=[]
count=0
for i in range(N):
    line,flat=map(int,sys.stdin.readline().split())
    if line==1:
        if stack1:
            if flat==stack1[-1]:
                continue
            elif flat>stack1[-1]:
                count+=1
                stack1.append(flat)
            else:
                i=len(stack1)
                while i>=0:
                    if len(stack1)==0:
                        stack1.append(flat)
                        count+=1
                        break
                    if flat>stack1[i-1]:
                        count+=1
                        stack1.append(flat)
                        break
                    elif flat==stack1[i-1]:
                        break
                    else:
                        stack1.pop()
                        count+=1
                    i-=1
        else:
            stack1.append(flat)
            count+=1
    elif line==2:
        if stack2:
            if flat==stack2[-1]:
                continue
            elif flat>stack2[-1]:
                count+=1
                stack2.append(flat)
            else:
                i=len(stack2)
                while i>=0:
                    if len(stack2)==0:
                        stack2.append(flat)
                        count+=1
                        break
                    if flat>stack2[i-1]:
                        count+=1
                        stack2.append(flat)
                        break
                    elif flat==stack2[i-1]:
                        break
                    else:
                        stack2.pop()
                        count+=1
                    i-=1
        else:
            stack2.append(flat)
            count+=1
    elif line==3:
        if stack2:
            if flat==stack3[-1]:
                continue
            elif flat>stack3[-1]:
                count+=1
                stack3.append(flat)
            else:
                i=len(stack3)
                while i>=0:
                    if len(stack3)==0:
                        stack3.append(flat)
                        count+=1
                        break
                    if flat>stack3[i-1]:
                        count+=1
                        stack3.append(flat)
                        break
                    elif flat==stack3[i-1]:
                        break
                    else:
                        stack3.pop()
                        count+=1
                    i-=1
        else:
            stack3.append(flat)
            count+=1   
    elif line==4:
        if stack4:
            if flat==stack4[-1]:
                continue
            elif flat>stack4[-1]:
                count+=1
                stack4.append(flat)
            else:
                i=len(stack4)
                while i>=0:
                    if len(stack4)==0:
                        stack4.append(flat)
                        count+=1
                        break
                    if flat>stack4[i-1]:
                        count+=1
                        stack4.append(flat)
                        break
                    elif flat==stack4[i-1]:
                        break
                    else:
                        stack4.pop()
                        count+=1
                    i-=1
        else:
            stack4.append(flat)
            count+=1   
    elif line==5:
        if stack5:
            if flat==stack5[-1]:
                continue
            elif flat>stack5[-1]:
                count+=1
                stack5.append(flat)
            else:
                i=len(stack5)
                while i>=0:
                    if len(stack5)==0:
                        stack5.append(flat)
                        count+=1
                        break
                    if flat>stack5[i-1]:
                        count+=1
                        stack5.append(flat)
                        break
                    elif flat==stack5[i-1]:
                        break
                    else:
                        stack5.pop()
                        count+=1
                    i-=1
        else:
            stack5.append(flat)
            count+=1 
    elif line==6:
        if stack6:
            if flat==stack6[-1]:
                continue
            elif flat>stack6[-1]:
                count+=1
                stack6.append(flat)
            else:
                i=len(stack6)
                while i>=0:
                    if len(stack6)==0:
                        stack6.append(flat)
                        count+=1
                        break
                    if flat>stack6[i-1]:
                        count+=1
                        stack6.append(flat)
                        break
                    elif flat==stack6[i-1]:
                        break
                    else:
                        stack6.pop()
                        count+=1
                    i-=1
        else:
            stack6.append(flat)
            count+=1
print(count)