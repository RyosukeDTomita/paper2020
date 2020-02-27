
# coding: utf-8

# In[ ]:

import requests
import sys
import os
def main():
    url = "https://notify-api.line.me/api/notify"
    token = 'jkn9gOyqaPKn09aseKhkieN1CPyk5niDyeXcqmCACcw'
    headers = {"Authorization" : "Bearer "+ token}

    args = sys.argv
    if args[0] == 1:
        message =  'MISSION accomplished'
    else :
        message = 'Congraturation!'
    payload = {"message" :  message}
    end  = os.path.join('/home/tomita/model/'+'end.jpg' )
    files = {"imageFile": open(end, "rb")}

    r = requests.post(url ,headers = headers ,params=payload, files=files)

if __name__ == '__main__':
    main()


# In[ ]:

#jupyter nbconvert --to notebook --execute notify.ipynb \
#    --output notify.ipynb --ExecutePreprocessor.timeout=2678400      --allow-errors --debug

