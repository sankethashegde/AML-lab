#x={'Tom':'tom@gmail.com','Bill':'bil@microsoft.com'}
#print(x['Bill'])
#x['Tomy']='mit@ua.edu'
#print(x)

#for name in x:
  #print(name)

#for email in x.values():
 # print(email)

#for name in x.items():
 # print (name)


#for name,email in x.items():
 # print(name)
  #print(email)


"""x=('tom','michel','tom@gmail.com')
fname,lname,email=x
print(lname)"""


"""x=('tom','michel','tom@gmail.com','ca')
fname,lname,email,cname=x"""


"""sales_record={
    'price':3.24,
    'num_items':4,
    'person':'tom',
    'email':'tom@gmail.com'
}
sales_statement='{} bought {} item(s) at price of INR {} each for total of INR {}'
print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']
                        ))"""



"""import datetime  as dt
import time as tm
print(tm.time())
from datetime import date
from datetime import time
from datetime import datetime
today=date.today()
print('today date is',today)
dtnow=dt.datetime.fromtimestamp(tm.time())
print(dtnow)
print(dtnow.year,dtnow.month,dtnow.day,dtnow.hour,dtnow.minute,dtnow.second)
delta=dt.timedelta(days=120)
today=dt.date.today()
print(today-delta)
today>today-delta"""




"""class Person:
    institute = 'MSIS'

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name('sanketha')
person.set_location('karkala')

print('{} lives in {} and studies in the institute {}'.format(
    person.name,
    person.location,
    person.institute
))

"""


"""x={1,'x',2,'y',(1,2,3),'hello'}
print(type(x))

y=(1,2,3)
type(y)

y={'one','x',2,'y',3}
z={1,'x','two','y','a'}
print(y,z)

y.add(4)
z.add('a')
print(y,z)"""




""""store1=[10.00,11.00,12.34,5.22]
store2=[18.00,10.00,12.34,5.22]
store3=[10.40,11.60,11.34,3.22]
cheapest=map(min,store1,store2,store3)
costly=map(max,store1,store2,store3)
print(cheapest)

for item in cheapest:
  print(item)

for item in costly:
  print(item)"""






"""def calculatesquare(n):
  return n*n
Numbers =(1,2,3,4)
result=map(calculatesquare,Numbers)
print(result)

res=list(result)
print(res)

numbers=(1,2,3,4)
result =map(lambda x:x*x,numbers)
print(result)

num1=[4,5,6]
num2=[5,6,7]
result =map(lambda n1,n2:n1*n2,num1,num2)
print(list(result))"""