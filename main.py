#3.N students take a apples and distribute then among each students evenly
#The remaining parts remain in the basket
#how many apples will each single student got?
#how many apples will remain in the basket?the program read the numbers K and N?


N=int(input("enter the number of students in class: "))
k=int(input("enter the number of applkes:"))

apples_got=(k//N)

remaining_apples=(k%N)
print(f"Each student got {apples_get}  ")
print(f"The remaining apples are{remaining_apples}  ")
