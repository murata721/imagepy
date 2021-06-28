def read_and_process(*args):    
    from rapper import rap_class
    rap_obj = rap_class.rap(args)
    
    rap_obj.nums[0] += 100
    rap_obj.print_nums()

    return rap_obj
