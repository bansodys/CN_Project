import os
os.system("git init")
os.system("git status")
fl=os.listdir()
# print(fl)
os.system("git add -A")
os.system('''git commit -m "added codes" ''')
# os.system('''git remote add origin https://github.com/bansodys/CN_Project.git''')
os.system('''git push -u origin master''')


