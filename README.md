Django学习
----------------

### 使用virtualenv进行python包管理
这里是用的`python2.7`所以需要安装`virtualenv`

`virtualenv`在使用过程中还能指定python版本
```
pip install virtualenv
virtualenv venv
\venv\scripts\activate
```
### 模块迁移

生成requirements.txt记录环境中安装的模块
```
#生成包管理文件
pip freeze > requirements.txt
#根据包管理安装依赖包 注意迁移的时候使用virtualenv虚拟环境
pip install -r requirements.txt
```

### 安装并启动Django
```
pip install django
django-admin startproject DjangoDEMO
cd DjangoDEMO
python manage.py runserver

```