num_list = [y for y in range(100) if y % 2 == 0 and y % 5 == 0]
print(num_list) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj) # 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']


obj = [ i + 3 for i in range(10)]
print(obj) # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

obj = list(range(3,13))
print(obj) # [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]