def print_logging(logtext):
    nonlocal logging_flag
    if logging_flag == True:
        print(logtext)

if __name__ == '__main__':
    logging_flag = True
    print_logging('test')
