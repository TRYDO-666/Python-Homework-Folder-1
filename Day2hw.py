python_para = """A Python course provides comprehensive training in this versatile and beginner-friendly programming language. 
It typically covers fundamental concepts like syntax, data structures, and control flows. Students advance to more complex topics such as object-oriented programming, error handling, and working with popular libraries. 
Courses often include practical, hands-on projects to apply skills in real-world applications like web development, data analysis, and automation. This prepares learners for high-demand careers in numerous fields, making Python an invaluable asset for both novice and experienced programmers."""

print(len(python_para))

print(python_para[0:51])

print(python_para.replace("Python","PYTHON"))

print(python_para.lower())

print(python_para.strip())

Individual_words = python_para.split(" ")
print(Individual_words)

print(("Course" in python_para))

a=623
b=100

display = f"The course description is {a} characters long and has {b} words."
print(display)


