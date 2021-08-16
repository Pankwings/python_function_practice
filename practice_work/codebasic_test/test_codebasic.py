###----------Python unit testing- pytest parameter-----------------------------##

import codebasic
import pytest

@pytest.mark.parametrize("test_input, expected_output",
[
    (5, 25),
    (9, 81),
    (7, 49),
    (10, 100)
])
def test_cal_square(test_input, expected_output):
    result = codebasic.cal_square(test_input)
    assert result == expected_output
###----------------------------------------------------------###
'''Instead of 3 different function you can write in better way'''

# def test_cal_square_1():
#     result = codebasic.cal_square(5)
#     assert result == 25

# def test_cal_square_2():
#     result = codebasic.cal_square(7)
#     assert result == 49

# def test_cal_square_3():
#     result = codebasic.cal_square(10)
#     assert result == 100


###--------------------------Python unit testing - pytest fixtures--------------##
# from fixtures.mydb import MyDB

# def test_johns_id():
#     db = MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#     id == cur.execute("select if from employee_db where name=John")
#     assert id == 123

# def test_toms_id():
#     db = MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#     id == cur.execute("select if from employee_db where name=Tom")
#     assert id == 789
##---------------------------------------------------------------------------##



#### Python unit testing - Skip/Selectively run tests in pytest.

# import codebasic
# import pytest
# import sys


##--------------------Test for program---------------------------------------##
# #@pytest.mark.skip(reason="I don't want to run this function for the moment")
# # The program below the ".skip()" will get skipped.
# def test_cal_total():
#     total = codebasic.cal_total(6,7)
#     assert total == 13

# #@pytest.mark.skipif(sys.version_info < (3,5),reason="I don't want to run this function for the moment")    
# # If the version of the python is < 3.5, then skip the "test_cal_mul()" 
# def test_cal_mul():
#     result = codebasic.cal_mul(10,3)
#     assert result == 30
    
# def test_dummy():
#     print("Dummy test.")
#     assert True

##------------------------------------------------------------------------##
##---------------------------Test for OS----------------------------------##
# '''
# Customizing the test into two catagories i.e., windows and linux.

# Use: $ pytest -m linux
# '''

# @pytest.mark.windows
# def test_windows_1():
#     assert True

# @pytest.mark.windows    
# def test_windows_2():
#     assert True

# @pytest.mark.linux    
# def test_linux_1():
#     assert True

# @pytest.mark.linux    
# def test_linux_2():
#     assert True
    
##-----------------------------------------------------------------------##