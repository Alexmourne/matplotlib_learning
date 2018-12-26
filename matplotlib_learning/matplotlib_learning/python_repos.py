import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r= requests.get(url)
print("Status code:", r.status_code)

#
response_dict = r.json()
#print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

#
repo_dicts = response_dict['items']
#print("Repositories returned:", len(repo_dicts))

#
repo_dict = repo_dicts[0]

def investigate_repo(repo_dict):
    print("\nKeys:", len(repo_dict))
    for key in sorted(repo_dict.keys()):
        print(key)
#investigate_repo(repo_dict)

#print("\nSelected information about first repository:")
def print_dict(repo_dict):
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Upload:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
#print_dict(repo_dict)

def print_each_dict(repo_dict, repo_dicts):
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print_dict(repo_dict)
    return repo_dict
#print_each_dict(repo_dict, repo_dicts)

names, stars = [], []
plot_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

#
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

#chart = pygal.Bar(my_style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
#chart.add('', plot_dicts)
chart.render_to_file('images\python_repos.svg')

