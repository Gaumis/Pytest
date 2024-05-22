import pytest
from source.school import Classroom, TooManyStudents

@pytest.mark.add_student
def test_add_student(hogwarts_classroom):
    neville = Classroom.Student("Neville Longbottom")
    hogwarts_classroom.add_student(neville)
    assert neville in hogwarts_classroom.students

@pytest.mark.add_student
def test_add_student_to_full_classroom(full_classroom):
    with pytest.raises(TooManyStudents):
        full_classroom.add_student(Classroom.Student("New Student"))

@pytest.mark.remove_student
def test_remove_student(hogwarts_classroom):
    hogwarts_classroom.remove_student("Harry Potter")
    assert all(student.name != "Harry Potter" for student in hogwarts_classroom.students)

@pytest.mark.parametrize("teacher_name", ["Albus Dumbledore", "Minerva McGonagall"])
@pytest.mark.change_teacher
def test_change_teacher(hogwarts_classroom, teacher_name):
    new_teacher = Classroom.Teacher(teacher_name)
    hogwarts_classroom.change_teacher(new_teacher)
    assert hogwarts_classroom.teacher.name == teacher_name

@pytest.mark.remove_student
def test_remove_nonexistent_student(hogwarts_classroom):
    initial_count = len(hogwarts_classroom.students)
    hogwarts_classroom.remove_student("Draco Malfoy")
    assert len(hogwarts_classroom.students) == initial_count
