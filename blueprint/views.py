from blueprint import app

# 1. 首先要导入蓝图实例
from blueprint.blueprints.home import home_bp
# 2. 然后在程序实例(APP)中注册蓝图
app.register_blueprint(home_bp)

@app.route('/')
def home():
    return "Hello!"