def get_value_from_nested_object(nested_object, key):
    key_list = key.split("/")
    current_val = nested_object
    for k in key_list:
        current_val = current_val.get(k, None)
        if current_val is None:
            return None
    return current_val

object_input = input("Please enter the nested object in the form of a dictionary: ")
key_input = input("Please enter the key in the form of 'x/y/z': ")

object_dict = eval(object_input)  
value = get_value_from_nested_object(object_dict, key_input)

print(f"The value associated with key '{key_input}' in the nested object is: {value}")
