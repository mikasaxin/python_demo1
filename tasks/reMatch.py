#!/usr/bin/env python
# -- coding: gb2312 --
__author__ = "zhaoxin"
import re,os,sys
reload(sys)
sys.setdefaultencoding('gb2312')


class rematch:
    def __init__(self):
        self.file = r"D:\test.txt"
        self.replace_file = r"D:\test1.txt"
        self.text = ""

    def main(self):
        with open(self.file, "r") as f:
            self.text = f.read().decode(encoding="gb2312")
        pre_text = "zhaoxin"
        post_text = "teacher"
        contents1 = "ass a\n"
        print contents1
        __pattern = re.compile(r"(%s\s*)(\S.*\S)(.*%s)" % (pre_text, post_text), re.S)
        _pattern = re.compile(r"%s(.*)%s(.*?)%s" % (pre_text, contents1, post_text), re.S)
        matched = re.search(_pattern, self.text)
        if matched:
            print "matched"
        print(self.text)
        matchs = re.search(__pattern, self.text)
        str = "    赵新"
        print(str)
        self.text = re.sub(__pattern, r"\1%s\3" % str, self.text, 1)
        if matchs:
            with open(self.replace_file, "wb") as f:
                f.write(self.text.encode(encoding="gb2312"))
                #f.write(matchs.group(1))
                #f.write(matchs.group(2))
                #f.write(matchs.group(3))
            print("[group1:] %s" % matchs.group(1))
            print("[group2:] %s" % matchs.group(2))
            print("[group3:] %s" % matchs.group(3))


if __name__ == '__main__':
    matchobj = rematch()
    sys.exit(matchobj.main())