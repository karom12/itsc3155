#Dictionaries
dic1 = {"a": 100 , "b": 200, "c": 300}
dic2 = {"a": 300 , "b": 200, "d": 400}
dic3 = dict(dic1)
dic3.update(dic2)
for i, j in dic1.items():
    for k, l in dic2.items():
        if i == k:
            dic3[i] = (j + l)
print(dic3)