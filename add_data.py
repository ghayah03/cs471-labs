import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()

from apps.bookmodule.models import Department, Card, Course, Student, Enrollment

# Delete old data
Department.objects.all().delete()
Card.objects.all().delete()
Course.objects.all().delete()
Student.objects.all().delete()
Enrollment.objects.all().delete()

# Create Departments
dept1 = Department.objects.create(name='Computer Science')
dept2 = Department.objects.create(name='Information Systems')
dept3 = Department.objects.create(name='Mathematics')

# Create Cards
card1 = Card.objects.create(card_number=1001)
card2 = Card.objects.create(card_number=1002)
card3 = Card.objects.create(card_number=1003)
card4 = Card.objects.create(card_number=1004)
card5 = Card.objects.create(card_number=1005)
card6 = Card.objects.create(card_number=1006)

# Create Courses
course1 = Course.objects.create(title='Programming', code=101)
course2 = Course.objects.create(title='Database', code=102)
course3 = Course.objects.create(title='Networks', code=103)
course4 = Course.objects.create(title='AI', code=104)

# Create Students
student1 = Student.objects.create(name='Ahmed', age=22, card=card1, department=dept1)
student2 = Student.objects.create(name='Sara', age=20, card=card2, department=dept1)
student3 = Student.objects.create(name='Mohammed', age=23, card=card3, department=dept2)
student4 = Student.objects.create(name='Fatima', age=21, card=card4, department=dept2)
student5 = Student.objects.create(name='Ali', age=22, card=card5, department=dept3)
student6 = Student.objects.create(name='Nora', age=20, card=card6, department=dept3)

# Enroll Students in Courses
Enrollment.objects.create(student=student1, course=course1)
Enrollment.objects.create(student=student1, course=course2)
Enrollment.objects.create(student=student2, course=course1)
Enrollment.objects.create(student=student2, course=course3)
Enrollment.objects.create(student=student3, course=course2)
Enrollment.objects.create(student=student3, course=course4)
Enrollment.objects.create(student=student4, course=course1)
Enrollment.objects.create(student=student4, course=course4)
Enrollment.objects.create(student=student5, course=course3)
Enrollment.objects.create(student=student6, course=course2)
Enrollment.objects.create(student=student6, course=course3)

print("=" * 50)
print(" Data inserted successfully!")
print("=" * 50)
print(f"Departments: {Department.objects.count()}")
print(f"Cards: {Card.objects.count()}")
print(f"Courses: {Course.objects.count()}")
print(f"Students: {Student.objects.count()}")
print(f"Enrollments: {Enrollment.objects.count()}")
print("=" * 50)