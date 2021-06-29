# 图像超分辨率重建系统演示版本使用说明

本系统基于MSRN，可以实现图片和视频的超分辨率重建

## 1、准备工作

`python3.6`或以上环境

按照`requirement.txt`文件安装所有需要的包

清空`input`和`output`文件夹

安装OpenH264解码器，[下载链接](https://github.com/cisco/openh264/releases)

运行`run.py`文件启动软件，若你是Windows用户可以直接通过运行`run.bat`文件启动

## 2、图片超分辨率重建

首先清空input文件夹，将图片文件复制进input文件夹中

然后设置软件重建模式为图片模式，设置重建参数后点击开始按钮

## 3、视频超分辨率重建

首先清空input文件夹，将视频文件复制进input文件夹中，该系统会依次对每一个视频进行重建

然后设置软件重建模式为视频模式，设置重建参数后点击开始按钮

## 4、获取输出文件

输出文件将被保存在`output`文件夹中

## 注意事项

1、由于图像超分辨率重建较为吃性能，推荐选择显卡进行重建，同时显存最好要超过6GB，否则一些分辨率较高的图片或视频可能无法重建

2、机器内存推荐在8GB以上，若使用cpu进行重建的话推荐内存在16GB以上

3、由于OpenCV和算法的原因，输出图像可能会出现轻微色差，请见谅

4、input文件夹里不要把图片和视频混着放，会报错

5、视频超分辨率重建耗时巨大，请耐心等待