 

#import request
#import json 
#a=input('URL:')
def task(finp,fout):
    d={}
    with open(finp,"r") as fi:
        for line in fi:
            for a in line:
                if a != "\n":
                    if d.get(a) is None:
                        d[a]=1
                    else:
                        d[a]=d[a]+1
    with open(fout,"w") as fo:
        for k,v in d.items():
            data = {'people':[{k':' v, }]}
            print(k,":",v,file=fo)
        
task("111.txt","222.txt")

#V= ('{"one": 1, "two": 2, "three": 3}')
#json_obj = json.loads(V) 
#with open('data.json', 'w') as f:
#    json.dump(json_obj, f)


def task(finp,fout):
    d={}
    with open(finp,"r", encoding="utf8") as fi:
        for line in fi:
            for a in line:
                if a != "\n":
                    if d.get(a) is None:
                        d[a]=1
                    else:
                        d[a]=d[a]+1
    with open(fout, 'w', encoding="utf8") as fo:
        for k,v in d.items():
            json.dump(k,v,file=fo)
task("111.txt","222.json")
#json_obj = json.loads(V) 
#with open('data.json', 'w', encoding="utf8") as f:
#    (json_obj, f)