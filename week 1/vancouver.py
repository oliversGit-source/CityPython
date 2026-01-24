'''VANCOUVER TEMPERATURES

Complete the code below to show monthly average temperatures in Vancouver, listing temperatures in both celcius and Fahrenheit. Round and pad outputs appropriately

Convert to F using the formula F = (9/5)*C + 32
'''

Mons = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
TempsInC = [4.,5.,7.,9.,13.,15.,17.,18.,15.,10.,6.,4.]
TempsInF = []
for x in TempsInC:
    F = (9 / 5) * x + 32
    TempsInF.append(round(F, 2))

for i in range(len(Mons)):
    print(f'For the month {Mons[i]} Mean temp is: {TempsInF[i]:.2f} Fahrenheit {TempsInC[i]:.2f} Celsius')

templist = []

for x in range(len(Mons)):
    a = [Mons[x], TempsInF[x], TempsInC[x]]
    templist.append(a)
# create header
    header = ["Month", "Temp F", "Temp C"]

# print header
print(f"{header[0]} {header[1]} {header[2]}")
print("-" * 25)
for row in templist:
    print(f"{row[0]:<10} {row[1]:<15} {row[2]:<20}")
