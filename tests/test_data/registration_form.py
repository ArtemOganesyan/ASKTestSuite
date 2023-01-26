class RegistrationFormEmail:
    #  213 Allowable characters: Alphanumeric & Special characters
    positive1 = {"test_data":
                     {"email": "aA1!@gmail.com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 200, "message": "User was created"}}
   #  228 Email field required, can’t be empty
    negative1 = {"test_data":
                     {"email": "",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "No recipients defined"}}

    #  233 Max 128 characters (128)
    positive2 =  {"test_data":
                     {"email": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa."
                               "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 200, "message": "User was created"}}


    #  239 Max 128 characters (129)
    negative2 =  {"test_data":
                     {"email": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa."
                               "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "Data too long for column 'email' at row 1"}}

    #  236 White spaces are not allowed (local port)

    negative3 =  {"test_data":
                     {"email": "student11 @gmail.com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "Can't send mail - all recipients were rejected: 553-5.1.3 The recipient address <student11 @gmail.com> is not a valid RFC-5321"}}


    # 330  White spaces are  not allowed(domain)
    negative4 = {"test_data":
                     {"email": "student11@ gmail.com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "Can't send mail - all recipients were rejected: 553-5.1.3 The recipient address <student11@ gmail.com> is not a valid RFC-5321"}}

    # 331 White spaces are not allowed (last part of the domain)
    negative5 = {"test_data":
                     {"email": "student11@gmail. com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "Some Error"}}

    # 240 Local port with 64 characters (64)
    positive3 = {"test_data":
                     {"email": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 200, "message": "User was created"}}

    # 241 Local port with 64 characters (65)
    negative6 = {"test_data":
                     {"email": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "Some Error"}}

    # 242 Domain on the right with 63 characters (63)
    positive4 = {"test_data":
                     {"email": "student11@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 200, "message": "User was created"}}

   # 243 Domain on the right with 63 characters (64)
    negative7 = {"test_data":
                     {"email": "student11@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "Some Error"}}

    # 244 63 characters in the last part of the domain (63)
    positive5 = {"test_data":
                     {"email": "student11@gmail.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 200, "message": "User was created"}}


    # 245 63 characters in the last part of the domain (64)
    negative8 = {"test_data":
                     {"email": "student11@gmail.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "Some Error"}}

    # 458 should contain top level domain separated by dot
    negative9 = {"test_data":
                     {"email": "student11@gmailcom",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "Some Error"}}

    # 459 should contain @ sign separating domain from local port
    negative10 = {"test_data":
                     {"email": " student11gmail.com",
                      "password": "12345",
                      "name": "Student Eleven",
                      "group": "CAB"},
                 "expected_result": {"status_code": 500, "message": "No recipients defined"}}