# create tmp.py
def rap_my_script(script_path,
                  rapper_path="rapper/rapper.txt",
                  write_path="rapper/tmp.py"):

    with open(rapper_path) as f:
        s_rapper = f.read()

    with open(script_path) as f:
        s_read_list = f.readlines()

    s_read = "    ".join(s_read_list)

    tmp_s = s_rapper.format(s_read)

    with open(write_path, mode='w') as f:
        f.write(tmp_s)
