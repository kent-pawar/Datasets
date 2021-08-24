import json

people_string ='''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "567890",
            "has_license": false
        },

        {
            "name": "Jane Doe",
            "phone": "123456",
            "has_license": null
        }
    ]
}
'''

# Create Python Data Object

data = json.loads(people_string)

#print(data["people"])

for person in data["people"]:
    print(person)
for person in data["people"]:
    print("Name: ",person["name"], "   Phone: ", person["phone"], "License:", person["has_license"])


