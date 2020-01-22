drinks ={
    'martini' : {'vodka', 'vermouth'},
    'black russian' : {'vodka', 'kahlua'},
    'white russian' : {'cream','kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

brs= drinks['black russian']
wrs=drinks['white russian']

print(brs)
print(wrs)
print(brs & wrs)