#이론
person= {"이름": "홍길동", "나이": 25}
print(person["이름"])
print(person["나이"])

print(person.keys())
print(person.values())

#
dic = {'이관훈': 25, '홍길동': 30}
#print("업데이트 이전의 홍길동 나이:", dic['홍길동'])

dic['홍길동'] = 31
#print("업데이트 이후의 홍길동 나이: ", dic['홍길동'])

dic.keys()
dic.values()

#연습문제 8번
dic = {'apple': 3, 'banana': 5, 'cherry': 2}
print(dic['banana'])
