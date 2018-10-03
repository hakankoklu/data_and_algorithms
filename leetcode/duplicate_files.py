"""
Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Note:
No order is required for the final output.
You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
The number of files given is in the range of [1,20000].
You may assume no files or directories share the same name in the same directory.
You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.
Follow-up beyond contest:
Imagine you are given a real file system, how will you search files? DFS or BFS?
If the file content is very large (GB level), how will you modify your solution?
If you can only read the file by 1kb each time, how will you modify your solution?
What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
How to make sure the duplicated files you find are not false positive?

Example 1:
Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
"""
import os
from pprint import pprint


class Directory:

    def __init__(self, path):
        self.path = path
        self.sub_directories, self.files = self.get_contents()

    def get_contents(self):
        sub_dirs = []
        files = []
        for sub_path in os.listdir(self.path):
            full_path = os.path.join(self.path, sub_path)
            if os.path.isdir(full_path):
                sub_dirs.append(full_path)
            else:
                files.append(full_path)
        return sub_dirs, files


class File:

    def __init__(self, folder, name, content):
        self.folder = folder
        self.name = name
        self.content = content
        self.path = self.folder + '/' + self.name

    def equals(self, other):
        return self.content == other.content


def get_files_from_path(s):
    arr = s.split()
    folder = arr[0]
    files = []
    for file in arr[1:]:
        file.rstrip(')')
        name, content = file.split('(')
        new_file = File(folder, name, content)
        files.append(new_file)
    return files


def find_duplicates(paths):
    all_files = []
    for path in paths:
        all_files.extend(get_files_from_path(path))
    content_map = {}
    for file in all_files:
        if file.content in content_map:
            content_map[file.content].append(file.path)
        else:
            content_map[file.content] = [file.path]
    return [x for x in content_map.values()
            if len(x) > 1]


def get_all_files(root_path):
    all_files = []
    directory = Directory(root_path)
    all_files.extend(directory.files)
    for sub_path in directory.sub_directories:
        all_files.extend(get_all_files(sub_path))
    return all_files


def get_all_files2(root_path):
    all_files = []
    for directory, _, files in os.walk(root_path):
        for file in files:
            all_files.append(os.path.join(directory, file))
    return all_files


def find_size_duplicates(root_path):
    files = get_all_files(root_path)
    size_map = {}
    for file in files:
        size = os.path.getsize(file)
        if size in size_map:
            size_map[size].append(file)
        else:
            size_map[size] = [file]
    return [x for x in size_map.values() if len(x) > 1]





if __name__ == '__main__':
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    output = find_duplicates(paths)
    # [["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]]
    print(output)
    pprint(find_size_duplicates('/home/hakan/Projects/data_and_algorithms/ctci'))