读写文件就是请求操作系统打开一个文件对象（文件描述符），然后通过操作系统提供的接口从这个文件对象中读写文件。

### 读文件

以读模式打开一个文件
```
>>> r = open("1.log", "r")
```

如果文件不存在，open()函数会抛出一个IOError的错误

```
>>> r = open("2.log", "r")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '2.log'
```
读取内容，关闭文件
```
>>> r.read()
'111111'
>>> r.close()
```

防止文件读写时因为产生IOError，而导致close()未调用。我们可以用try... finally
```
try:
    f = open("1.log", "r")
    try:
        print(f.read())
    except:
        print("文件读写异常")
    finally:
        f.close()
except:
    print('打开文件异常')
```

with open简单写法，等同于try...finally
```
try:
    with open("1.log", "r") as f:
        print(f.read())
except:
    print("打开文件异常")
```

### 写文件

当我们写文件时，系统往往不会立即写入，而是先放到内存里缓存起来，空闲时慢慢写入。只有调用close()方法时，操作系统才能立即写入。为了防止忘记调用close()，所以用with语句比较保险
```
with open("1.log", "w") as f:
    f.write("hello world")
```