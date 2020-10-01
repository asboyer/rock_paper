from random import randint
r = 0
p = 0
s = 0
for i in range(1000):
    chosen = randint(1,3)
    if chosen == 1:
        chosen = "rock"
        r = r + 1
    if chosen == 2:
        chosen = "paper"
        p = p + 1
    if chosen == 3:
        chosen = "scissors"
        s = s + 1
    print(chosen)
print("\n# of rocks: " + str(r))
print("# of paper " + str(p))
print("# of scissors " + str(s))
