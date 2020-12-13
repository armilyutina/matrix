import random as random
import time


def main():
	text = input('Ввести параметры матрицы вручную? Y/N  ' )
	isOpen = True  if text == 'Y' else False	

	if(isOpen):
		data = generateData()
		print()
		return handler(data)
	else:
	 	f = open('data.txt','r')
	 	array = [[int(elem) for elem in row.split()] for row in f]
	 	for i in array:
	 		print(*i)
	 	return handler(array)
	 	
	 	


def generateData():
	M = int(input('Enter M '))
	N = int(input('Enter N '))
	arr = [[0 for i in range(N+2)] for j in range(M+2)]

	for j in range(1, M+1):
		for i in range(1, N+1):
			arr[j][i] = round(random.random())

	for i in arr:
		print(*i)

	return arr




def handler(arr):
  value = 0
  for i in range(1, len(arr)-1):
    for j in range(1, len(arr[i])-1):

      value = sum([arr[i+1][j], arr[i+1][j+1], arr[i][j+1], 
      				arr[i-1][j], arr[i-1][j-1], arr[i][j-1], 
      				arr[i-1][j+1], arr[i+1][j-1]])
      
      if(arr[i][j] == 0 and value == 3):
        arr[i][j] = 1

      if(arr[i][j] == 1 and (value > 3 or value < 2)):
        arr[i][j] = 0
    
      value = 0

  return arr


print()
result = main()

for i in result:
	print(*i)
print()


def foo(data):
    res = handler(data)
    for i in result:
        print(*i)
    print()
    time.sleep(1)
    foo(res)

foo(result)