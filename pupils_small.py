import time

class Pupil():
    def __init__(self, info_pupil):
        info = info_pupil.split(" ")
        self.name = self.info[1]
        self.surname = self.info[0]
        self.mark = int(self.info[2])

pupil = []

with open("pupils.txt", "r", encoding= "utf-8") as file:
    for line in file.readlines():
        pupils.append(
            Pupil (line)
            )

for pupil in pupils:
    print(pupil.name, pupil.surname, pupil.mark)

mid = 0

for pupil in pupils:
    if pupil.mark == 5:
        print(pupil.surname)

print(f"середня оцінка: {mid / len(pupils)}")
print(time())