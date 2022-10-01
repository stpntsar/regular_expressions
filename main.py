import re
import csv

with open('phonebook_raw.csv', encoding='utf-8', newline='') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r'(\+7|8)\s*\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?\(?(доб\.)?\s?(\d{4})?\)?'
substitution = r'+7(\2)\3-\4-\5 \6 \7'

def main(contacts_list: list):
    new_list = []
    for contact in contacts_list:
        name = ' '.join(contact[:3]).split(' ')
        res = [name[0], name[1], name[2], contact[3], contact[4], re.sub(pattern, substitution, contact[5]),contact[6]]
        new_list.append(res)
    return sorting(new_list)

def sorting(contacts: list):
    for con in contacts:
        for cont in contacts:
            if con[0] == cont[0] and con[1] == con[1]:
                if con[2] == '':
                    con[2] = cont[2]
                if con[3] == '':
                    con[3] = cont[3]
                if con[4] == '':
                    con[4] = cont[4]
                if con[5] == '':
                    con[5] = cont[5]
                if con[6] == '':
                    con[6] = cont[6]
    res_list = []
    for item in contacts:
        if item not in res_list:
            res_list.append(item)
    return res_list



with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(main(contacts_list))