# encoding=utf-8
__author__ = 'lujin'

from appJar import gui
import os
import shutil

def press():
    # print("file_dir:", app.entry("文件目录"), "key:", app.entry("关键字"))
    file_dir = app.entry("文件目录")
    key = app.entry("关键字")
    copy_dir = "copy" + key
    result = []
    for maindir, subdir, file_name_list in os.walk(file_dir):
        for filename in file_name_list:
            if key in filename:
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                result.append(apath)
    # print(result)
    if result:
        if os.path.exists(copy_dir):
            pass
        else:
            os.mkdir(copy_dir)
            for i in result:
                new_file = copy_dir + "/" + i.split("\\")[-1]
                shutil.copyfile(i, new_file)
        new_file_dir = os.getcwd() + "\\" + copy_dir
        message = "关键字为：'%s' 的文件已copy到 %s 下,请查看;\n原文件存在于 %s " %(key, new_file_dir, result)
        app.infoBox("通知", message, parent=None)
    else:
        message = "没有找到关键字为：'%s' 的相关文件" % key
        # print("没有找到关键字为：'%s' 的相关文件" % key)
        app.warningBox("提醒", message, parent=None)

with gui("文件夹分类小工具", "400x200") as app:
    app.label("Just for you   -- jin", bg='blue', fg='orange')
    app.entry("文件目录", label=True, focus=True)
    app.entry("关键字", label=True, focus=True)
    app.buttons(["Submit", "Cancel"], [press, app.stop])
