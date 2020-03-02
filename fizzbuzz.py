# i = 1

# while i < 100:
#     fizzy = ""
#     if i % 3 == 0:
#         fizzy += "Fizz"
#     elif i % 5 == 0:
#         fizzy += "Buzz"
#     else:
#         print(i)
#     i += 1


for num in range(1,200):
    fizzy = ""
    if num % 3 == 0:
        fizzy += "Fizz"
    if num % 5 == 0:
        fizzy += "Buzz"
    if fizzy == "":
        fizzy = num
    print(fizzy)