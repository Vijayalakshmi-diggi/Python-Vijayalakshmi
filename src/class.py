class goa:
    name="" 
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("enjoy in beach")
ramesh=goa()
suresh=goa()
suresh.name="suresh"
ramesh.name="ramesh"
suresh.drink="no"
ramesh.drink="yes"
print(suresh.name)
print("drinks",suresh.drink)
suresh.beach()
print(ramesh.name)
print("drinks",ramesh.drink)
ramesh.party()
ramesh.beach()