# coding=utf-8
import re

# 匹配a z之间的任意字符

try:
    match = re.match(r"a.*z", "ab\nz")
    print match.group()
except AttributeError as attr_e:
    print attr_e
# 使用python代码 python中的re.DOTALL可以匹配到换行,默认.不能匹配换行,在python中有异常

match = re.match(r"a.*z", "ab\nz", re.DOTALL)
print match.group()

# 匹配任意两个字符
match = re.match(r"..", "\n\n", re.DOTALL)
print match.group()

# 匹配end之前的字符

match = re.match(r"(.*)end", "hello world end", re.DOTALL)
print match.group(1)

# 匹配已form开始的字符串

match = re.match(r"^from\s*(.*)", "from beijing", re.DOTALL)
print match.group(1)

# 匹配/bin/tcsh结尾的字符串

match = re.match(r"(.*)\s*/bin/tcsh$", "sh /bin/tcsh", re.DOTALL)
print match.group(1)

# 匹配任何由单独的字符串Subject：hi构成的字符串

match = re.match(r"^Subject：(.*)hi$", "Subject：hello hi", re.DOTALL)
print match.group(1)

# 匹配bat bet bit but
match = re.match(r"b(a|e|i|u)t", "bat")
print match.group(1)

# 匹配c2do 或者r3p2
match = re.match(r"[cr][23][dp][o2]", "c2do")
print match.group()
