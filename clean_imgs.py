import os
import hashlib
from collections import defaultdict

def GetMd5(path):
    hash = hashlib.md5()
    hash.update(open(path, "rb").read())
    return hash.hexdigest()


def get_allmd(path):
    res = []
    for name in os.listdir(path):
        tpath = os.path.join(path, name)
        if os.path.isdir(tpath):
            res.extend(get_allmd(tpath))
        elif os.path.isfile(tpath) and os.path.splitext(tpath)[-1] == ".md":
            res.append(tpath)
    return res

def replaceText(text, else2left):
    for k,v in else2left.items():
        text = text.replace(k, v)
    return text

def deleteElse(else2left):
    for k in else2left:
        os.remove(os.path.join(root, k))

if __name__ == "__main__":
    root = "./imgs"
    file_names = os.listdir(root)
    md52file = defaultdict(list)

    for name in file_names:
        md5 = GetMd5(os.path.join(root, name))
        md52file[md5].append(name)
    else2left = {}

    for k, v in md52file.items():
        for t in v[1:]:
            else2left[t] = v[0]

    for path in get_allmd("./"):
        with open(path, "r", encoding="utf8") as f:
            text = f.read()
        with open(path, "w", encoding="utf8") as f:
            text = replaceText(text, else2left)
            f.write(text)
    
    deleteElse(else2left)


