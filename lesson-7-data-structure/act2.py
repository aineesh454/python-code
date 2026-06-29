from pprint import pprint
student={
    'name': 'Alice',
    'grade': '9th',
    'school': 'Greenwood High',
    'address':{
        'city': 'pune',
        'pin_code': '67684',
        'country': 'india',
    }
}

pprint(student,sort_dicts=False)

student['favColor']= 'blue'

student.pop('favColor')
pprint(student,sort_dicts=False)

_ids = ['1001', '1002', '1003', '1004']
names = ["John", "David", "Tim", "Walter"]

"""
1001 : John
1002 : David
1003 : Tim
1004 : Walter
"""

emp_records = list(zip(_ids, names))
pprint(emp_records)
