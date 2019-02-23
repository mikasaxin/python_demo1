#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "zhaoxin"
import os,sys,re


class Person(object):

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def main(self):
        print "teacher %s" % self.name
        meta = __import__("student")
        stu = getattr(meta, "Student")
        student = stu("rose", "woman", "20")
        student.run(self.name, self.sex)
        print "teacher %s" % self.name
        print "student %s" % student.name


if __name__ == '__main__':
    args = sys.argv
    person = Person(args[1], args[2])
    exit(person.main())
