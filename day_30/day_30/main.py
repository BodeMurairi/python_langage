try:
    file = open("a_file.txt")
    a_dict = {"Dict":"Value"}
    a_dict["Dict"]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The Key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise indexError as 