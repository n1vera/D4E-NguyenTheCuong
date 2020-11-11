import pyexcel
quizzes ={

'question': 'con cho co may chan ?',
'answer': 4,
'choices':[
'2 chan',
'3 chan',
'1 chan',
'4 chan'
]
},
{
'question': 'con cho co may chan ?',
'answer': 4,
'choices':[
'2 chan',
'3 chan',
'1 chan',
'4 chan'
]
}

pyexcel.save_as(records=quizzes, dest_file_name='quizzes1.xls')
