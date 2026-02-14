score = 88

if score > 100:
    print("verify your score")
    exit()
    
if score >= 90:
    grade = 'A'
elif score >= 80: #and score <90:
    grade = 'B'
elif score >= 70: #and score <80:
    grade = 'C'
elif score >= 60: #and score <70:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)