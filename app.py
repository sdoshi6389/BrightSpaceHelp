import datetime
import re
from flask import Flask, render_template

app = Flask(__name__)

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

course11AnnouncementHeaders = []
course11Announcements = []
course11ContentHeaders = []
course11Content = []
course11ContentTitles = []
course11ContentHref = []
course11Grades = []

course12AnnouncementHeaders = []
course12Announcements = []
course12ContentHeaders = []
course12Content = []
course12ContentTitles = []
course12ContentHref = []
course12Grades = []

course13AnnouncementHeaders = []
course13Announcements = []
course13ContentHeaders = []
course13Content = []
course13ContentTitles = []
course13ContentHref = []
course13Grades = []

course14AnnouncementHeaders = []
course14Announcements = []
course14ContentHeaders = []
course14Content = []
course14ContentTitles = []
course14ContentHref = []
course14Grades = []

course15AnnouncementHeaders = []
course15Announcements = []
course15ContentHeaders = []
course15Content = []
course15ContentTitles = []
course15ContentHref = []
course15Grades = []

# Course 1

with open('course1AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    fullHeader = ''
    counter = 0
    for line in file:
        if (counter == 0):
            fullHeader += line.strip() + " --- "
        if (counter == 1):
            fullHeader += line.strip()
        counter += 1
        if (counter == 2):
            course1AnnouncementHeaders.append(fullHeader)
            counter = 0
            fullHeader = ''

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

filtered_course1Grades = []

for i in range(len(course1Grades)): 
    temp = []
    for j in range(len(course1Grades[i])):
        if (course1Grades[i][j] != ''):
            temp.append(course1Grades[i][j])
    filtered_course1Grades.append(temp)

# print(filtered_course1Grades)

#Course 2

with open('course2AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course2AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course2Grades = []

for i in range(len(course2Grades)): 
    temp = []
    for j in range(len(course2Grades[i])):
        if (course2Grades[i][j] != ''):
            temp.append(course2Grades[i][j])
    filtered_course2Grades.append(temp)


# Course 3

with open('course3AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course3AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course3Grades = []

for i in range(len(course3Grades)): 
    temp = []
    for j in range(len(course3Grades[i])):
        if (course3Grades[i][j] != ''):
            temp.append(course3Grades[i][j])
    filtered_course3Grades.append(temp)

# Course 4

with open('course4AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course4AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course4Grades = []

for i in range(len(course4Grades)): 
    temp = []
    for j in range(len(course4Grades[i])):
        if (course4Grades[i][j] != ''):
            temp.append(course4Grades[i][j])
    filtered_course4Grades.append(temp)

# Course 5

with open('course5AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course5AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course5Grades = []

for i in range(len(course5Grades)): 
    temp = []
    for j in range(len(course5Grades[i])):
        if (course5Grades[i][j] != ''):
            temp.append(course5Grades[i][j])
    filtered_course5Grades.append(temp)

# Course 6

with open('course6AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course6AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course6Grades = []

for i in range(len(course6Grades)): 
    temp = []
    for j in range(len(course6Grades[i])):
        if (course6Grades[i][j] != ''):
            temp.append(course6Grades[i][j])
    filtered_course6Grades.append(temp)

# Course 7

with open('course7AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course7AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course7Grades = []

for i in range(len(course7Grades)): 
    temp = []
    for j in range(len(course7Grades[i])):
        if (course7Grades[i][j] != ''):
            temp.append(course7Grades[i][j])
    filtered_course7Grades.append(temp)

# Course 8

with open('course8AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course8AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course8Grades = []

for i in range(len(course8Grades)): 
    temp = []
    for j in range(len(course8Grades[i])):
        if (course8Grades[i][j] != ''):
            temp.append(course8Grades[i][j])
    filtered_course8Grades.append(temp)

# Course 9

with open('course9AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course9AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course9Grades = []

for i in range(len(course9Grades)): 
    temp = []
    for j in range(len(course9Grades[i])):
        if (course9Grades[i][j] != ''):
            temp.append(course9Grades[i][j])
    filtered_course9Grades.append(temp)

# Course 10

with open('course10AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if (counter == 0):
                fullHeader += line.strip() + " --- "
            if (counter == 1):
                fullHeader += line.strip()
            counter += 1
            if (counter == 2):
                course10AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

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

filtered_course10Grades = []

for i in range(len(course10Grades)): 
    temp = []
    for j in range(len(course10Grades[i])):
        if (course10Grades[i][j] != ''):
            temp.append(course10Grades[i][j])
    filtered_course10Grades.append(temp)

# Course 11

with open('course11AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if counter == 0:
                fullHeader += line.strip() + " --- "
            if counter == 1:
                fullHeader += line.strip()
            counter += 1
            if counter == 2:
                course11AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

# print(course11AnnouncementHeaders)

with open('course11Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course11Announcements.append(announcement)
            announcement = ''

# print(course11Announcements) 

with open('course11Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course11ContentHeaders.append(line.strip())

# print(course11ContentHeaders)

with open('course11Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course11Content.append((line.strip()).split(','))

for j in range(len(course11Content)):
    temp = []
    for i in range(len(course11Content[j])):
        match = re.search(r'title="([^"]*)"', course11Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course11ContentTitles.append(temp)

# print(course11ContentTitles)

for j in range(len(course11Content)):
    temp = []
    for i in range(len(course11Content[j])):
        match = re.search(r'href="([^"]*)"', course11Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course11ContentHref.append(temp)

# print(course11ContentHref)

with open('course11Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course11Grades.append((line.strip()).split(','))

# print(course11Grades)

filtered_course11Grades = []

for i in range(len(course11Grades)): 
    temp = []
    for j in range(len(course11Grades[i])):
        if course11Grades[i][j] != '':
            temp.append(course11Grades[i][j])
    filtered_course11Grades.append(temp)

# Course 12

with open('course12AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if counter == 0:
                fullHeader += line.strip() + " --- "
            if counter == 1:
                fullHeader += line.strip()
            counter += 1
            if counter == 2:
                course12AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

# print(course12AnnouncementHeaders)

with open('course12Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course12Announcements.append(announcement)
            announcement = ''

# print(course12Announcements) 

with open('course12Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course12ContentHeaders.append(line.strip())

# print(course12ContentHeaders)

with open('course12Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course12Content.append((line.strip()).split(','))

for j in range(len(course12Content)):
    temp = []
    for i in range(len(course12Content[j])):
        match = re.search(r'title="([^"]*)"', course12Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course12ContentTitles.append(temp)

# print(course12ContentTitles)

for j in range(len(course12Content)):
    temp = []
    for i in range(len(course12Content[j])):
        match = re.search(r'href="([^"]*)"', course12Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course12ContentHref.append(temp)

# print(course12ContentHref)

with open('course12Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course12Grades.append((line.strip()).split(','))

# print(course12Grades)

filtered_course12Grades = []

for i in range(len(course12Grades)): 
    temp = []
    for j in range(len(course12Grades[i])):
        if course12Grades[i][j] != '':
            temp.append(course12Grades[i][j])
    filtered_course12Grades.append(temp)

# Course 13

with open('course13AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if counter == 0:
                fullHeader += line.strip() + " --- "
            if counter == 1:
                fullHeader += line.strip()
            counter += 1
            if counter == 2:
                course13AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

# print(course13AnnouncementHeaders)

with open('course13Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course13Announcements.append(announcement)
            announcement = ''

# print(course13Announcements) 

with open('course13Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course13ContentHeaders.append(line.strip())

# print(course13ContentHeaders)

with open('course13Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course13Content.append((line.strip()).split(','))

for j in range(len(course13Content)):
    temp = []
    for i in range(len(course13Content[j])):
        match = re.search(r'title="([^"]*)"', course13Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course13ContentTitles.append(temp)

# print(course13ContentTitles)

for j in range(len(course13Content)):
    temp = []
    for i in range(len(course13Content[j])):
        match = re.search(r'href="([^"]*)"', course13Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course13ContentHref.append(temp)

# print(course13ContentHref)

with open('course13Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course13Grades.append((line.strip()).split(','))

# print(course13Grades)

filtered_course13Grades = []

for i in range(len(course13Grades)): 
    temp = []
    for j in range(len(course13Grades[i])):
        if course13Grades[i][j] != '':
            temp.append(course13Grades[i][j])
    filtered_course13Grades.append(temp)

# Course 14

with open('course14AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if counter == 0:
                fullHeader += line.strip() + " --- "
            if counter == 1:
                fullHeader += line.strip()
            counter += 1
            if counter == 2:
                course14AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

# print(course14AnnouncementHeaders)

with open('course14Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course14Announcements.append(announcement)
            announcement = ''

# print(course14Announcements) 

with open('course14Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course14ContentHeaders.append(line.strip())

# print(course14ContentHeaders)

with open('course14Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course14Content.append((line.strip()).split(','))

for j in range(len(course14Content)):
    temp = []
    for i in range(len(course14Content[j])):
        match = re.search(r'title="([^"]*)"', course14Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course14ContentTitles.append(temp)

# print(course14ContentTitles)

for j in range(len(course14Content)):
    temp = []
    for i in range(len(course14Content[j])):
        match = re.search(r'href="([^"]*)"', course14Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course14ContentHref.append(temp)

# print(course14ContentHref)

with open('course14Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course14Grades.append((line.strip()).split(','))

# print(course14Grades)

filtered_course14Grades = []

for i in range(len(course14Grades)): 
    temp = []
    for j in range(len(course14Grades[i])):
        if course14Grades[i][j] != '':
            temp.append(course14Grades[i][j])
    filtered_course14Grades.append(temp)

# Course 15

with open('course15AnnouncementHeaders.txt', 'r', encoding='utf-8') as file:
    for line in file:
        fullHeader = ''
        counter = 0
        for line in file:
            if counter == 0:
                fullHeader += line.strip() + " --- "
            if counter == 1:
                fullHeader += line.strip()
            counter += 1
            if counter == 2:
                course15AnnouncementHeaders.append(fullHeader)
                counter = 0
                fullHeader = ''

# print(course15AnnouncementHeaders)

with open('course15Announcements.txt', 'r', encoding='utf-8') as file:
    announcement = ''
    for line in file:
        announcement += line.strip()
        if "</d2l-html-block>" in line:
            announcement = announcement.replace('\n', '')
            announcement = announcement.replace('<d2l-html-block html="', '')
            announcement = announcement.replace('"></d2l-html-block>', '')
            course15Announcements.append(announcement)
            announcement = ''

# print(course15Announcements) 

with open('course15Headers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course15ContentHeaders.append(line.strip())

# print(course15ContentHeaders)

with open('course15Content.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course15Content.append((line.strip()).split(','))

for j in range(len(course15Content)):
    temp = []
    for i in range(len(course15Content[j])):
        match = re.search(r'title="([^"]*)"', course15Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course15ContentTitles.append(temp)

# print(course15ContentTitles)

for j in range(len(course15Content)):
    temp = []
    for i in range(len(course15Content[j])):
        match = re.search(r'href="([^"]*)"', course15Content[j][i])
        if match:
            title = match.group(1)
            temp.append(title)
    course15ContentHref.append(temp)

# print(course15ContentHref)

with open('course15Grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        course15Grades.append((line.strip()).split(','))

# print(course15Grades)

filtered_course15Grades = []

for i in range(len(course15Grades)): 
    temp = []
    for j in range(len(course15Grades[i])):
        if course15Grades[i][j] != '':
            temp.append(course15Grades[i][j])
    filtered_course15Grades.append(temp)


@app.route('/')
def home():
    return render_template('dashboard.html', courses=courseNames)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', courses=courseNames)

@app.route('/course1/')
def course1():
    return render_template('course1.html', courses=courseNames)

course1announce = list(zip(course1Announcements, course1AnnouncementHeaders))
@app.route('/course1announcements/')
def course1announcements():
    return render_template('announcements.html', announcements=course1announce, courses=courseNames)

course1contentinfo = list(zip(course1ContentHeaders, course1ContentTitles, course1ContentHref))
@app.route('/course1content/')
def course1content():
    return render_template('content.html', content=course1contentinfo, courses=courseNames)

@app.route('/course1grades')
def course1grades():
    return render_template('grades.html', grades=filtered_course1Grades, courses=courseNames)

@app.route('/course2/')
def course2():
    return render_template('course2.html', courses=courseNames)

course2announce = list(zip(course2Announcements, course2AnnouncementHeaders))
@app.route('/course2announcements/')
def course2announcements():
    return render_template('announcements.html', announcements=course2announce, courses=courseNames)

course2contentinfo = list(zip(course2ContentHeaders, course2ContentTitles, course2ContentHref))
@app.route('/course2content/')
def course2content():
    return render_template('content.html', content=course2contentinfo, courses=courseNames)

@app.route('/course2grades')
def course2grades():
    return render_template('grades.html', grades=filtered_course2Grades, courses=courseNames)

@app.route('/course3/')
def course3():
    return render_template('course3.html', courses=courseNames)

course3announce = list(zip(course3Announcements, course3AnnouncementHeaders))
@app.route('/course3announcements/')
def course3announcements():
    return render_template('announcements.html', announcements=course3announce, courses=courseNames)

course3contentinfo = list(zip(course3ContentHeaders, course3ContentTitles, course3ContentHref))
@app.route('/course3content/')
def course3content():
    return render_template('content.html', content=course3contentinfo, courses=courseNames)

@app.route('/course3grades')
def course3grades():
    return render_template('grades.html', grades=filtered_course3Grades, courses=courseNames)

@app.route('/course4/')
def course4():
    return render_template('course4.html', courses=courseNames)

course4announce = list(zip(course4Announcements, course4AnnouncementHeaders))
@app.route('/course4announcements/')
def course4announcements():
    return render_template('announcements.html', announcements=course4announce, courses=courseNames)

course4contentinfo = list(zip(course4ContentHeaders, course4ContentTitles, course4ContentHref))
@app.route('/course4content/')
def course4content():
    return render_template('content.html', content=course4contentinfo, courses=courseNames)

@app.route('/course4grades')
def course4grades():
    return render_template('grades.html', grades=filtered_course4Grades, courses=courseNames)

@app.route('/course5/')
def course5():
    return render_template('course5.html', courses=courseNames)

course5announce = list(zip(course5Announcements, course5AnnouncementHeaders))
@app.route('/course5announcements/')
def course5announcements():
    return render_template('announcements.html', announcements=course5announce, courses=courseNames)

course5contentinfo = list(zip(course5ContentHeaders, course5ContentTitles, course5ContentHref))
@app.route('/course5content/')
def course5content():
    return render_template('content.html', content=course5contentinfo, courses=courseNames)

@app.route('/course5grades')
def course5grades():
    return render_template('grades.html', grades=filtered_course5Grades, courses=courseNames)

@app.route('/course6/')
def course6():
    return render_template('course6.html', courses=courseNames)

course6announce = list(zip(course6Announcements, course6AnnouncementHeaders))
@app.route('/course6announcements/')
def course6announcements():
    return render_template('announcements.html', announcements=course6announce, courses=courseNames)

course6contentinfo = list(zip(course6ContentHeaders, course6ContentTitles, course6ContentHref))
@app.route('/course6content/')
def course6content():
    return render_template('content.html', content=course6contentinfo, courses=courseNames)

@app.route('/course6grades')
def course6grades():
    return render_template('grades.html', grades=filtered_course6Grades, courses=courseNames)

@app.route('/course7/')
def course7():
    return render_template('course7.html', courses=courseNames)

course7announce = list(zip(course7Announcements, course7AnnouncementHeaders))
@app.route('/course7announcements/')
def course7announcements():
  return render_template('course7announcements.html', announcements=course7announce, courses=courseNames)

course7contentinfo = list(zip(course7ContentHeaders, course7ContentTitles, course7ContentHref))
@app.route('/course7content/')
def course7content():
  return render_template('course7content.html', content=course7contentinfo, courses=courseNames)

@app.route('/course7grades')
def course7grades():
  return render_template('course7grades.html', grades=filtered_course7Grades, courses=courseNames)

@app.route('/course8/')
def course8():
    return render_template('course8.html', courses=courseNames)

course8announce = list(zip(course8Announcements, course8AnnouncementHeaders))
@app.route('/course8announcements/')
def course8announcements():
  return render_template('course8announcements.html', announcements=course8announce, courses=courseNames)

course8contentinfo = list(zip(course8ContentHeaders, course8ContentTitles, course8ContentHref))
@app.route('/course8content/')
def course8content():
  return render_template('course8content.html', content=course8contentinfo, courses=courseNames)

@app.route('/course8grades')
def course8grades():
  return render_template('course8grades.html', grades=filtered_course8Grades, courses=courseNames)

@app.route('/course9/')
def course9():
    return render_template('course9.html', courses=courseNames)

course9announce = list(zip(course9Announcements, course9AnnouncementHeaders))
@app.route('/course9announcements/')
def course9announcements():
  return render_template('course9announcements.html', announcements=course9announce, courses=courseNames)

course9contentinfo = list(zip(course9ContentHeaders, course9ContentTitles, course9ContentHref))
@app.route('/course9content/')
def course9content():
  return render_template('course9content.html', content=course9contentinfo, courses=courseNames)

@app.route('/course9grades')
def course9grades():
  return render_template('course9grades.html', grades=filtered_course9Grades, courses=courseNames)

@app.route('/course10/')
def course10():
    return render_template('course10.html', courses=courseNames)

course10announce = list(zip(course10Announcements, course10AnnouncementHeaders))
@app.route('/course10announcements/')
def course10announcements():
  return render_template('course10announcements.html', announcements=course10announce, courses=courseNames)

course10contentinfo = list(zip(course10ContentHeaders, course10ContentTitles, course10ContentHref))
@app.route('/course10content/')
def course10content():
  return render_template('course10content.html', content=course10contentinfo, courses=courseNames)

@app.route('/course10grades')
def course10grades():
  return render_template('course10grades.html', grades=filtered_course10Grades, courses=courseNames)

@app.route('/course11/')
def course11():
    return render_template('course11.html', courses=courseNames)

course11announce = list(zip(course11Announcements, course11AnnouncementHeaders))
@app.route('/course11announcements/')
def course11announcements():
  return render_template('course11announcements.html', announcements=course11announce, courses=courseNames)

course11contentinfo = list(zip(course11ContentHeaders, course11ContentTitles, course11ContentHref))
@app.route('/course11content/')
def course11content():
  return render_template('course11content.html', content=course11contentinfo, courses=courseNames)

@app.route('/course11grades')
def course11grades():
  return render_template('course11grades.html', grades=filtered_course11Grades, courses=courseNames)

@app.route('/course12/')
def course12():
    return render_template('course12.html', courses=courseNames)

course12announce = list(zip(course12Announcements, course12AnnouncementHeaders))
@app.route('/course12announcements/')
def course12announcements():
  return render_template('course12announcements.html', announcements=course12announce, courses=courseNames)

course12contentinfo = list(zip(course12ContentHeaders, course12ContentTitles, course12ContentHref))
@app.route('/course12content/')
def course12content():
  return render_template('course12content.html', content=course12contentinfo, courses=courseNames)

@app.route('/course12grades')
def course12grades():
  return render_template('course12grades.html', grades=filtered_course12Grades, courses=courseNames)

@app.route('/course13/')
def course13():
    return render_template('course13.html', courses=courseNames)

course13announce = list(zip(course13Announcements, course13AnnouncementHeaders))
@app.route('/course13announcements/')
def course13announcements():
  return render_template('course13announcements.html', announcements=course13announce, courses=courseNames)

course13contentinfo = list(zip(course13ContentHeaders, course13ContentTitles, course13ContentHref))
@app.route('/course13content/')
def course13content():
  return render_template('course13content.html', content=course13contentinfo, courses=courseNames)

@app.route('/course13grades')
def course13grades():
  return render_template('course13grades.html', grades=filtered_course13Grades, courses=courseNames)

@app.route('/course14/')
def course14():
    return render_template('course14.html', courses=courseNames)

course14announce = list(zip(course14Announcements, course14AnnouncementHeaders))
@app.route('/course14announcements/')
def course14announcements():
  return render_template('course14announcements.html', announcements=course14announce, courses=courseNames)

course14contentinfo = list(zip(course14ContentHeaders, course14ContentTitles, course14ContentHref))
@app.route('/course14content/')
def course14content():
  return render_template('course14content.html', content=course14contentinfo, courses=courseNames)

@app.route('/course14grades')
def course14grades():
  return render_template('course14grades.html', grades=filtered_course14Grades, courses=courseNames)

@app.route('/course15/')
def course15():
    return render_template('course15.html', courses=courseNames)

course15announce = list(zip(course15Announcements, course15AnnouncementHeaders))
@app.route('/course15announcements/')
def course15announcements():
  return render_template('course15announcements.html', announcements=course15announce, courses=courseNames)

course15contentinfo = list(zip(course15ContentHeaders, course15ContentTitles, course15ContentHref))
@app.route('/course15content/')
def course15content():
  return render_template('course15content.html', content=course15contentinfo, courses=courseNames)

@app.route('/course15grades')
def course15grades():
  return render_template('course15grades.html', grades=filtered_course15Grades, courses=courseNames)


# # ...
# @app.route('/about/')
# def about():
#     return render_template('about.html')

# ...

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

