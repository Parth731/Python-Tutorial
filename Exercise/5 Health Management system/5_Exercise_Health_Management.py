# import datetime
#
# def gettime():
#     return datetime.datetime.now()
#
# # print(gettime())
# # 2020-09-18 10:26:47.019778
# print(str([str(gettime())]))
#
#
# def tack_information(lock):
#
#     if lock == 1:
#         choose = int(input("1 for Exercise:\n2 for Diet\n"))
#         if choose == 1:
#             value = input("Enter Exercise\n")
#             print(str([str(gettime())]), value)
#             with open("Rohit_Exercise.txt","a") as fop:
#                 fop.write(str([str(gettime())]) +  " : " + value + "\n")
#                 print("Rohit_Exercise.txt successfully write")
#             fop.close()
#         elif choose == 2:
#             value = input("Enter Diet\n")
#             print(str([str(gettime())]), value)
#             with open("Rohit_Diet.txt","a") as fop:
#                 fop.write(str([str(gettime())]) +  " : " + value + "\n")
#                 print("Rohit_Diet.txt successfully write")
#             fop.close()
#
#     if lock == 2:
#         choose = int(input("1 for Exercise:\n2 for Diet\n"))
#         if choose == 1:
#             value = input("Enter Exercise\n")
#             print(str([str(gettime())]), value)
#             with open("Parth_Exercise.txt", "a") as fop:
#                 fop.write(str([str(gettime())]) + " : " + value + "\n")
#                 print("Parth_Exercise.txt successfully write")
#             fop.close()
#         elif choose == 2:
#             value = input("Enter Diet\n")
#             print(str([str(gettime())]), value)
#             with open("Parth_Diet.txt", "a") as fop:
#                 fop.write(str([str(gettime())]) + " : " + value + "\n")
#                 print("Parth_Diet.txt successfully write")
#             fop.close()
#
#
#     if lock == 3:
#         choose = int(input("1 for Exercise:\n2 for Diet\n"))
#         if choose == 1:
#             value = input("Enter Exercise\n")
#             print(str([str(gettime())]), value)
#             with open("Dhoni_Exercise.txt", "a") as fop:
#                 fop.write(str([str(gettime())]) + " : " + value + "\n")
#                 print("Dhoni_Exercise.txt successfully write")
#             fop.close()
#         elif choose == 2:
#             value = input("Enter Diet\n")
#             print(str([str(gettime())]), value)
#             with open("Dhoni_Diet.txt", "a") as fop:
#                 fop.write(str([str(gettime())]) + " : " + value + "\n")
#                 print("Dhoni_Diet.txt successfully write")
#             fop.close()
#
#
# def retrieve_Information(rev):
#     if rev == 1:
#         choose = int(input("1 for Exercise:\n2 for Diet\n"))
#         if choose == 1:
#             with open("Rohit_Exercise.txt") as fop:
#                 print(fop.read())
#             print("Rohit_Exercise.txt successfully read")
#             fop.close()
#         if choose == 2:
#             with open("Rohit_Daite.txt") as fop:
#                 print(fop.read())
#             print("Rohit_Daite.txt successfully read")
#             fop.close()
#
#     if rev == 2:
#         choose = int(input("1 for Exercise:\n2 for Diet\n"))
#         if choose == 1:
#             with open("Parth_Exercise.txt") as fop:
#                 print(fop.read())
#             print("Parth_Exercise.txt successfully read")
#             fop.close()
#         if choose == 2:
#             with open("Parth_Diet.txt") as fop:
#                 print(fop.read())
#             print("Parth_Diet.txt successfully read")
#             fop.close()
#
#     if rev == 3:
#         choose = int(input("1 for Exercise:\n2 for Diet\n"))
#         if choose == 1:
#             with open("Dhoni_Exercise.txt") as fop:
#                 print(fop.read())
#             print("Dhoni_Exercise.txt successfully read")
#             fop.close()
#         if choose == 2:
#             with open("Dhoni_Diet.txt") as fop:
#                 print(fop.read())
#             print("Dhoni_Diet.txt successfully read")
#             fop.close()
#
#
#
#
#
# def Introduction():
#     print(" Health Management System ")
#
#     lr = int(input("choose:\n1 for lock:\n2 for retrieve:\n"))
#
#     if lr == 1:
#         lock = int(input("1. Rohit\n2. Parth\n3. Dhoni\n"))
#         tack_information(lock)
#     elif lr == 2:
#         rev =  int(input("1. Rohit\n2. Parth\n3. Dhoni\n"))
#         retrieve_Information(rev)
#     else:
#         print("please valid input\nchoose:\n1 for lock:\n2 for retrieve:\n")
#         exit()
#
#
# Introduction()
#
#
#################################################


import datetime

def gettime():
    return datetime.datetime.now()


Client_list = {
    1: "Dhoni",
    2: "Rohit",
    3: "Parth",
}
log_list = {
    1 : "Exercise",
    2 : "Diet"
}

try:

    print("Select Client Name")
    for key,value in Client_list.items():
        print("Press",key,"For",value)
    client_name = int(input())

    print("Select Client :",Client_list[client_name],"\n")

    print("1 For log")
    print("2 For Retrieve")
    op = int(input())

    if op == 1:

        for key,value in log_list.items():
            print("Press", key, "to log",value)
        log_name = int(input())

        print("Select Job :",log_list[log_name],"\n")
        fop = open(Client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k="y"
        while(k!="n"):
            print("Enter",log_list[log_name])
            mytext = input()
            fop.write("[" + str(gettime()).replace(":","-") + "] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        fop.close()
    elif op == 2:
        for key,value in log_list.items():
            print("Press", key, "to log",value)
        log_name = int(input())
        print(Client_list[client_name],"-",log_list[log_name],"Report : ","\n")
        fop = open(Client_list[client_name] + "_" + log_list[log_name] + ".txt")
        contents = fop.readlines()
        for line in contents:
            print(line, end="")
        fop.close()
    else:
        print("Invalid Input")

except:
    print("Something wrong")



