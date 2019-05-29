# labelImg_save_bbox
  Based on the popular label annotation tool labelImg, this repo can help you save the bbox of labled imgs.

# usage
* 1. download [labelImg tool](https://github.com/tzutalin/labelImg)
* 2. make our dateset with the format of imgs.

 * (1)imgs

      In this way, u can directly load the img folder to labelImg.
    
 * (2)video

    * First, run `ffmpeg -i ./CH2_20190127150000_20190127160000.mp4 -vf fps=fps=8/1 -q 0 ./imgs/%06d.jpg`.
      
    * Second, put imgs to labelImg.
    
* 3. get bbox

    run `xml2img.py` script with your xml_path and roi_path.

