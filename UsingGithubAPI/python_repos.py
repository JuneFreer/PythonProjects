import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中, 是一个JSON格式的文件
response_dict = r.json()
print("Total repositories:", response_dict['total_count']) # GitHub总共包含多少个Python仓库

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts)) # 获悉我们获得了多少个仓库的信息

# 研究第一个仓库
repo_dict = repo_dicts[0] # 提取repo_dicts中的第一个字典（第一个仓库）
print("\nKeys:", len(repo_dict)) # 看看第一个仓库中有多少信息
# for key in sorted(repo_dict.keys()): # 我们打印这个字典的所有键，看看其中包含哪些信息
#     print(key)

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.label_font_size = 14
# my_config.major_label_font_size = 18
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000
#
#
# chart = pygal.Bar(my_config, style=my_style) # 创建条形图对象
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

# 字典列表
plot_dicts = [
    {'value': 45709, 'label': 'Description of httpie.'},
    {'value': 47044, 'label': 'Description of django.'},
    {'value': 48752, 'label': 'Description of flask.'},
]


chart.add('', plot_dicts) # 向add()传递一个字典列表，而不是值列表
chart.render_to_file('bar_descriptions.svg')

# 处理结果
print(response_dict.keys())
