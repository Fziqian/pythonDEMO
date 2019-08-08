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
### 安装mysqlclient
```
# python3.x直接使用
pip install mysqlclient
# python2.x使用wheel
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
pip install wheel xxx.wheel
# 然后在setting.py里配置好数据库
```

### 添加模块
```
python manage.py startapp xxmodel #生成模块
python manage.py migrate #初始化数据库构建表结果
python manage.py migrations xxmodel #生成自定义模块的migration
python manage.py migrate xxmodel #将模块迁移到数据库中，生成对应的表结构

```