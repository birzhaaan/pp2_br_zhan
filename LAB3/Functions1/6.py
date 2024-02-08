def reverseddd(soz):
    words = soz.split()
    keri_soz = ' '.join(reversed(words))
    return keri_soz

bir_soilem = input("ENGIZ: ")
answer = reverseddd(bir_soilem)
print(answer)