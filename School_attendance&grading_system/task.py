import logging

# The task was to write a python programme that simulates a school's attendance and grading system.
# The school has subjects, which have students.
# The school should be able to add subjects and students.
# The school should also be able to add students to subjects.
# The school should also be able to print out the average score and attendance of a subject.
# The school should also be able to print out the average score of a school.
# The school should also be able to print out the average score and attendance of a student.

def add_student(school,subject,student):
    school.add_student(student)
    subject.add_student(student)
    student.add_class(subject.title)


def add_subject(school,subject):
    school.add_subject(subject)


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.classes_score = {}
        self.classes_attendance = {}

    def add_class(self, class_name):
        self.classes_score[class_name] = []
        self.classes_attendance[class_name] = []

    def add_score(self, class_name, score):
        if class_name in self.classes_score:
            self.classes_score[class_name].append(score)
        else:
            logging.warning("Student {} {} not in class {}.".format(self.name,self.surname))

    def get_score(self, class_name):
        if class_name in self.classes_score:
            return sum(self.classes_score[class_name])/len(self.classes_score[class_name])
        else:
            logging.warning("Student {} {} not in class {}.".format(self.name,self.surname))

    def add_attendance(self,class_name):
        if class_name in self.classes_attendance:
            self.classes_attendance[class_name].append(1)
        else:
            logging.warning("Student {} {} not in class {}.".format(self.name,self.surname))

    def get_attendance(self,class_name):
        if class_name in self.classes_attendance:
            if len(self.classes_attendance[class_name]) == 0:
                logging.warning("Student {} {} has no attendance in class {}.".format(self.name,self.surname,class_name))
                return 0
            return sum(self.classes_attendance[class_name])/len(self.classes_attendance[class_name])
        else:
            logging.warning("Student {} {} not in class {}.".format(self.name,self.surname))

class Subject:
    def __init__(self,title):
        self.title = title
        self.students = []
    
    def add_student(self,student):
        self.students.append(student)

    def get_average_class(self):
        avg = 0
        for student in self.students:
            avg += student.get_score(self.title)
        return avg/len(self.students)
    
    def get_average_attendance(self):
        avg = 0
        for student in self.students:
            avg += student.get_attendance(self.title)
        return avg/len(self.students)
    
class School:
    def __init__(self,name):
        self.name = name
        self.subjects = []
        self.students = []

    def add_subject(self,subject):
        self.subjects.append(subject)

    def add_student(self,student):
        self.students.append(student)

    def get_average_school(self):
        avg = 0
        for subject in self.subjects:
            avg += subject.get_average_class()
        return avg/len(self.subjects)

def main():
    school = School("AGH")
    subject = Subject("Math")
    subject1 = Subject("Spanish")
    subject2 = Subject("English")
    student = Student("Jan","Kowalski")
    student1 = Student("Adam","Nowak")
    school.add_subject(subject)
    school.add_subject(subject1)
    school.add_subject(subject2)
    school.add_student(student)
    school.add_student(student1)
    subject.add_student(student)
    subject.add_student(student1)
    subject1.add_student(student)
    subject1.add_student(student1)
    subject2.add_student(student)
    subject2.add_student(student1)
    student.add_class("Math")
    student.add_class("Spanish")
    student.add_class("English")
    student.add_score("Math",5)
    student.add_score("Spanish",4)
    student.add_score("English",3)
    student.add_attendance("Math")
    student.add_attendance("Spanish")
    student1.add_class("Math")
    student1.add_class("Spanish")
    student1.add_class("English")
    student1.add_score("Math",5)
    student1.add_score("Spanish",5)
    student1.add_score("English",5)
    student1.add_attendance("Math")
    student1.add_attendance("Spanish")
    student1.add_attendance("English")
    print("Average score in Math: {}".format(subject.get_average_class()))
    print("Average score in Spanish: {}".format(subject1.get_average_class()))
    print("Average score in English: {}".format(subject2.get_average_class()))  
    print("Average attendance in Math: {}".format(subject.get_average_attendance()))
    print("Average attendance in Spanish: {}".format(subject1.get_average_attendance()))
    print("Average attendance in English: {}".format(subject2.get_average_attendance()))
    print("Average score in school: {}".format(school.get_average_school()))

if __name__ == "__main__":
    main()