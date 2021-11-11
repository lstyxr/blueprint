'''
前端蓝图模块
一个蓝图一个模块文件，
也可以单独为文件夹包（package）来管理，在构造文件 init 中创建蓝图实例
'''

from flask import Blueprint

# 实例时指定 前缀
home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
def home():
    return "这是家！"

@home_bp.route('/hi')
def hi():
    return "别来无恙！"