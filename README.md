#README#

##采花大道数据同步工具##

###配置系统###
1.所有的配置文件在conf/config.py中
OldDB节点配置旧数据库地址
newDB配置新数据库地址

2.确保运行的系统上面安装了:
python2.7
(以下类库可以通过pip安装等)
peewee
PyMySQL
request
tornado


###运行系统###
python chdd/core/DBCopy.py