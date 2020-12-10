from datetime import datetime

# 1. Uzdevums
user_name = input("Ievadiet savu vārdu: ")
user_age = input("Ievadiet savu vecumu: ")
user_age = int(user_age)

years_till_100 = 100 - user_age

current_year = datetime.today().year

print(f"Jums, {user_name} pēc {years_till_100} būs 100 gadi.")
print(f"Tas būs {current_year + years_till_100} gadā.")


# 2. Uzdevums
h = input("Ievadiet augstumu: ")
w = input("Ievadiet platumus: ")
z = input("Ievadiet platumu: ")

h = float(h)
w = float(w)
z = float(z)

print(f"Telpas tilpums ir: {h * w * z:.03f}.")


# 3. Uzdevums
c = input("Ievadīt temperatūru pēc Celsija: ")
c = float(c)

f = 32 + c * (9 / 5)

print(f"{c:.02f} grādi Celsija skalā atbilst {f:.02f} grādiem pēd Farenheita.")
