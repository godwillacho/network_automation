import pickle
#pickle serialisation
friends={'acho':[20,'landon',1321343],'Anah':[25,'Maddrid',1234567]}
with open('friends.dat','wb') as f:
   pickle.dump(friends,f)
#pickle deserialisation
with open ('friends.dat','rb') as f:
   obj=pickle.load(f)
   print(obj)

students ={1234:'anah',1233:'acho'}
with open('students.dat','wb') as f:
    pickle.dump(students,f)



