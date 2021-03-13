import random
import string
import timeit

def Q01():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    age = 100 - age + 2021
    print(name)
    print(age)

def Q02():
    number = int(input("Enter number: "))
    if (number%2)==0:
        print(number," is even")
    else:
        print(number," is odd")

def Q03():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for x in a:
        if x < 5:
            print(x, end=" ")
def Q04():
    number = int(input("Enter number: "))
    for x in range(1,number+1):
        if number%x==0:
            print(x, end=" ")

def Q05():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for x in a:
        for y in b:
            if x==y:
                c.append(x)
    print(c)

def Q06():
    rev_str = ""
    user_input=input("Enter string: ")
    for x in range(len(user_input)-1,-1,-1):
        rev_str+=user_input[x]
    if user_input==rev_str:
        print(user_input," has palindrome")
    else:
        print(user_input," not have palindrome")

def Q07():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = []
    for x in a:
        if x%2==0:
            b.append(x)
    print(b)

def Q08():
    i=1
    while i==1:
        print("1:Rock 2:Paper 3: Scissor")
        player_1=int(input("Player 1: "))
        while player_1<1 or player_1>3:
            print("Enter again!!!")
            player_1 = int(input("Player 1: "))

        player_2=int(input("Player 2: "))
        while player_2<1 or player_2>3:
            print("Enter again!!!")
            player_2 = int(input("Player 2: "))

        if player_1==player_2:
            print("Draw")
        elif player_1==1:
            if player_2==2:
                print("Player 2 Win")
            else:
                print("Player 1 Win")
        elif player_1==2:
            if player_2==1:
                print("Player 1 Win")
            else:
                print("Player 2 Win")
        elif player_1==3:
            if player_2==2:
                print("Player 1 Win")
            else:
                print("Player 2 Win")

        i = int(input("Start new game? 0:No 1:Yes "))

def Q09():
    ran_number=random.randint(1,9)
    user_guess=int(input("Guess the number between 1-9: "))
    if user_guess>ran_number:
        print("guess is high")
    elif user_guess<ran_number:
        print("guess is low")
    else:
        print("guess is right")

def Q10():
    user_input=int(input("Enter number: "))
    a=0
    for x in range(1,user_input+1):
        if user_input%x==0:
            a+=1
    if a<=2:
        print(user_input ," is prime number")
    else:
        print(user_input ," is not prime number")

def Q11():
    a = [5, 10, 15, 20, 25]
    first_last_list(a)

def first_last_list(a_list):
    print(a_list[0])
    print(a_list[len(a_list)-1])

def Q12():
    num=int(input("Enter n: "))
    for x in range(num):
        print(fibonnacci(x), end=" ")

def fibonnacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonnacci(n-1)+ fibonnacci(n-2)

def Q13():
    a=[1,2,3,4,5,6,5,4,3,2,1,1,2,3]
    remove_duplicate(a)

def remove_duplicate(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    print(b)

def Q14():
    user_string=input("Enter a long string: ")
    backward_str(user_string)

def backward_str(a):
    str_list = a.split()
    for x in range(len(str_list)-1,-1,-1):
        print(str_list[x], end=" ")

def Q15():
    start=timeit.default_timer()
    print(random_password_generator())
    stop=timeit.default_timer()
    print("Runtime: ", stop - start)

def random_password_generator():
    characters=string.ascii_letters+string.digits+string.punctuation
    select_character=random.sample(characters,random.randint(8,15))
    password="".join(select_character)
    return password


Q01()
Q02()
Q03()
Q04()
Q05()
Q06()
Q07()
Q08()
Q09()
Q10()
Q11()
Q12()
Q13()
Q14()
Q15()