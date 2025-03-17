import os
import re
import xml.etree.ElementTree as ET
import json
import yaml


# 1
def create_text_file(name):

    students = [
        ('Jane Corden', 'Group A', (4, 7, 8)),
        ('Kate Blake', 'Group B', (9, 9, 8)),
        ('Oliver Whales', 'Group B', (4, 8, 9)),
        ('Elijah Knight', 'Group A', (4, 5, 9)),
    ]

    with open(name, 'w') as file:
        for student in students:
            # Записываем данные о каждом студенте в файл
            file.write(f"Name: {student[0]}, Group: {student[1]}, "
                       f"Marks: {','.join(map(str, student[2]))}\n")

    print(f"File {name} is created with list of students!")


def open_read_file(name):
    if not os.path.exists(name):
        raise FileNotFoundError(f"File {name} not found")

    with open(name, 'r') as file:
        lines = file.readlines()
        result = []
        for line in lines:
            result.append(line.strip())
        return result


def students_data(students):
    total_number_of_students = len(students)
    students_in_group = {}
    group_grades = {}

    for student in students:
        i = student.split(", ")
        group = i[1].split(": ")[1]
        marks = list(map(int, i[2].split(": ")[1].split(",")))

        average_grade = sum(marks) / len(marks)

        if group not in students_in_group:
            students_in_group[group] = 0
            group_grades[group] = []

        students_in_group[group] += 1
        group_grades[group].append(average_grade)

    for group in group_grades:
        group_grades[group] = (sum(group_grades[group])
                               / len(group_grades[group]))

    return total_number_of_students, students_in_group, group_grades


def write_to_end_file(name, total_number_of_students,
                      students_in_group, group_grades):
    with open(name, 'a') as file:
        file.write(f"\nTotal number of students: {total_number_of_students}\n")
        for group, count in students_in_group.items():
            file.write(f"Group: {group}, number of students: {count}, "
                       f"average grade: {group_grades[group]}\n")


name = "students.txt"
create_text_file(name)

try:
    data_list = open_read_file(name)
    for i in data_list:
        print(i)
    total_number_of_students, students_in_group, group_grades = (
        students_data(data_list))
    print(f"\nTotal number of students: {total_number_of_students}")
    print(f"Students in each group: {students_in_group}")
    print(f"Average grades in each group: {group_grades}")
    write_to_end_file(name, total_number_of_students, students_in_group, group_grades)
    print(f"Results are written to end of file {name}")

except FileNotFoundError as error:
    print(error)


# 2 "dd.mm.yyyy"
def find_dates(name):

    with open(name, 'r') as file:
        text = file.read()
    date_format = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)

    if date_format:
        for i in date_format:
            print(i)
    else:
        print('No dates in file')


name = 'Date.txt'
find_dates(name)


# 3
def find_valid_password(password):
    if (len(password) >= 4 and re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password)):
        return True
    return False


passwords = ['123', '1234', 'abcd', 'Abcd', 'Abc1', '54Gbd']
for i in passwords:
    if find_valid_password(i):
        print(f'Password "{i}" is valid')
    else:
        print(f'Password "{i}" is not valid')


# 4
def correct_text(text):
    pattern = r'(\w+)\s+\1'
    corrected_text = re.sub(pattern, r'\1', text)
    return corrected_text


text = ('Довольно распространённая ошибка ошибка — это '
        'лишний повтор повтор слова слова. Смешно, '
        'не не правда ли? Не нужно портить хор хоровод.')

no_repeats_text = correct_text(text)
print(f'Fixed text with no repeats: {no_repeats_text}')


# 5 XML
def total_cost_calculation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    total_cost = 0

    for good in root.findall('good'):
        price = int(good.find('price').text)
        quantity = int(good.find('quantity').text)
        total_cost += price * quantity

    return total_cost


xml_file = 'Goods.xml'
total_cost = total_cost_calculation(xml_file)
print(f"Total cost of the goods is: {total_cost}")


# 6 JSON
def find_club_with_most_wins(json_file):
    with open(json_file, 'r') as file:
        football_clubs = json.load(file)

    number_of_wins = 0
    club_with_most_wins = None
    for i in football_clubs:
        if i['wins'] > number_of_wins:
            number_of_wins = i['wins']
            club_with_most_wins = i

    return club_with_most_wins


json_file = 'FootballClubs.json'
club_with_most_wins = find_club_with_most_wins(json_file)
if club_with_most_wins:
    print(f"Football Club with most wins is {club_with_most_wins['name']} "
          f"with {club_with_most_wins['wins']} wins from "
          f"{club_with_most_wins['country']}")
else:
    print("No Football Clubs were found")


# 7 YAML
def display_books(filename):
    with open(filename, 'r') as file:
        books = yaml.load(file, Loader=yaml.SafeLoader)
        return books or []


def add_book(books):
    name = input("Enter name of the book: ")
    author = input("Enter author of the book: ")
    released = int(input("Enter year when the book was released: "))

    new_book = {
        'name': name,
        'author': author,
        'released': released
    }
    books.append(new_book)
    print("Book added successfully!")


def save_books(filename, books):
    with open(filename, 'w') as file:
        yaml.dump(books, file)


filename = 'Books.yaml'
books = display_books(filename)
print("List of books in file:")
for book in books:
    print(f"'{book['name']}' by {book['author']}, "
          f"released in {book['released']}")

add_book(books)
save_books(filename, books)
print(f"Changes saved in {filename}")
