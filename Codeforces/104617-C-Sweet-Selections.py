flavors = len(input().split())
drizzles = len(input().split())
toppings = len(input().split())

print((int) (flavors*(flavors-1)/2+flavors)*drizzles*toppings)