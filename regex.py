"""Module to get subdomain"""
import re

regex = r"(www.)|([\w\-\.]+).microsoft.com"

test_str = ("https://www.blog.microsoft.com/test/test\n"
            "https://blog.microsoft.com/test.html \n"
            "https://www.microsoft.com \n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print("Subdomain is {group}".format(group=match.group(2)))
