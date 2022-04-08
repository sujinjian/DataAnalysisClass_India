from collections import Counter

# open the data file for reading
fp = open("course_data.txt","r")

# initialize mydict to empty dict, courses to empty list
mydict = {}
courses = []

# read each line of the courses_data.txt file
for line in fp:
    line = line.strip()
    (cnum, instr) = line.split()
    # use setdefault to add the current instructor to the list for this course
    mydict.setdefault(cnum,[]).append(instr)
    # add the current course to the list of courses (for use with counter)
    courses.append(cnum)
print (mydict)

print (courses)
# create a Counter based on the courses list
c = Counter(courses)
# print the top two most common courses
top2 = c.most_common(2)
print (top2)
