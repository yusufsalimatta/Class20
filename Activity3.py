weather=(1,0,0,0,1,1,0)
Sunny=0
Rainy=0
for i in range(0,7):
    if (weather[i]==1):
        Sunny+=1
    else:
        Rainy+=1

if Sunny>Rainy:
    print("Good Weather")
else:
    print("Bad Weather")