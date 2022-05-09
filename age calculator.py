def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age,"Years Old")
y=int(input("Enter Your Birth Year : "))
m=int(input("Enter Your Birth Month : "))
d=int(input("Enter Your Date of Birth : "))
ageCalculator(y,m,d)
