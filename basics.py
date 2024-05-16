
def print_s_words():
    st = 'Print only the words that start with s in this sentence SASASA SASA SAS SA'
    for word in st.split():
        if word[0] == 's':
            print(word)

def divide_by_3():
    mylist =[]
    x = range(1,50)
    for n in x:
        if n % 3 == 0:
            mylist.append(n)

    print(mylist)

def better_solutions():
    print([w for w in range(1,51) if w%3 == 0])
    print(list(range(0,10)))

def even_number_of_letters():
    st = 'Print every word in this sentence that has an even number of letters'
    for word in st.split():
        if len(word) % 2 == 0:
            print("Even! {}".format(word))

def buzz_fizz_buzzfizz():
    y = range(0,100)
    for n in y:
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz {}'.format(n))
        elif n % 5 == 0:
            print('Buzz {}'.format(n))
        elif n % 3 == 0:
            print('Fizz {}'.format(n))
        else:
            print(n)

def first_letters():
    st = 'Create a list of the first letters of every word in this string'
    for fl in st.split():
        print(fl[0])

def myfunc(a): 
    st = ""
    for index, lett in enumerate(a):
        if index % 2 == 0:
            st += lett.upper()
        else:
            st += lett.lower()
    return st


def display_list(list):
    print(list)

#a = [0,1,2,3,4,5]
#display_list(a)

def data_type():
    b = input("Choose a number from 0-10: ")
    if b.isdigit():
        c = int(b)
        print(type(c))
        if c <= 10:
            print("thanks")
        else:
            data_type()
    else:
        data_type()

def user_choice():
    choice = "wrong"

    while choice not in ['0','1','2']:
        choice = input("Please chose a number [0,1,2]: ")

        if choice not in input:
            print("Wrong answer!")
        else:
            print("Thanks!")
    return int(choice)

def game_of_choice():
    position = [0,1,2]

    print("Here is the list:")
    print(position)

def lesser_of_two_evens(a,b):
    if(a % 2 == 0 and b % 2 == 0):
        if a > b:
            print(b)
        else:
            print(a)
    else:
        if a > b:
            print(a)
        else:
            print(b) 
                
def animal_crackers(text):
    a = text.find(' ')
    b = text[a+1]

    if(text[0] == b):
        print(True)
    else:
        print(False)

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or n1 + n2 == 20:
        print(True)
    else:
        print(False)
    
def old_macdonald(name):
    new_name = name.capitalize().replace(name[3], name[3].upper(), 1)
    print(new_name)
    
def master_yoda(text):
    m = text.split(" ")
    o = m[::-1]
    n = " ".join(o)

    print(n)
    print(m)
    print(o)

def almost_there(n):
    if (n >= 190 and n <= 210) or (n >=90 and n <= 110):
        print(True)
    else:
        print(False)

def has_33(nums):
    pass