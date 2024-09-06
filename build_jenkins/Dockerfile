# 使用官方 Python 镜像作为基础镜像
FROM python:3.11.9

# 设置工作目录
WORKDIR /Next_Component

# 复制当前目录下的所有文件到工作目录
COPY . /Next_Component

# 安装应用程序依
RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install numpy==1.26.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install flask==3.0.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu
# 暴露应用程序需要的端口
EXPOSE 8050

# 定义容器启动时运行的命令
CMD ["python", "main.py"]