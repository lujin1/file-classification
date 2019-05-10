# encoding=utf-8
__author__ = 'lujin'
import os
import shutil

file_dir = "test"
key = "卢进"
copy_dir = "copy" + key
result = []
for maindir, subdir, file_name_list in os.walk(file_dir):
    for filename in file_name_list:
        if key in filename:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            result.append(apath)
print(result)
if result:
    if os.path.exists(copy_dir):
        pass
    else:
        os.mkdir(copy_dir)
        for i in result:
            new_file = copy_dir + "/" + i.split("\\")[-1]
            shutil.copyfile(i, new_file)
else:
    print("没有找到关键字为：'%s' 的相关文件" % key)