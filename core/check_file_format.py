import os

video_format_list = ["avi", "mov", "rmvb", "rm", "flv", "mp4", "3gp", "mkv"]
picture_format_list = ["bmp", "jpg", "jpeg", "png", "tif", "gif", "pcx", "tga", "exif", "fpx", "svg", "psd", "cdr", "pcd", "dxf",  "raw"]

def check_file_format(folder):
    is_video = False
    is_picture = False
    format_list = os.listdir(folder)
    for f in video_format_list:
        for file_name in format_list:
            if f in file_name:
                is_video = True
    for f in picture_format_list:
        for file_name in format_list:
            if f in file_name:
                is_picture = True
    if is_picture and is_video:
        print("请不要把图片和视频混着放!")
        return -1
    if is_video:
        return 1
    if is_picture:
        return 0