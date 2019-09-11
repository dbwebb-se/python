message = "Python är det bästa programmeringsspråket!"
end_message = ""
for letter in message:
    if letter is not " ":
        end_message += letter
print(end_message)
