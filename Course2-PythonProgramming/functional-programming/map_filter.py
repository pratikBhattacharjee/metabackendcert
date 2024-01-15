menu = [ 'espresso', 'americano', 'caffelatte', 'cappuccino' ]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

#using the map function to check if the first letter of each item in the menu list is 'c'
map_coffee = map(find_coffee, menu)

print([x for x in map_coffee])
#returns [None, None, 'caffelatte', 'cappuccino']

filter_coffee = filter(find_coffee, menu)
print([x for x in map_coffee])
#returns ['caffelatte', 'cappuccino']
