#reads lines into array. they can be formatted into csv format from here as well
def file_read(items, lines_array):
    for item in items:
        for line in item:
            if var1 in line: #change var1 to specifics
                lines_array.append(','join(line.split()) #if outputing to .csv
                lines_array.append(line) #if just saving strings
    #lines_array.append(line) if var1 in line for line in item for item in items

#put info to a file
def comile_info(info, output_file):
    with open(output_file, 'w') as w:
        sys.stdout = w
        for line in info:
            print(line) #for line in info: #change to look for specifics if need be

#clean data for unwanted lines
def clean_data(lines_array, bad_data):
    for x in bad_data:
        for y in lines_array:
            if x in y:
                lines_array.remove(y)

#prompt for directory with wanted data
def get_directory(base_dir, items):
    results = input("Which files are to be read? ")
    results = base_dir + results
    os.chdir(results)
    files = os.listdir(results)
    items.append(item) for item in files


base_dir = "\change\to\wanted\directory\" #change to directory to start in
lines_array, items, bad_data - [], [], []
