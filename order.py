import os
path_name='/home/why/Documents/SLAM_dateset/kalibr_bag/m_stereo/R'
i=0
for item in os.listdir(path_name):
	os.rename(os.path.join(path_name,item),os.path.join(path_name,('R' + str(i) + '.ppm')))
	i+=1
