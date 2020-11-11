person = {
'name': 'Cuong',
'yob': 2002,
'job_title': 'student',
'height': '180cm'
  }
print(person['name'])
yob = person['yob']
print(yob)
del person['height']
for key in person:
    print(key, person[key])
