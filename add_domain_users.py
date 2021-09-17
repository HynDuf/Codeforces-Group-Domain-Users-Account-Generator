
"""
Created on Fri Sep 10 14:29:06 2021

@author: HynDuf
"""
import random
import string
from unidecode import unidecode
class Student:
    def __init__(self, name):
        self.name = name
        self.contest = set()
    def generate_id(self):
        id = 0
        for c in self.name:
            id = (id * 317 + ord(c)) % 31731
        self.id = id
    def generate_account(self):
        sep = unidecode(self.name).split(' ')
        self.username = sep[0].lower().replace('-', '_') + '_'
        for i in range(1, len(sep) - 1):
            self.username = self.username + sep[i][0].lower()
        self.username = self.username + sep[-1].lower() + '_' + str(self.id)
        self.password = ''.join(random.choices(
                                string.ascii_uppercase 
                              + string.ascii_lowercase 
                              + string.digits, k=8)) 
    def generate_string(self):
        ret = ""
        for x in self.contest: 
            ret = ret + str(x) + ','
        ret = ret[:-1] + ' | ' + self.username + ' | ' + self.password + ' | ' + self.name
        return ret
        

with open('input.txt', 'r', encoding="utf8") as f:
    lines = f.read().splitlines()
add_contest = set(lines[0].split())
students = {}
for i in range(1, len(lines)):
    if lines[i].isspace() or lines[i] == '':
        continue
    S = Student(lines[i].strip())
    S.generate_id()
    S.generate_account()
    S.contest.update(add_contest)
    students[S.id] = S
with open('output.txt', 'r', encoding="utf8") as f:
    lines = f.read().splitlines()
for x in lines:
    if x.isspace() or x == '':
        continue
    sep = [y.strip() for y in x.split('|')]
    contest = set([y.strip() for y in sep[0].split(',')])
    S = Student(sep[-1].strip())
    S.generate_id()
    S.contest = contest
    S.username = sep[1]
    S.password = sep[2]
    if S.id in students:
        S.contest.update(add_contest)
    students[S.id] = S

with open('output.txt', 'w', encoding="utf8") as f:
    for i in students:
        f.write(students[i].generate_string())
        f.write('\n')

