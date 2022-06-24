import requests
from requests.api import request

print("wait for loading")
print("your internet connection:")

def test(mstr):
        res = requests.get(mstr)
        if res.status_code == 200:
        
            print(f'{"connected"}\n')
        else:
            print(f'{"not connected"}\n')
    
 
if __name__ == '__main__':
    print(test(mstr='http://www.ya.ru'))
