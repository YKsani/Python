# Считайте число N и сформируйте список из N элементов, заполнив его числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Input format
# В первой строке одно целое число N. Во второй строке целые числа через пробел, указанные позиции.
# Output format
# Одно число, произведение элементов на указанных позициях.

num=int(input())
positions= [int(i) for i in input().split()]
num_list=[]
prod=1
for i in range(-num,num+1):
    num_list.append(i)
for num in positions:
    prod*=num_list[num]
print(prod)