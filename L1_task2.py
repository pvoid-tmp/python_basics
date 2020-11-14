# Lesson 1 task 2
# no input data control

while True:
    inp_time = (input("Enter time in seconds or N to exit: "))
    if inp_time == 'N':
        break
    inp_time = int(inp_time)
    if inp_time < 0:
        print("Error: negative time")
        continue
    print(f"{inp_time // 3600:02d}:{(inp_time % 3600) // 60:02d}:{inp_time % 60:02d}")
