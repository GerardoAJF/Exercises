with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/no_space_left_on_device_input.txt", "r+") as f:

    base_directory = {}
    actual_directory = {}

    for line in f:

        command_parts = line.strip().split()
        if command_parts[0] == "$" and command_parts[1] == "cd":

            if command_parts[2] == "/":
                base_directory = {"name": "/",
                                  "parent": None,
                                  "dirs": [],
                                  "files": [],
                                  "weight": 0}

                actual_directory = base_directory
                continue

            if command_parts[2] == "..":
                parent_directory = actual_directory["parent"]

                actual_directory = parent_directory
                continue

            sub_directory = {"name": command_parts[2],
                             "parent": actual_directory,
                             "dirs": [],
                             "files": [],
                             "weight": 0}
            actual_directory["dirs"].append(sub_directory)

            actual_directory = sub_directory

        elif command_parts[0] != "$" and command_parts[0] != "dir":
            actual_directory["files"].append((command_parts[0], command_parts[1]))
            actual_directory["weight"] += int(command_parts[0])

    directorys = [base_directory]
    new_directorys =  []
    directorys_revised = []
    while True:
        new_directorys.clear()
        
        for directory in directorys:
            if directory not in directorys_revised:
                if not directory["dirs"]:
                    directorys_revised.append(directory)
                    
                    continue
            
                elif all(sub_directory in directorys_revised for sub_directory in directory["dirs"]):
                    directorys_revised.append(directory)
                    total_weight = sum(sub_directory["weight"] for sub_directory in directory["dirs"])
                    directory["weight"] += total_weight

                    continue
        
                if (directory["dirs"]) and (directory not in new_directorys) and (directory not in directorys_revised):
                    for sub_directory in directory["dirs"]:
                        if (sub_directory not in directorys_revised):
                            new_directorys.append(sub_directory)
        
        for directory in directorys:
            if (directory not in directorys_revised) and (directory not in new_directorys):
                    new_directorys.append(directory)
        
        directorys.clear()
        
        for new_directory in new_directorys:
            directorys.append(new_directory)

        if all(directory in directorys_revised for directory in directorys):
            break

    result = []
    directorys = [base_directory]
    new_directorys = []
    while True:
        for directory in directorys:
            
            if directory["weight"] <= 100000:
                result.append((directory["name"], directory["weight"]))

            for directory in directory["dirs"]: 
                new_directorys.append(directory)

        directorys.clear()

        for new_directory in new_directorys:
            directorys.append(new_directory)

        new_directorys.clear()
        
        if not directorys:
            break
    
    value = 0
    for letter, number in result:
        value += number

# # ==========SECOND PART============
    
with open("/home/catowo/Documentos/IT/Exercises/Advent Of Code 2022/no_space_left_on_device_input.txt", "r+") as f:

    base_directory = {}
    actual_directory = {}

    for line in f:

        command_parts = line.strip().split()
        if command_parts[0] == "$" and command_parts[1] == "cd":

            if command_parts[2] == "/":
                base_directory = {"name": "/",
                                  "parent": None,
                                  "dirs": [],
                                  "files": [],
                                  "weight": 0}

                actual_directory = base_directory
                continue

            if command_parts[2] == "..":
                parent_directory = actual_directory["parent"]

                actual_directory = parent_directory
                continue

            sub_directory = {"name": command_parts[2],
                             "parent": actual_directory,
                             "dirs": [],
                             "files": [],
                             "weight": 0}
            actual_directory["dirs"].append(sub_directory)

            actual_directory = sub_directory

        elif command_parts[0] != "$" and command_parts[0] != "dir":
            actual_directory["files"].append(
                (command_parts[0], command_parts[1]))
            actual_directory["weight"] += int(command_parts[0])

    directorys = [base_directory]
    new_directorys = []
    directorys_revised = []
    while True:
        new_directorys.clear()

        for directory in directorys:
            if directory not in directorys_revised:
                if not directory["dirs"]:
                    directorys_revised.append(directory)

                    continue

                elif all(sub_directory in directorys_revised for sub_directory in directory["dirs"]):
                    directorys_revised.append(directory)
                    total_weight = sum(
                        sub_directory["weight"] for sub_directory in directory["dirs"])
                    directory["weight"] += total_weight

                    continue

                if (directory["dirs"]) and (directory not in new_directorys) and (directory not in directorys_revised):
                    for sub_directory in directory["dirs"]:
                        if (sub_directory not in directorys_revised):
                            new_directorys.append(sub_directory)

        for directory in directorys:
            if (directory not in directorys_revised) and (directory not in new_directorys):
                new_directorys.append(directory)

        directorys.clear()

        for new_directory in new_directorys:
            directorys.append(new_directory)

        if all(directory in directorys_revised for directory in directorys):
            break

    result = []
    directorys = [base_directory]
    new_directorys = []
    
    disk = 70000000
    actualization = 30000000
    
    while directorys:
        for directory in directorys:

            if directory["weight"] >= actualization - (disk - base_directory["weight"]):
                result.append((directory["name"], directory["weight"]))

            for directory in directory["dirs"]:
                new_directorys.append(directory)

        directorys.clear()
        directorys = new_directorys

    print(min(result, key=lambda element: element[1]))
