# 安装 build 工具
pip install build
# 打包项目
python -m build
# 安装 twine
pip install twine
# 上传包
twine upload dist/*    