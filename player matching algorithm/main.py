import time
import asyncio

categories=['SDE-1','SDE-2','SDE-3','React Developer','Django Developer']
users=[]
timeLimit=30

class User():
    uId=1
    def __init__(self,name,category,isInterviewer=False) -> None:
        self.name=name
        self.category=category
        self.isInterviewer=isInterviewer
        self.userId=User.uId
        User.uId+=1

    async def match(self):
        print("Hello World")
        return
        users.append(self)
        # Instead of searching in the list we will be using the searching the DB in real world scenario
        matchedUser=filter(lambda x:x.category==self.category and x.isInterviewer !=self.isInterviewer,users)
        matchedUser=list(matchedUser)
        pair=[]
        if len(matchedUser) !=0:
            pair=[matchedUser[0],self]
            for user in pair:
                i=users.find(user)
                users.pop(i)

        else:
            await asyncio.sleep(timeLimit)
            if self in users:
                print("Sorry try again to match the correct user")
            else:
                return    

    def __str__(self) -> str:
        return f"{self.userId} - {self.name}"

u1=User("Adnan Ali",categories[0])
u1match=User("Arish Ansari",categories[0],True)

u2=User("Mithil Joshi",categories[1])
u2match=User("Ayush Agarwal",categories[1],True)

u3=User("Adnan Ali",categories[2])
u3match=User("Vikas Thakur",categories[1],True)

u4=User("Faraz Malik",categories[3])
u4match=User("Vinay Pant",categories[1],True)

u5=User("n1",categories[0])
u5match=User("n2",categories[1],True)

u6=User("n3",categories[0])
u6match=User("n4",categories[1],True)

u7=User("n5",categories[1])

asyncio.create_task(u1.match())
time.sleep(1)

asyncio.create_task(u2.match())
time.sleep(0.5)

asyncio.create_task(u1match.match())