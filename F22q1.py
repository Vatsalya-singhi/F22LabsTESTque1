import json,urllib.request
url= input("Enter the url:\n")
#url="https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

invest=set([])
try: 
    for i in range(1,len(data)+1):
        #print('Episode '+str(i)+"\n")
        for x in data['Episode '+str(i)]:
            l=x['investors'].replace('and',',')
            l=l.split(',')
            for i in range(len(l)):
                l[i]=l[i].strip('\n').lstrip().rstrip()
            invest=invest.union(l)
    invest.remove('')
    oo = {e:[] for e in invest}
    for i in range(1,len(data)+1):
        for x in data['Episode '+str(i)]:
            sample=x['investors']
            for i in oo:
                if i in sample:
                    oo[i].append(x['product'].lstrip().rstrip().strip('\n'))
    for k in sorted(oo, key=lambda k: len(oo[k]), reverse=True):
        print (str(k)+"  : "+str(oo[k]))
        print("\n")
except (ValueError, KeyError, TypeError):
    print("JSON format error")
