
all_languages = []
at_least_one_language = []

num_students = int(input())

for _ in range(num_students):
    num_languages_known = int(input()) 
    student_languages = []
    for _ in range(num_languages_known):
        language = input()  
        student_languages.append(language)  
    at_least_one_language.extend(student_languages)
    if not all_languages:
        all_languages = student_languages.copy()
    else:
        all_languages = [language for language in all_languages if language in student_languages]

print(len(all_languages))
for language in sorted(all_languages):
    print(language)

print(len(set(at_least_one_language)))
for language in sorted(set(at_least_one_language)):
    print(language)
