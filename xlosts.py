import requests
import random
import string

a = 200

def id_generator(size=5, chars=string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
num = id_generator()

r = ('https://soundcloud.com/jahseh-onfroy/xxxtentacion-feat-rza-ice/s-'+num)
response = requests.get('https://soundcloud.com/jahseh-onfroy/xxxtentacion-feat-rza-ice/s-'+num)
m = response.status_code

while(m!=a):
     print('Not found')

else:
     print('Found:  '+r)
        


    



