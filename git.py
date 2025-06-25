#a simple forloop demonstration
laptop_brands = ['HP', 'Dell','Lenovo','Acer', 'Microsoft']

for i in laptop_brands:
    print(i)

user_input = input('What laptop brand?')
laptop_brands.append(user_input)

print(laptop_brands)