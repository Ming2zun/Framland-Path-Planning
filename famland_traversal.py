import math

class Coordinateself:
#--------------------------------------------------------------------------
# 坐标转换函数

    def transform(self, points):
        """
        将给定的4个坐标点进行坐标系转换
        参数:
        points (list): 包含4个坐标点的列表, 例如 [(3,6),(18,5),(19,28),(4,25)]
        返回:
        list: 转换后的4个坐标点
        """
        # 新坐标系的前2个点
        distance = ((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)**0.5
        new_points = [(0,0), (distance, 0)]
        # 先进行平移
        b = []
        for point in points:
            b.append((point[0] - points[0][0], point[1] - points[0][1]))
        # 计算旋转角度
        theta = -math.atan2(points[1][1] - points[0][1], points[1][0] - points[0][0])     
        # 进行旋转
        c = []
        for point in b:
            c.append((
                point[0] * math.cos(theta) - point[1] * math.sin(theta) + new_points[0][0],
                point[0] * math.sin(theta) + point[1] * math.cos(theta) + new_points[0][1]
            ))
        return c ,theta
#--------------------------------------------------------------------------
# 回转函数，再转换回来
    def back_transform(self,points, angle):
        """
        将给定的坐标点列表绕原点旋转一定角度
        参数:
        points (list): 包含坐标点的列表
        angle (float): 旋转角度，单位为弧度
        返回:
        list: 旋转后的坐标点列表
        """
        rotated_points = []
        for point in points:
            # 计算旋转后的坐标点
            x = point[0] * math.cos(angle) - point[1] * math.sin(angle)
            y = point[0] * math.sin(angle) + point[1] * math.cos(angle)
            rotated_points.append((x, y))
        return rotated_points
#--------------------------------------------------------------------------
# 更具坐标生成直线方程函数
    @staticmethod
    def calculate_slope_intercept(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if x1 == x2:
            slope = float('inf')  # 斜率为无穷大表示垂直于x轴的直线
            intercept = x1  # 在垂直于x轴的直线上，intercept就是x轴的值
        else:
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
        return slope, intercept

    def calculate_line_equations(self, points):
        line_equations = []
        for i in range(len(points) - 1):
            line_equations.append(self.calculate_slope_intercept(points[i], points[i + 1]))
        line_equations.append(self.calculate_slope_intercept(points[-1], points[0]))
        return line_equations
#--------------------------------------------------------------------------
# 选择方程求x点函数
    def calculate_x_coordinate(self,slope, intercept, known_y):
        x = (known_y - intercept) / slope
        return x
#--------------------------------------------------------------------------
# 选择方程求y点函数
    def calculate_y_coordinate(self,slope, intercept, known_x):
        y = slope * known_x + intercept
        return y

#--------------------------------------------------------------------------
    def move_horizontally(self,line_equations, with_co, y_plass, limit3,limit4):
    # 计算线性方程
        line_equation =self.small_quad(line_equations, with_co)
        l2 = line_equation[1]
        l3 = line_equation[2]
        l4 = line_equation[3]
        x2_list, x3_list, x4_list = [], [], []
        
        if limit3 < limit4:
            while (y_plass) < limit4:
                x_4 = self.calculate_x_coordinate(l4[0], l4[1], y_plass)
                if y_plass < limit3 and y_plass < limit4:
                    x_2 = self.calculate_x_coordinate(l2[0], l2[1], y_plass)
                    x2_list.append((x_2,y_plass))
                    
                else:
                    x_3 = self.calculate_x_coordinate(l3[0], l3[1], y_plass)
                    if x_3>=x_4: 
                        x3_list.append((x_3,y_plass))
                    else:
                        x3_list.append((x_4,y_plass))
                        x4_list.append((x_4,y_plass))
                        break
                x4_list.append((x_4,y_plass))
                y_plass += with_co
        else:
            while (y_plass) < limit3:
                x_2 = self.calculate_x_coordinate(l2[0], l2[1], y_plass)
                if y_plass < limit4 and y_plass < limit3:
                    
                    x_4 = self.calculate_x_coordinate(l4[0], l4[1], y_plass)
                    x4_list.append((x_4,y_plass))
                else:
                    x_3 = self.calculate_x_coordinate(l3[0], l3[1], y_plass)
                    if x_3<=x_2: 
                        x3_list.append((x_3,y_plass))
                    else:
                        x3_list.append((x_2,y_plass))
                        x2_list.append((x_2,y_plass))
                        break
                
                x2_list.append((x_2,y_plass))
                y_plass += with_co

        return  x2_list, x3_list, x4_list
#--------------------------------------------------------------------------
    def small_quad(self,line_equations, with_co):
        # 返回一个小四边形
        l2 = line_equations[1]
        l3 = line_equations[2]
        l4 = line_equations[3]
        #  x 轴的夹角（弧度）
        angle_2 = math.atan(l2[0])
        angle_3 = math.atan(l3[0])
        angle_4 = math.atan(l4[0])
        # 计算移动距离
        # move_2 = abs(with_co / math.sin(angle_2))
        # move_3 = abs(with_co / math.sin(angle_3))
        # move_4 = abs(with_co / math.sin(angle_4))

        y_1 = with_co
        # y_2 = move_2/l2[0]
        if l2[0] < 0:
            y_2 = -abs(with_co/math.cos(angle_2))
        else:
            y_2 = abs(with_co/math.cos(angle_2))
        y_3 = -abs(with_co/math.cos(angle_3))
        if l4[0] <0:
            y_4 = abs(with_co/math.cos(angle_4))
        else:
            y_4 = -abs(with_co/math.cos(angle_4))
        
        y_list = [y_1,y_2,y_3,y_4]

        line_equ_new =  [(x, y + y_list[i]) for i, (x, y) in enumerate(line_equations)]
        return line_equ_new
#--------------------------------------------------------------------------
    # 计算了两条直线的交点
    def find_Xpoint(self,line1, line2):
        m1, b1 = line1
        m2, b2 = line2
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        return (x, y)


    def intersection_points(self,line_equations,with_co):
#计算4条线的交点
        def intersection_point(m1, b1, m2, b2):
            # 计算交点的x坐标
            x = (b2 - b1) / (m1 - m2)
            # 使用任何一条线的方程来计算交点的y坐标
            y = m1 * x + b1
            return x, y

        # 存储交点的列表
        b = []
        for i in range(len(line_equations) - 1):
            m1, b1 = line_equations[i]
            m2, b2 = line_equations[i + 1]
            intersection = intersection_point(m1, b1, m2, b2)
            b.append(intersection)
        
        # 计算最后一条线与第一条线的交点
        m1, b1 = line_equations[-1]
        m2, b2 = line_equations[0]
        intersection = intersection_point(m1, b1, m2, b2)
        b.append(intersection)
        c=(b[3][0]+with_co / math.sin(math.atan(line_equations[3][0])),b[3][1])
        b.reverse()
        b.append(c)
        return b
    
    def loop (self,line_equations,with_co):
        #遍历回环收割路径，直到完成作业宽度
        c=[]
        a=0
        while a<20:
            equ_i = self.small_quad(line_equations,with_co)
            b=self.intersection_points(equ_i,with_co)
            if (b[3][0]-b[0][0])<=with_co and (b[2][0]-b[1][0])<with_co:
                a=100
            else:
                if (b[1][1]-b[0][1])<with_co and (b[2][1]-b[3][1])<with_co:
                    a=100
                else:
                    a=0
                    line_equations = equ_i
                c=c+b
        return c
    
    def complete_path(self,list_a, list_b):
        # 传入2个列表生成一个s 型路径
        new_list = []
        new_list.append(list_a[0])
        for i in range(1, len(list_a), 2):
            new_list.extend(list_b[i-1:i+1])
            new_list.extend(list_a[i:i+2])
        if len(list_a) % 2 == 1:
            new_list.append(list_b[-1])
        return new_list


# 直接生成s型路径--------------------------------------------------------------------------------------
    def s_rote(self,or_points,working_wide):
        with_co = working_wide
        y_plass = working_wide
        points,angel_for_back = self.transform(or_points)
        line_equations = self.calculate_line_equations(points)
        limit3y = points[2][1]
        limit4y = points[3][1]
        x2_list, x3_list, x4_list = self.move_horizontally(line_equations, with_co, y_plass, limit3y,limit4y)
        # # 获取每个列表的长度
        len_list2 = len(x2_list)
        len_list4 = len(x4_list)
        if len_list4 > len_list2 :
            list_he = x2_list + x3_list
            list_max = x4_list
        else:
            list_he = x4_list + x3_list
            list_max = x2_list
        list5 = self.complete_path(list_max, list_he)
        dx = float(or_points[0][0] )
        dy = float(or_points[0][1] ) 
        # 使用列表推导式来更新列表a中的点
        po = self.back_transform(list5, -angel_for_back)
        path_list  = [(ax + dx, ay + dy) for ax, ay in po ]
        return path_list,angel_for_back
# 直接生成s型路径--------------------------------------------------------------------------------------


# 直接生成o型路径------------------------------------------------------------------------------------
    def o_rote(self,or_points,with_co):
        points,angel_for_back = self.transform(or_points)

        line_equations = self.calculate_line_equations(points)

        p =self.loop (line_equations,with_co)
        dx = float(or_points[0][0] )
        dy = float(or_points[0][1] ) 

        po = self.back_transform(p, -angel_for_back)
        path_list  = [(ax + dx, ay + dy) for ax, ay in po ]
        return path_list 
# 直接生成o型路径------------------------------------------------------------------------------------

