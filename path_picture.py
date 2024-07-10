import yaml
import matplotlib.pyplot as plt


class Pathpicture:
    def plot_from_yaml(x_yaml_path, y_yaml_path, or_points):
        # 定义一个内部函数用于读取 YAML 文件中的坐标列表
        def read_yaml_file(yaml_file):
            with open(yaml_file, 'r') as file:
                data = yaml.safe_load(file)
                data = [float(item) for item in data]
            return data

        # 在 or_points 末尾添加它的第一个点
        or_points = or_points + [or_points[0]]

        # 读取 YAML 文件中的 x 和 y 坐标
        x_values = read_yaml_file(x_yaml_path)
        y_values = read_yaml_file(y_yaml_path)

        # 检查 x 和 y 坐标列表长度是否一致
        if len(x_values) != len(y_values):
            raise ValueError("The lengths of x_values and y_values must be the same.")

        # 绘制原始坐标点
        plt.plot(x_values, y_values, '-o', label='Original Points')

        # 绘制额外的 or_points 点
        or_x, or_y = zip(*or_points)  # 解构 or_points 为 x 和 y 值
        plt.plot(or_x, or_y, '-*', label='OR Points')

        plt.xlabel('X values')
        plt.ylabel('Y values')
        plt.title('Connected Coordinate Points')
        plt.legend()
        plt.grid(True)
        plt.show()

# 使用示例
