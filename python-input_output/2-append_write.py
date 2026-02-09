#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, 'a') as file:
        file_len = file.write(text)
        return file_len
