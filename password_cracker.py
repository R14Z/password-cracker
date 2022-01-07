# info

user = input('User: ')
password = input('(Must be 1 character) Password: ')

# characters

char = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# checks if the index[0] of user is uppercase or lower

if user[0] != user[0].upper():
    print(f'User is {user[0].upper()}{user[1:]}.')
else:
    print(f'User is {user}.')

# create combinations until you find the password

for index in char:
    index + index
    if index == password:
        print('Password found')
        print(f'Password is {index}')
