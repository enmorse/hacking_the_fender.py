import csv
import json

compromised_users = []

with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)

    for password_row in password_csv:
        # print(password_row['Username'])
        compromised_users.append(password_row['Username'])
        # print(compromised_users)


with open('compromised_users.txt', 'w') as compromised_users_file:
    for compromised_user in compromised_users:
        compromised_users_file.write(compromised_user)


with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
    json.dump(boss_message_dict, boss_message)


with open('passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = """
    YOU GOT
    HACKED
    - SLASH
    NULL
    """
    new_passwords_obj.write(slash_null_sig)
