#! /bin/python 

def print_file(name):
    with open(name) as file:
        print(file.read())

print_file("tex_src")

