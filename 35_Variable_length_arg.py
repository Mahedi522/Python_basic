# keyword variable length argument

def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)


person(name="Mahedi", age=23, city="Bogura", mob=45555938)