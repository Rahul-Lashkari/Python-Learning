letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Rahul"

print(letter.format(country, name))
print(f"Hey my name is {name} and I'm from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I'm from {{country}}")
price = 49.099
txt = f"For only {price:.2f} dollars!"
print(txt)
print(txt.format())
print(type(f"{2*30}"))