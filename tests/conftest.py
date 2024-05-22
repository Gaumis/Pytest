import pytest
from source.school import Classroom

@pytest.fixture
def hogwarts_classroom():
    harry = Classroom.Student("Harry Potter")
    hermione = Classroom.Student("Hermione Granger")
    ron = Classroom.Student("Ron Weasley")
    snape = Classroom.Teacher("Severus Snape")
    return Classroom(teacher=snape, students=[harry, hermione, ron], course_title="Potions")

@pytest.fixture
def full_classroom():
    students = [Classroom.Student(f"Student {i}") for i in range(10)]
    snape = Classroom.Teacher("Severus Snape")
    return Classroom(teacher=snape, students=students, course_title="Defence Against the Dark Arts")
