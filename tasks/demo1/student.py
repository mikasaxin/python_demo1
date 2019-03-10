#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "zhaoxin"

from Person import Person


class Student(Person):

    def __init__(self, name, sex, age):
        super(Student, self).__init__(name, sex)
        self.age = age

    @classmethod
    def run(cls, name, sex):
        student = Student("zhaoxin", "man", "34")
        print "student %s" % student.name
        print "%s%s%s" % (student.name, student.age, student.sex)


if __name__ == '__main__':
    exit(Student.run("", ""))
