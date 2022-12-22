# A software academy teaches two types of courses: local courses that are held in some of the academy’s local labs
# and offsite courses held in some other town outside of the academy’s headquarters. Each course has a name, a teacher
# assigned to teach it and a course program (sequence of topics). Each teacher has a name and knows the courses he or
# she teaches. Both courses and teachers could be printed in human-readable text form. All your courses should implement
# ICourse. Teachers should implement ITeacher. Local and offsite courses should implement ILocalCourse and IOffsiteCourse
# respectively. Courses and teachers should be created only through the ICourseFactory interface implemented by a class
# named CourseFactory. Write a program that will form courses of software academy.

import json
import os
from abc import ABC
from abc import abstractmethod

class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, value): pass

    @property
    @abstractmethod
    def courses(self): pass

    @abstractmethod
    def __str__(self): pass

class Teacher(ITeacher):
    staff_members = []

    def __init__(self, value):
        self.name = value["name"]
        self.__courses = []
        Teacher.staff_members.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Please, input a string value")
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    def add_course(self, value):
        self.__courses.append(value)

    def __str__(self):
        return f'{self.name} teaches next courses - {[elem.course_name for elem in self.courses]}'

    @classmethod
    def get_teacher(cls, value):
        for vals in cls.staff_members:
            if vals.name == value:
                return vals
        raise ValueError("None such teacher")


class ICourse(ABC):
    @property
    @abstractmethod
    def course_name(self): pass

    @course_name.setter
    @abstractmethod
    def course_name(self, value): pass

    @property
    @abstractmethod
    def teacher(self): pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value): pass

    @property
    @abstractmethod
    def course_program(self): pass

    @course_program.setter
    @abstractmethod
    def course_program(self, value): pass

    @abstractmethod
    def __str__(self): pass

class Course(ICourse):
    def __init__(self, data):
        self.course_name = data["name"]
        self.teacher = Teacher.get_teacher(data["teacher"])
        self.course_program = data["course program"]
        self.teacher.add_course(self)

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Please, input a string value")
        self._course_name = value

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Please, input an instance of Teacher class")
        self._teacher = value

    @property
    def course_program(self):
        return self._course_program

    @course_program.setter
    def course_program(self, value):
        if not all(isinstance(vals, str) for vals in value):
            raise TypeError("Please, input a string value sequence")
        self._course_program = value

    def __str__(self):
        return f'Course name: {self.course_name}. Course program: {self.course_program}. Course lecturer: {self.teacher.name}.'


class ICourseFactory(ABC):
    @abstractmethod
    def get_object(self): pass

class CourseFactory(ICourseFactory):
    def __init__(self, file):
        if not os.path.isfile(file):
            raise ValueError("None such file")
        with open(file, "r") as finp:
            self.stash = json.load(finp)

    def get_object(self):
        data = self.stash[0]
        self.stash.pop(0)
        match data.get("type"):
            case "local":
                return LocalCourse(data)
            case "offsite":
                return OffsiteCourse(data)
            case "teacher":
                return Teacher(data)
            case _:
                raise ValueError("Invalid json data")


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def auditory(self): pass

    @auditory.setter
    @abstractmethod
    def auditory(self, value): pass

class LocalCourse(ILocalCourse, Course):
    def __init__(self, value):
        super().__init__(value)
        self.auditory = value["auditory"]

    @property
    def auditory(self):
        return self._auditory

    @auditory.setter
    def auditory(self, value):
        if not isinstance(value, str):
            raise TypeError("Please, input a string address")
        self._auditory = value

    def __str__(self):
        return super().__str__() + f' Course classroom: {self.auditory}'


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def address(self): pass

    @address.setter
    @abstractmethod
    def address(self, value): pass

class OffsiteCourse(IOffsiteCourse, Course):
    def __init__(self, value):
        super().__init__(value)
        self.address = value["address"]

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("Please, input a string address")
        self._address = value

    def __str__(self):
        return super().__str__() + f' Course platform: {self.address}'

database = 'coursesandteachers.json'
objects = CourseFactory(database)
object1 = objects.get_object()
object2 = objects.get_object()
object3 = objects.get_object()
object4 = objects.get_object()
object5 = objects.get_object()
object6 = objects.get_object()
object7 = objects.get_object()
object8 = objects.get_object()
object9 = objects.get_object()

print("________________________________________________________________________________________________________________________________________________________")
print("1.", object1)
print("________________________________________________________________________________________________________________________________________________________")
print("2.", object2)
print("________________________________________________________________________________________________________________________________________________________")
print("3.", object3)
print("________________________________________________________________________________________________________________________________________________________")
print("4.", object4)
print("________________________________________________________________________________________________________________________________________________________")
print("5.", object5)
print("________________________________________________________________________________________________________________________________________________________")
print("6.", object6)
print("________________________________________________________________________________________________________________________________________________________")
print("7.", object7)
print("________________________________________________________________________________________________________________________________________________________")
print("8.", object8)
print("________________________________________________________________________________________________________________________________________________________")
print("9.", object9)
print("________________________________________________________________________________________________________________________________________________________")