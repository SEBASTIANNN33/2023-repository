print(2*2*2*2*2*2*2*2*2*2)

print(2**10)

for promenna in (1, 2, 3, 4, 5):
    print (promenna)

print("a ted range:")


for promenna in range(0, 5) :
    print(promenna)

zaklad = 2

for x in range(10):
    zaklad = zaklad * 2

print(zaklad)

soucet = 0

for cislo in range(1, 101):
    soucet = soucet + cislo
 
print(soucet)

soucet = 0
for cislo in range(1,51):
    prvni = cislo
    druhe = 101 - cislo
    celkem_pricteme = prvni + druhe
    soucer = soucet + celkem_pricteme
