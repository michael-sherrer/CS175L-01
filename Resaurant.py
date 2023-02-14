#CS175L
#Michael Sherrer
#restaurant while loop
restart='yes'
while restart=='yes':
    vegetarian=False
    vegan=False
    gluten_free=False
    response1=input('Is anyone in your party a vegetarian? ')
    if response1=='yes':
        vegetarian=True
    response2=input('Is anyone anyone in your party a vegan? ')
    if response2=='yes':
        vegan=True
    response3=input('Is anyone in your party gluten free? ')
    if response3=='yes':
        gluten_free=True
    print('Here are your restaurant choices: ')
    print('The Chef\'s Kitchen')
    print('The Corner cafe')
    if vegan==False:
        print('Main Street Pizza')
    if vegan==False and gluten_free==False:
        print('Mama\'s Fine Italian')
    if vegetarian==False and vegan==False and gluten_free==False:
        print('Joe\'s Gourmet Burgers')
    restart=input('Would you like to do another restaurant search(type yes or no)? ')
