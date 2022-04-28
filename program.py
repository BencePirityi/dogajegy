maxpont = int(input("Adja meg a max pontot: "))
pont = int(input("Adja meg az elért pontot: "))

szazalek = int((pont / maxpont) * 100)

if szazalek >= 90:
    jegy = 5
elif szazalek >= 80:
    jegy = 4
elif szazalek >= 65:
    jegy = 3
elif szazalek >= 50:
    jegy = 2
else:
    jegy = 1



print(f"{szazalek}%-ot értél el, a jegyed: {jegy}")