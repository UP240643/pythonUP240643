# Here we have a person dictionary. Feel free to modify it
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    if len(skills) > 2:
        middle_skill = skills[len(skills) // 2]
        print(f"Middle skill: {middle_skill}")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'Python' in skills:
        print("The person has Python skill.")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
else:
        print('Unknown title')

#  * If the person is married and if he lives in Finland, print the information in the following format:
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")