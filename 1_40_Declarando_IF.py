is_male = False
#is_male = False #True
He_Is_Tall = False

# or  , and

if is_male:
    print('Macho')
else:
    print('I Dont Think So')

if is_male and He_Is_Tall:
    print("Approved")
else:
    print('Not This time')
if is_male and not He_Is_Tall:
    print('Not Phisical Condition')

elif not He_Is_Tall and not is_male:
    print('Not Approved')
