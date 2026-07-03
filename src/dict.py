#stores key value pairs
library={
    "std_id" :501,
    "book_name":"splash"
    }
print(library)
print(library["std_id"])
#add key 
library["time"]= 12
print(library)
#pop
library.pop("std_id")
print(library)
#keys
print(library.keys())
#values()
print(library.values())
# item()
print(library.items())
#get() it returns non or default value if no item
print(library.get("std_id"))
# in loop it only gives keys
for i in library:
    print(i)
#in loop print only values
for i in library.values():
    print(i)
# in loop print items()
for i in library.items():
    print(i)
# converting dict into set (it wil print only keys so use .items)
print(set(library.items))
