import json

employee_data = '''
{
    "people":[
    {
       "Name" : "Sonish",
       "Email" : ["sonish@gmail.com"],
       "Martial Status" : "Single"
    },
    {
        "Name" : "Raghu",
        "Email" : ["Raghu@gmail.com"],
        "Martial Status" : "Single"
    }
]
}
'''
print(employee_data)

data = json.loads(employee_data)
print(data)