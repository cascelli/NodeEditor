import traceback

def dumbException(e):
    print('EXCEPTION:', e)
    traceback.print_tb(e.__traceback__)