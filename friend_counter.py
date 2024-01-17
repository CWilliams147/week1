def countFriends(person):
    if 'friends' in person:
        return len(person['friends'])
    else:
        return 0

ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

ramit_friends_count = countFriends(ramit)
print(f"Ramit has {ramit_friends_count} friend(s).")
