import json as json

readfile=json.loads(open("json/songs.json").read())

def addSong(title):
    if title not in readfile:
        readfile[title]={"tags":[],"artist":None,"plays":0}
        return True
    return False

def addTags(title, tags=[]):
    if title not in readfile:
        addSong(title)
    if tags==[]:
         tags=[x.strip() for x in input().split(",")]
    for x in tags:
        if x not in readfile[title]["tags"]:
            readfile[title]["tags"].append(x)
