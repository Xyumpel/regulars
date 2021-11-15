import re
from pprint import pprint
import csv
with open("phonebook_raw.csv", encoding = 'utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pattern1 = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
new_pattern1 = r'\1\3\10\4\6\9\7\8'
new_contact_list1 = list()
for name in contacts_list:
  as_string1 = ','.join(name)
  formatted_card1 = re.sub(pattern1, new_pattern1, as_string1)
  as_list1 = formatted_card1.split(',')
  new_contact_list1.append(as_list1)

pattern2 = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
new_pattern2 = r'+7(\4)\8-\11-\14\15\17\18\19\20'
new_contact_list2= list()
for number in new_contact_list1:
  as_string2 = ','.join(number)
  formatted_card = re.sub(pattern2, new_pattern2, as_string2)
  card_as_list = formatted_card.split(',')
  new_contact_list2.append(card_as_list)

for i in new_contact_list2:
  for j in new_contact_list2:
    if i[0] == j[0] and i[1] == j[1] and i is not j:
      if i[2] == '':
        i[2] = j[2]
      if i[3] == '':
        i[3] = j[3]
      if i[4] == '':
         i[4] = j[4]
      if i[5] == '':
         i[5] = j[5]
      if i[6] == '':
         i[6] = j[6]
contacts_list_updated = list()
for duplicates in new_contact_list2:
  if duplicates not in contacts_list_updated:
    contacts_list_updated.append(duplicates)



print(contacts_list_updated)
with open("phonebook.csv", "w", encoding = 'utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list_updated)