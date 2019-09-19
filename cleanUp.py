import os, os.path, re


def filter_filenames(dirpath, predicate):
    for item in os.listdir(dirpath):
        if predicate(item):
            f = open(item,"r")
            data = f.read()
            rows = data.split("\n")
            for row in rows:
                split_row = row.split(" ")
                for ele in split_row:
                    if ele == "Name:":
                        print(split_row)
                        for py_file in os.listdir(dirpath):
                            if re.compile(item[:-3] + '.*' ).match(py_file):
                                os.rename(py_file, split_row[1] + '_' + split_row[2] + py_file[len(item)-4:] )
                    

filter_filenames('.',re.compile(r'.*\.txt').match)