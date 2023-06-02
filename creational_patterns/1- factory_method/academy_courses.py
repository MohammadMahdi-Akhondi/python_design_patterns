from abc import ABC, abstractmethod


class CourseCreator(ABC):
    @abstractmethod
    def create(self): pass

    def get_info(self):
        course = self.create()
        print(f'Info: {course.info()}')


class EnglishCreator(CourseCreator):
    def create(self):
        return EnglishCourse()


class ProgrammingCreator(CourseCreator):
    def create(self):
        return ProgrammingCourse()


class Course(ABC):
    @abstractmethod
    def info(self): pass


class EnglishCourse(Course):
    def info(self):
        return 'The duration of the English course is 10 hours'


class ProgrammingCourse(Course):
    def info(self):
        return 'The duration of the Programming course is 15 hours'


def course_client(course):
    return course.get_info()


if __name__ == '__main__':
    print('App Launched with the EnglishCreator')
    course_client(EnglishCreator())

    print('-' * 50)

    print('App Launched with the ProgrammingCreator')
    course_client(ProgrammingCreator())
