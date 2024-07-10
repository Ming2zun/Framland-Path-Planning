# --------
from famland_traversal import Coordinateself
from path_picture import Pathpicture
import math
import yaml
# 创建坐标转换器对象并进行转换
transformer = Coordinateself()
p_show = Pathpicture
# 定义作业宽度
working_wide = 5

or_points = [(6436.9, 26841.3),(6524.3, 26832.9),(6515.1, 26926.4),(6450.7, 26903.9)]
# or_points = [(6, 6),(176, 5),(187, 74),(14, 75)]

path_list,angel_for_back = transformer.s_rote(or_points,working_wide)
    

yaml_file = '/home/boxing/di_pan_ws/test/x.yaml'
yaml_file_y = '/home/boxing/di_pan_ws/test/y.yaml'
x_values = []
y_values = []
for point in path_list:
    x_values.append(point[0])
    y_values.append(point[1])
# 将x值写入x.yaml文件
with open('/home/boxing/di_pan_ws/test/x.yaml', 'w') as x_file:
    yaml.dump(x_values, x_file)
# 将y值写入y.yaml文件
with open('/home/boxing/di_pan_ws/test/y.yaml', 'w') as y_file:
    yaml.dump(y_values, y_file)

p_show.plot_from_yaml(yaml_file,yaml_file_y,or_points)