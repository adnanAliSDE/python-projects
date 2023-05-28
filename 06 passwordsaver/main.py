# class Provider:
#     def __init__(self,name,userId,password):
#         self.name=name
#         self.userId=userId
#         self.password=password

# provider=input("Enter your authentication provider: ")
# userId=input("Enter your username: ")
# password=input("Enter your password: ")
# p1=Provider(provider,userId,password)
# print(p1.password)
data=[]
with open('data.csv') as f:
    lines=f.readlines()
    for index,line in enumerate(lines):
        if lines.index(line)!=len(lines)-1:
            line=line.strip('\n')
        data.append(line)