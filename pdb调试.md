pdb调试

```
python3 -m pdb test1.py
```
> pdb调试命令

命令 | 简写 | 说明
---|---|---
list | l | 显示当前代码
next | n | 向下执行一条代码
continue | c | 继续执行代码
break | b | 添加断点
clear | - | 删除断点
step | s | 进入函数
print | p | 打印变量的值
args | a |  打印所有传入的参数
return | r | 执行代码知道从当前函数返回
quit | q | 退出调试
回车 | - | 重复执行上一条命令
bt  | - | 查看函数调用栈