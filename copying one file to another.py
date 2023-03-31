#opeaning file 'txt1.txt' in read mode
f1=open('txt1','r')

'''opeaning file 'txt2.txt' in write mode
    This mode will rewrite on file 'txt2.txt' if already exist and
    if file 'txt2.txt' was not created before then it will be created.'''
f2=open('txt2','w')


'''Here we are fetching data from file 'txt1.txt' and
    writing one by one to f2 i.e. file 'txt2.txt' '''
for data in f1:
    f2.write(data)


f2.write('\n\n\t_ _ _ _ _ THSI IS COPIED FILE _ _ _ _ _\n')