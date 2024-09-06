from api import app

# 运行应用
if __name__ == '__main__':
    app.run(app.config["HOST"], app.config["PORT"], debug=True)