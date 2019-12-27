char={'A':'ACHIEVER','B':'BOLD','C':'CHEERFUL','D':'DANCER','E':'ENERGETIC','F':'FANTASTIC','G':'GRACEFUL','H':'HELPFUL','I':'IMMORTAL','J':'JOYFUL','K':'KIND','L':'LUCKY','M':'MASTER','N':'NEATEST','O':'OPEN-MINDED','P':'PHILOSOPHER','Q':'QUICKER','R':'READABLE','S':'SPECIALIST','T':'TRUSTFUL','U':'UNBEATABLE','V':'VERSATILE','W':'WONDERFUL','X':'XIEXIE','Y':'YOUNG','Z':'ZERO'}
name=input("Enter your name:")
name=name.upper()
word=name.split()
for item in word:
    for val in item:
        print(val,"=",char[val])
    else:
        print("Thank you")
