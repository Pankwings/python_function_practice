###----------Python unit testing - pytest parameters----------------##
def cal_square(num):
    return(num*num)


##----------Python unit testing - pytest fixtures------------##
## Mock (or Fake) database created for demonstration purpose
## Lecture 37

## "This one didn't work.""

# class MyDB:
#     def __init__(self) -> None:
#         self.connection = Connection()

#     def connect(self, connection_string):
#         return self.connection

# class Connection:
#     def __init__(self) -> None:
#         self.cur = Cursor()
    
#     def cursor(self):
#         return self.cur

#     def close(self):
#         pass
# class Cursor():
#     def execute(self, query):
#         if query == "select if from employee_db where name=John":
#             return 123

#         elif query == "select if from employee_db where name=Tom":
#             return 789
#         else:
#             return -1

#     def close(self):
#         pass

##------------------

# def cal_total(a,b):
#     return(a+b)

# def cal_mul(a,b):
#     return(a*b)

##------------------
