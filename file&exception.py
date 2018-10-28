###################从文件中读取数据##################
#####读取整个文件(同级目录)########
with open('pi_digits.txt') as file_object:#open('file_name'),且要打开的文件需要与当前运行的文件在同级目录。open()返回一个表示文件的对象即这里的file_object
    #关键字'with'在不再需要访问文件后将其关闭，不需再去调用close()
    contents=file_object.read()#read()读取该文件的全部内容，该方法会比原内容多返回一个空行，因为read()到达文件末尾时返回一个空字符串，显示出来就是一个空行
    print(contents.rstrip())#rstrip()：删除字符串末尾的空白
##### 读取整个文件(文件路径)########
#with open('text_files/file_name') as file_objiect:#相对文件路径：其中text_file与当前文件在同级目录
#with open('/home/PycharmProjects/untitled/venv/text_files/file_name') as file_objiect:#绝对文件路径：
######逐行读取#######
with open('pi_digits.txt') as file_object8:
    for line in file_object8:#逐行读取文件，用line
        print(line.rstrip())#文件中每行末尾都有一个看不见的换行符，且print也会加上一个换行符，故每行末尾有2个换行符
