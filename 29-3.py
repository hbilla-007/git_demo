def myfunc():
    choice=" "
    within_range=False
    while choice.isdigit()==False or within_range==False:
        choice=input('enter number')
        if choice.isdigit()==False:
            print('please check the number')
        if choice.isdigit()==True:
            if int(choice) in range(0,20):
                within_range=True
            else:
                within_range=False
        else:
            pass
    return int(choice)
print(myfunc())