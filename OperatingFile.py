with open('temp', 'w') as mf:
    name = "NAME"
    phone = "PHONE"
    mf.write(f'{name:10} ==> {phone:10}\n')
    i = 0
    while i <= 2 :
        name = input("enter Name :")
        phone = input("enter Phone :")
        mf.write(f'{name:10} ==> {phone:10}\n')
        i= i + 1
    mf.close()
