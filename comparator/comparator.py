import os

def make_list_without(main_type = "idw", slave_type = "pdf"):
    # Makes list with main files, which have not pairs of slave files
    main_without_slave_list = sorted(list(set(extensions_dict[main_type]) - set(extensions_dict[slave_type])))
    print("\n {0} files without {1} files:\n---------------------------------------".format(main_type, slave_type))
    for number, item in enumerate(main_without_slave_list):
        print(number+1,": ", item)
    print("---------------------------------------\n")
    return {"main type" : main_type, "slave type" : slave_type, "operation" : "main without slave", "list" : main_without_slave_list}

def make_list_with (main_type = "idw", slave_type = "pdf"):
    # Makes list with main files, which have pairs of slave files
    main_with_slave_list = sorted(list(set(extensions_dict[main_type]) & set(extensions_dict[slave_type])))
    print("\n {0} files with {1} files:\n---------------------------------------".format(main_type, slave_type))
    for number, item in enumerate(main_with_slave_list):
        print(number+1,": ", item)
    print("---------------------------------------\n")
    return {"main type" : main_type, "slave type" : slave_type, "operation" : "main with slave", "list" : main_with_slave_list}
    

#cur_path = os.getcwd()
cur_path = "C:\\Users\\mrogozhyn\\Desktop\\test folder\\folder 1\\folder 1_1"

print("Curren directory:\n", cur_path,)

# Makes dictionary with all files information
names_dict = {}
file_types_set = set()
for name in os.listdir(cur_path):
    if os.path.isfile(os.path.join(cur_path, name)):
        names_dict[name] = {"File name": os.path.splitext(name)[0],
                            "File extension" : os.path.splitext(os.path.join(cur_path, name))[1][1:],
                            "File size" : os.path.getsize(os.path.join(cur_path, name)),
                            "File mod. time" : os.path.getmtime(os.path.join(cur_path, name))}
        file_types_set.add(os.path.splitext(os.path.join(cur_path, name))[1][1:])

# Makes list of all extensions from set with all extensions
file_types_list = sorted(list(file_types_set))
print("\nThere are files with extensions:\n---------------------------------------")
for number, type_ in enumerate(file_types_list):
    print(number+1,": ", type_)
print("---------------------------------------\n")

# Makes new dictionary with all extensions
extensions_dict = {}
for type_ in file_types_list:
    extensions_dict[type_] = []

# Adds file names to the list linked with the key
for key in extensions_dict:
    for name in names_dict:
        if names_dict[name]["File extension"] == key:
            extensions_dict[key].append(names_dict[name]["File name"])

idw_without_pdf = make_list_without()
idw_without_dwg = make_list_without("idw", "dwg")
idw_with_pdf = make_list_with()
idw_with_dwg = make_list_with("idw", "dwg")

time_dict = {}
for file in idw_with_pdf["list"]:
    time_dict[file] = round((names_dict[file + ".idw"]["File mod. time"] - names_dict[file + ".pdf"]["File mod. time"])/60)

print (time_dict)



input('')
