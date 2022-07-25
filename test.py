#num = int(input())
#div = []
#for i in range(num):
#    
#    div += list(i) if num % i == 0 else
#
#print(div)



def leap_year(year):

    this_year = True

    if year % 4:

        this_year = False

    else:

        if year % 100:

            this_year = True

        else:

            if year % 400:

                this_year = False
            
            else:

                this_year = True

    if this_year:

        result = f'{year}은 윤년입니다.'

    else:

        result = f'{year}은 윤년이 아닙니다'

    return result


print(leap_year(2021))
print(leap_year(2020))