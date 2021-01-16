def data_type_operations(type_of_data, some_data):
    result = None

    if type_of_data == "int":
        result = int(some_data) * 2
    elif type_of_data == "real":
        result = f"{float(some_data) * 1.5:.2f}"
    elif type_of_data == "string":
        result = "$" + some_data + "$"

    return result


data_type = input()
data = input()
print(data_type_operations(data_type, data))