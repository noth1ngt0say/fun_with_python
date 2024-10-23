import datetime
FILE_LOG = 'cesar.txt'
def logger(message_, file_):
    time_ = datetime.datetime.now()
    fd = open("cesar.txt", "at", encoding="utf-8")
    error = f'{time_}:File: {file_} Message: {message_}'
    fd.write(error + '\n')
    fd.close()