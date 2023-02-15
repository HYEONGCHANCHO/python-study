#비교 <,>,<=,>=
#파이썬에서는 비교 연산자 <,>,<=,>= 등을 set()과 함께 사용할 수 있으며,이를 통해 집합이 서브셋인지 슈퍼셋인지, 또는 다른 세트와 동일한지를 확인할 수 있다. 집합 내부에 있는 항목에 따라 True 또는 False를 반환한다.
days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
days2 = {"Monday", "Tuesday"}
days3 = {"Monday", "Tuesday", "Friday"}

print('days1>days2:',days1>days2)
print('days1.issuperset(days2):',days1.issuperset(days2))

print('days1.issubset(days2):',days1.issubset(days2))
print('days2.issubset(days1):',days2.issubset(days1))
print('days1<days2:',days1<days2)
print('days1==days2:',days1==days2)
