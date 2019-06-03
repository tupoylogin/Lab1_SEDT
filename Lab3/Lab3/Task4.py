import unicodedata

def keysort(s):
    sort_order = {
        'CYRILLIC':1,
        'LATIN':2
        }
    name = unicodedata.name(s.lower()[0],'UNKNOWN')
    first = name.split()[0]
    n = sort_order.get(first,0)

    return n,s


with open("test4.txt","r") as fp:
    lines = fp.readlines()
    words=[]
    for word in lines:
        words.append(word.split())
    flatten = [item for sublist in words for item in sublist]



flatten.sort(key=keysort)

print(flatten)
