Here is the corrected Python code:


lines_needed = 2000
output_file = "challenge_2000_lines.py"

with open(output_file, "w") as f:
    for i in range(1, lines_needed + 1):
        if i % 3 == 0:
            f.write(f"def func_{i}():\n")
        elif i % 5 == 0:
            f.write(f"print('Hello World {i}')\n")
        elif i % 7 == 0:
            f.write(f"x{i} = y{i} + 5\n")
        elif i % 11 == 0:
            f.write(f"if {i} == {i}: \n") 
        elif i % 13 == 0:
            f.write(f"for j in range({i}): \n")
        elif i % 17 == 0:
            f.write(f"print('Error line {i}')\n")
        elif i % 19 == 0:
            f.write(f"return {i}\n")  
        elif i % 23 == 0:
            f.write(f"class MyClass_{i}:\n")
        elif i % 29 == 0:
            f.write("while True: \n")
        elif i % 31 == 0:
            f.write(f"import module{i}\n")
        elif i % 37 == 0:
            f.write(f"def recursive_{i}(x): return {i}\n")  
        else:
            f.write(f"val{i} = {i} + {i}\n")

print(f"{output_file} generated with {lines_needed} lines and 100+ intentional errors.")