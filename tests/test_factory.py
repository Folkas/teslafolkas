import pytest


class Class:
    def __init__(self, students_list: list, teacher_name: str) -> None:
        self.__students_list = students_list
        self.__teacher_name = teacher_name

    def __str__(self) -> str:
        return f"Teacher of this class is {self.__teacher_name}. There are {len(self.__students_list)} students in the class."

    @property
    def students_count(self) -> int:
        return len(self.__students_list)

    def add_student(self, student_name: str) -> None:
        if student_name in self.__students_list:
            raise ValueError(f"Student {student_name} is already in the class!")
        self.__students_list.append(student_name)

    def remove_student(self, student_name) -> None:
        self.__students_list.remove(student_name)

model = Class(["Larry", "Amy", "Terrence"], ["Judith"])

# model.students_count
def test_students_count_is_correct():

  assert model.students_count == 3
    # CHECK IF STUDENTS COUNT IS CORRECT

def test_can_add_student():
  assert model.add_student("Jerry") is None
    # CHECK IF YOU CAN ADD STUDENT

def test_can_remove_student():
  assert model.remove_student("Jerry") is None
    # CHECK IF YOU CAN REMOVE STUDENT


def test_can_not_add_duplicate_student():
  with pytest.raises(ValueError):
    model.add_student("Amy")
    # CHECK IF CAN NOT ADD DUPLICATE STUDENT
