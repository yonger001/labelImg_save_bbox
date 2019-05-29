
#encoding:utf-8
import os
import xml.etree.ElementTree as ET
import cv2

## extract frames with 8fps,and save to folder named imgs
## ffmpeg -i ./CH2_20190127150000_20190127160000.mp4 -vf fps=fps=8/1 -q 0 ./imgs/%06d.jpg


def get_roi(xml_file):

    tree_all = ET.ElementTree()
    tree = tree_all.parse(xml_path)    #直接解析xml文件
    #print('tree.tag:', tree.tag)      #tree[0]:获取xml文件的根节点
    #print('len(tree):', len(tree))    

    path = tree.find('path').text
    bbox = tree[6][4]
    xmin = int(bbox.find('xmin').text)
    xmax = int(bbox.find('xmax').text)
    ymin = int(bbox.find('ymin').text)
    ymax = int(bbox.find('ymax').text)
    #print(xmin,xmax,ymin,ymax)

    src_img = cv2.imread(path)
    roi = src_img[ymin:ymax, xmin:xmax,:]

    return roi, path.split('/')[-1]




if __name__ == '__main__':
   
    
    xml_path = "./xml"
    roi_path = "./xml"
    if not os.path.exists(roi_path):
        os.makedirs(roi_path)

    flag_num = 0
    for i in os.listdir(xml_path):
        xml_file = xml_path + '/' + i
        roi,name = get_roi(xml_file)
        #print('xml_file:', xml_file)
        #print('name:', roi_path+'/'+name)
        
        cv2.imwrite(roi_path+'/'+name, roi)
        # cv2.imshow('cop.jpg', roi)
        # cv2.waitKey(0)
        flag_num += 1
        print("Here, have deal with %d imgs."%(flag_num))

print("---- Ending, have save %d imgs.----"%(flag_num))



