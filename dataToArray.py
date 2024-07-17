import re

courseNames = []

with open('courseNames.txt', 'r') as file:
    for line in file:
        courseNames.append(line.strip())

# print(courseNames)

course1AnnouncementHeaders = []
course1Announcements = []
course1ContentHeaders = []
course1Content = []
course1ContentTitles = []
course1ContentHref = []
course1Grades = []

course2AnnouncementHeaders = []
course2Announcements = []
course2ContentHeaders = []
course2Content = []
course2ContentTitles = []
course2ContentHref = []
course2Grades = []

course3AnnouncementHeaders = []
course3Announcements = []
course3ContentHeaders = []
course3Content = []
course3ContentTitles = []
course3ContentHref = []
course3Grades = []

course4AnnouncementHeaders = []
course4Announcements = []
course4ContentHeaders = []
course4Content = []
course4ContentTitles = []
course4ContentHref = []
course4Grades = []

course5AnnouncementHeaders = []
course5Announcements = []
course5ContentHeaders = []
course5Content = []
course5ContentTitles = []
course5ContentHref = []
course5Grades = []

course6AnnouncementHeaders = []
course6Announcements = []
course6ContentHeaders = []
course6Content = []
course6ContentTitles = []
course6ContentHref = []
course6Grades = []

course7AnnouncementHeaders = []
course7Announcements = []
course7ContentHeaders = []
course7Content = []
course7ContentTitles = []
course7ContentHref = []
course7Grades = []

course8AnnouncementHeaders = []
course8Announcements = []
course8ContentHeaders = []
course8Content = []
course8ContentTitles = []
course8ContentHref = []
course8Grades = []

course9AnnouncementHeaders = []
course9Announcements = []
course9ContentHeaders = []
course9Content = []
course9ContentTitles = []
course9ContentHref = []
course9Grades = []

course10AnnouncementHeaders = []
course10Announcements = []
course10ContentHeaders = []
course10Content = []
course10ContentTitles = []
course10ContentHref = []
course10Grades = []

# Course 1

with open('course1AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course1AnnouncementHeaders.append(line.strip())

# print(course1AnnouncementHeaders)

with open('course1Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course1Announcements.append(announcement)
            announcement = ''

# print(course1Announcements) 

with open('course1Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course1ContentHeaders.append(line.strip())

# print(course1ContentHeaders)

with open('course1Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course1Content.append((line.strip()).split(','))

for j in range(len(course1Content)):
    temp = []
    for i in range(len(course1Content[j])):
        match = re.search(r'title="([^"]*)"', course1Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course1ContentTitles.append(temp)

# print(course1ContentTitles)

for j in range(len(course1Content)):
    temp = []
    for i in range(len(course1Content[j])):
        match = re.search(r'href="([^"]*)"', course1Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course1ContentHref.append(temp)

# print(course1ContentHref)

with open('course1Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course1Grades.append((line.strip()).split(','))

# print(course1Grades)


#Course 2

with open('course2AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course2AnnouncementHeaders.append(line.strip())

# print(course2AnnouncementHeaders)

with open('course2Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course2Announcements.append(announcement)
            announcement = ''

# print(course2Announcements) 

with open('course2Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course2ContentHeaders.append(line.strip())

# print(course2ContentHeaders)

with open('course2Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course2Content.append((line.strip()).split(','))

for j in range(len(course2Content)):
    temp = []
    for i in range(len(course2Content[j])):
        match = re.search(r'title="([^"]*)"', course2Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course2ContentTitles.append(temp)

# print(course2ContentTitles)

for j in range(len(course2Content)):
    temp = []
    for i in range(len(course2Content[j])):
        match = re.search(r'href="([^"]*)"', course2Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course2ContentHref.append(temp)

# print(course2ContentHref)

with open('course2Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course2Grades.append((line.strip()).split(','))

# print(course2Grades)


# Course 3

with open('course3AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course3AnnouncementHeaders.append(line.strip())

# print(course3AnnouncementHeaders)

with open('course3Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course3Announcements.append(announcement)
            announcement = ''

# print(course3Announcements) 

with open('course3Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course3ContentHeaders.append(line.strip())

# print(course3ContentHeaders)

with open('course3Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course3Content.append((line.strip()).split(','))

for j in range(len(course3Content)):
    temp = []
    for i in range(len(course3Content[j])):
        match = re.search(r'title="([^"]*)"', course3Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course3ContentTitles.append(temp)

# print(course3ContentTitles)

for j in range(len(course3Content)):
    temp = []
    for i in range(len(course3Content[j])):
        match = re.search(r'href="([^"]*)"', course3Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course3ContentHref.append(temp)

# print(course3ContentHref)

with open('course3Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course3Grades.append((line.strip()).split(','))

# print(course3Grades)


# Course 4

with open('course4AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course4AnnouncementHeaders.append(line.strip())

# print(course4AnnouncementHeaders)

with open('course4Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course4Announcements.append(announcement)
            announcement = ''

# print(course4Announcements) 

with open('course4Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course4ContentHeaders.append(line.strip())

# print(course4ContentHeaders)

with open('course4Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course4Content.append((line.strip()).split(','))

for j in range(len(course4Content)):
    temp = []
    for i in range(len(course4Content[j])):
        match = re.search(r'title="([^"]*)"', course4Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course4ContentTitles.append(temp)

# print(course4ContentTitles)

for j in range(len(course4Content)):
    temp = []
    for i in range(len(course4Content[j])):
        match = re.search(r'href="([^"]*)"', course4Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course4ContentHref.append(temp)

# print(course4ContentHref)

with open('course4Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course4Grades.append((line.strip()).split(','))

# print(course4Grades)


# Course 5

with open('course5AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course5AnnouncementHeaders.append(line.strip())

# print(course5AnnouncementHeaders)

with open('course5Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course5Announcements.append(announcement)
            announcement = ''

# print(course5Announcements) 

with open('course5Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course5ContentHeaders.append(line.strip())

# print(course5ContentHeaders)

with open('course5Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course5Content.append((line.strip()).split(','))

for j in range(len(course5Content)):
    temp = []
    for i in range(len(course5Content[j])):
        match = re.search(r'title="([^"]*)"', course5Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course5ContentTitles.append(temp)

# print(course5ContentTitles)

for j in range(len(course5Content)):
    temp = []
    for i in range(len(course5Content[j])):
        match = re.search(r'href="([^"]*)"', course5Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course5ContentHref.append(temp)

# print(course5ContentHref)

with open('course5Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course5Grades.append((line.strip()).split(','))

# print(course5Grades)


# Course 6

with open('course6AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course6AnnouncementHeaders.append(line.strip())

# print(course6AnnouncementHeaders)

with open('course6Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course6Announcements.append(announcement)
            announcement = ''

# print(course6Announcements) 

with open('course6Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course6ContentHeaders.append(line.strip())

# print(course6ContentHeaders)

with open('course6Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course6Content.append((line.strip()).split(','))

for j in range(len(course6Content)):
    temp = []
    for i in range(len(course6Content[j])):
        match = re.search(r'title="([^"]*)"', course6Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course6ContentTitles.append(temp)

# print(course6ContentTitles)

for j in range(len(course6Content)):
    temp = []
    for i in range(len(course6Content[j])):
        match = re.search(r'href="([^"]*)"', course6Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course6ContentHref.append(temp)

# print(course6ContentHref)

with open('course6Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course6Grades.append((line.strip()).split(','))

# print(course6Grades)


# Course 7

with open('course7AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course7AnnouncementHeaders.append(line.strip())

# print(course7AnnouncementHeaders)

with open('course7Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course7Announcements.append(announcement)
            announcement = ''

# print(course7Announcements) 

with open('course7Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course7ContentHeaders.append(line.strip())

# print(course7ContentHeaders)

with open('course7Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course7Content.append((line.strip()).split(','))

for j in range(len(course7Content)):
    temp = []
    for i in range(len(course7Content[j])):
        match = re.search(r'title="([^"]*)"', course7Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course7ContentTitles.append(temp)

# print(course7ContentTitles)

for j in range(len(course7Content)):
    temp = []
    for i in range(len(course7Content[j])):
        match = re.search(r'href="([^"]*)"', course7Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course7ContentHref.append(temp)

# print(course7ContentHref)

with open('course7Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course7Grades.append((line.strip()).split(','))

# print(course7Grades)


# Course 8

with open('course8AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course8AnnouncementHeaders.append(line.strip())

# print(course8AnnouncementHeaders)

with open('course8Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course8Announcements.append(announcement)
            announcement = ''

# print(course8Announcements) 

with open('course8Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course8ContentHeaders.append(line.strip())

# print(course8ContentHeaders)

with open('course8Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course8Content.append((line.strip()).split(','))

for j in range(len(course8Content)):
    temp = []
    for i in range(len(course8Content[j])):
        match = re.search(r'title="([^"]*)"', course8Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course8ContentTitles.append(temp)

# print(course8ContentTitles)

for j in range(len(course8Content)):
    temp = []
    for i in range(len(course8Content[j])):
        match = re.search(r'href="([^"]*)"', course8Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course8ContentHref.append(temp)

# print(course8ContentHref)

with open('course8Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course8Grades.append((line.strip()).split(','))

# print(course8Grades)


# Course 9

with open('course9AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course9AnnouncementHeaders.append(line.strip())

# print(course9AnnouncementHeaders)

with open('course9Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course9Announcements.append(announcement)
            announcement = ''

# print(course9Announcements) 

with open('course9Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course9ContentHeaders.append(line.strip())

# print(course9ContentHeaders)

with open('course9Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course9Content.append((line.strip()).split(','))

for j in range(len(course9Content)):
    temp = []
    for i in range(len(course9Content[j])):
        match = re.search(r'title="([^"]*)"', course9Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course9ContentTitles.append(temp)

# print(course9ContentTitles)

for j in range(len(course9Content)):
    temp = []
    for i in range(len(course9Content[j])):
        match = re.search(r'href="([^"]*)"', course9Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course9ContentHref.append(temp)

# print(course9ContentHref)

with open('course9Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course9Grades.append((line.strip()).split(','))

# print(course9Grades)


# Course 10

with open('course10AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course10AnnouncementHeaders.append(line.strip())

# print(course10AnnouncementHeaders)

with open('course10Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course10Announcements.append(announcement)
            announcement = ''

# print(course10Announcements) 

with open('course10Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course10ContentHeaders.append(line.strip())

# print(course10ContentHeaders)

with open('course10Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course10Content.append((line.strip()).split(','))

for j in range(len(course10Content)):
    temp = []
    for i in range(len(course10Content[j])):
        match = re.search(r'title="([^"]*)"', course10Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course10ContentTitles.append(temp)

# print(course10ContentTitles)

for j in range(len(course10Content)):
    temp = []
    for i in range(len(course10Content[j])):
        match = re.search(r'href="([^"]*)"', course10Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course10ContentHref.append(temp)

# print(course10ContentHref)

with open('course10Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course10Grades.append((line.strip()).split(','))

# print(course10Grades)