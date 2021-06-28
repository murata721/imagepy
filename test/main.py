from rapper import rapper

main_a = 15
main_b = 30

rapper.rap_my_script("process.py")

# read created tmp.py
from rapper import tmp
return_obj = tmp.read_and_process(main_a, main_b)

print(type(return_obj))
