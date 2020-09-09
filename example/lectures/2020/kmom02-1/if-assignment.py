"""
Check if input integers follow criteria
"""
first = int(input("Enter an integer"))
second = int(input("Enter another integer"))

# Non validating solution
# message = "Rejected"
# if (first > 10 and first < 100) and (second > 10 and second < 100):
#     if first < 50 or second < 50:
#         if first > 40 or second > 40:
#             message = "Approved"
# 
# print(message)

# Best solution
message = "Rejected"
if 10 < first < 100 and 10 < second < 100:
    if first < 50 or second < 50:
        if first > 40 or second > 40:
            message = "Approved"
print(message)
# 
# Less good solution
# if 10 < first < 100 and 10 < second < 100:
#     if first < 50 or second < 50:
#         if first > 40 or second > 40:
#             print("Approved")
#         else:
#             print("Rejected")
#     else:
#         print("Rejected")
# else:
#     print("Rejected")
