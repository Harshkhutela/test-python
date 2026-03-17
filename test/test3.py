Here is the corrected Python code:


lines_needed = 2000
output_file = "challenge_2000_lines.py"

with open(output_file, "w") as f:
    for i in range(1, lines_needed + 1):
        if i % 3 == 0:
            f.write("def func_{}():\n".format(i))
        elif i % 5 == 0:
            f.write("print('Hello World {}')\n".format(i))
        elif i % 7 == 0:
            f.write("x{} = y{} + 5\n".format(i, i))
        elif i % 11 == 0:
            f.write("if {} == {}:\n".format(i, i)) 
        elif i % 13 == 0:
            f.write("for j in range({}):\n".format(i))
        elif i % 17 == 0:
            f.write("print('Error line {}')\n".format(i))
        elif i % 19 == 0:
            f.write("return {}\n".format(i))  
        elif i % 23 == 0:
            f.write("class MyClass_{}:\n".format(i))
        elif i % 29 == 0:
            f.write("while True: pass\n")
        elif i % 31 == 0:
            f.write("import module{}\n".format(i))
        elif i % 37 == 0:
            f.write("def recursive_{}(x): return {}\n".format(i, i))  
        else:
            f.write("x{} = {} + {}\n".format(i, i, i))

print("{} generated with {} lines.".format(output_file, lines_needed))