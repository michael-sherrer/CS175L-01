#CS175L
#Michael Sherrer
#restaurant

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
if vegetarian==False and vegan==False and gluten_free==False:
    print('Joe\'s Gourmet Burgers')
    print('Corner Cafe')
    print('Chef\'s Kitchen')
    print('Mama\'s Fine Italian')
    print('Main Street Pizza')
elif vegetarian==True and vegan==False and gluten_free==False:
    print('Mama\'s Fine Italian')
    print('Main Street Pizza')
    print('Corner Cafe')
    print('Chef\'s Kitchen')
elif vegetarian==True and vegan==False and gluten_free==True:
    print('Main Street Pizza')
    print('Corner Cafe')
    print('Chef\'s Kitchen')
elif vegetarian== True and vegan==True and gluten_free==True:
    print('Corner Cafe')
    print('Chef\'s Kitchen')
    

