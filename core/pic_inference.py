import torch
import numpy
import cv2
import os
from .pic_dataset import picture_read
from .model import MSRN
from .br import get_flag

def pic_SR(picFolder, scale, device, formats):
    net = MSRN(scale)
    para = torch.load('./core/parafile/x' + str(scale) + '.pth', map_location=torch.device(device))
    net.load_state_dict(para)
    device = torch.device(device)
    net = net.to(device)
    torch.set_grad_enabled(False)
    torch.no_grad()
    net.eval()
    data_num = picture_read(picFolder).__len__()
    print("一共有"+ str(data_num) + "张图片")
    for i in range(data_num):
        print("正在处理第" + str(i+1) +"张图片", end='\t')
        img , name = picture_read(picFolder).__getitem__(i)
        img = img / 255.
        img = img.to(device)
        img_SR = net(img)
        img_SR = img_SR.permute(0,2,3,1)
        img_SR = numpy.squeeze(img_SR,0).cpu()
        img_SR = numpy.array(img_SR)
        img_SR = img_SR * 255.
        out_name = name.replace('input','output')
        out_name, _ = os.path.splitext(out_name)    #去除后缀名
        out_name = out_name + '.' + formats
        cv2.imencode('.'+formats, img_SR)[1].tofile(out_name)    #防止中文名乱码
        if get_flag() == True:
            break
        print("完成！")
        torch.cuda.empty_cache()