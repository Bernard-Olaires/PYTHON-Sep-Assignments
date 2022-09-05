# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists

resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}


print(users[0])

print("------------------------") #gives space to output

print(users[0]["last"])
print(users[2]["first"])


print(resume_data["skills"][1])

print("------------------------") #gives space to output

print(resume_data["skills"][1])
print(users[2]["first"])

print("------------------------") #gives space to output

resumes = [
    {
    "skills" : ["front-end", "back-end", "database"],
    "languages" : ["Python", "JavaScrip"],
    "hobbies" : ["rock climbing", "knitting"]
    },
    {
    "skills" : ["front-end"],
    "languages" : ["HTML", "CSS"],
    "hobbies" : ["video games", "gym"]
    }
]

print(resumes)
print("------------------------") #gives space to output

print(resumes[0]["hobbies"][1])

print("------------------------") #gives space to output

