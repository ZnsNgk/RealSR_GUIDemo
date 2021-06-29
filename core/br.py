
break_flag = False

def init():
    global break_flag
    break_flag = False

def get_flag():
    return break_flag

def set_flag(flag):
    global break_flag
    break_flag = flag