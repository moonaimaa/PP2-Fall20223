import json 

with open('sample-data.json', 'r') as f:
    a=json.load(f)

# for i in range(len(a['imdata'])):
#     print(a['imdata'][i]['l1PhysIf']['attributes']['dn'], a['imdata'][i]['l1PhysIf']['attributes']['descr'], 
#         a['imdata'][i]['l1PhysIf']['attributes']['mtu'], a['imdata'][i]['l1PhysIf']['attributes']['speed'])


print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU
-------------------------------------------------- --------------------  ------  ------""")

for i in a["imdata"]:
    print("{DN:50}{Speed:>30}{MTU:>6}".format(DN = i["l1PhysIf"]["attributes"]["dn"], Speed = i["l1PhysIf"]["attributes"]["speed"], MTU = i["l1PhysIf"]["attributes"]["mtu"]))