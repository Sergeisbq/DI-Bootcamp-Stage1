import json

sampleJson = '''{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}'''


some_str = json.loads(sampleJson)
print(some_str['company']['employee']['payable']['salary'])

some_str['company']['employee']['payable']['salary'] += 700
print(some_str['company']['employee']['payable']['salary'])

some_str['company']['employee']['birth_date'] = '12/12/2021'
print(some_str)

sampleJson_new = json.dumps(some_str, indent = 2, sort_keys=True)
print (sampleJson_new)

with open("ExXP.json",'w') as file:
    json.dump(some_str, file, indent = 2)