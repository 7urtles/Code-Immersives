name = "Charles"
job_title = "Student"
age = 29

# Concatenation
print("\n\n\t [String Concatenation]\n")
solution1 = name + " : " + job_title
print(solution1)
print("-----------------------------------------------")

# Appending
print("\n\n\t [String Appending]\n")
joined_heading = name
joined_heading += job_title
print(joined_heading)
print("-----------------------------------------------")


# Escape Sequences
    # \n -> New Line
    # \t -> HORIZONTAL tab
    # \v -> VERTICAL tab
print("\n\n\t [Escape Sequences]\n")
sentence = name + ", \v is the greatest...\t of all time."
print(sentence)
print("-----------------------------------------------")


# Argument by Position
print("\n\n\t [String arguments by position]\n")
solution4 = "This is a {}".format('string')
print("Solution4: {0}".format(solution4))
print("-----------------------------------------------")


# Argument by Name
print("\n\n\t [String arguments by name]\n")
solution5 = "My name is {name}, my favorite number is {number} and I am working as a {job}".format(number = 22, job = job_title, name = name)
print(solution5)
print("-----------------------------------------------")


# F-Strings
print("\n\n\t [Working with f'strings]\n")
solution6 = f"Name: {name} \nAge: {age} \nJob Title: {job_title}"
print(solution6)
print("-----------------------------------------------")


# Some String Methods
    # Method #1: .captialize()
job_title = "student"
print("\n\n\t [String Methods]\n")
solution7 = f"\'{job_title}\' \t.capitalize(): \t{job_title.capitalize()}"
print(solution7)

    # Method #2: .upper()
job_title = "Student"
solution7 = f"\'{job_title}\' \t.upper() \t{job_title.upper()}"
print(solution7)

    # Method #3: .lower()
job_title = "Student"
solution7 = f"\'{job_title}\' \t.lower() \t{job_title.lower()}"
print(solution7)

    # Method #4: .swapcase()
job_title = "StUdEnT"
solution7 = f"\'{job_title}\' \t.swapcase() \t{job_title.swapcase()}"
print(solution7)

    # Method #5: .title()
job_title = "a student"
solution7 = f"\'{job_title}\' \t.title() \t{job_title.title()}"
print(solution7)

    # Method #6: .len()
job_title = "a student"
solution7 = f"\'{job_title}\' \t.len()\t \t{len(job_title)}"
print(solution7)

    # Method #7: .type()
job_title = "a student"
solution7 = f"\'{job_title}\' \t.type()\t \t{type(job_title)}"
print(solution7)

    # Method #7: .replaxe(x,y)
abc = "abcdefgh"
solution7 = f"\'{abc}\' \t.replace(a,1) \t{abc.replace('a','1')}"
print(solution7)

    # Method #7: .count()
a_list = [1, 2, 3, 4]
number = 1
solution7 = f"[1, 2, 3, 4] \t.count(2) \tAppears: {a_list.count(number)} time"
print(solution7)

print("-----------------------------------------------")
