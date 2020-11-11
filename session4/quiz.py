import pyexcel
quizzes = pyexcel.get_records(file_name='quizzes1.xls')
# print(quizzes['question'])
count = 0
for i in range(len(quizzes['choices'])):
    print(f'{i+1}: {quizzes["choices"][i]}')
    answer = int(input('enter answer'))
    if answer == quizzes['answer']:
        print('correct')
        count = count +1
    else:
        print('incorrect')
print(score = (count*100)/ len(quizzes))
