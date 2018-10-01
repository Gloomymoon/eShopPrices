import random

from flask import render_template
#from pyecharts import Scatter3D

from . import main

REMOTE_HOST = "https://pyecharts.github.io/assets/js"



@main.route('/')
def index():
    return render_template('index.html')

'''
@main.route('/charts')
def pyecharts():
    s3d = scatter3d()
    return render_template('pyecharts.html',
                           myechart=s3d.render_embed(),
                           host=REMOTE_HOST,
                           script_list=s3d.get_js_dependencies())
'''

@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

'''
def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D


def generate_3d_random_point():
    return [random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)]
'''