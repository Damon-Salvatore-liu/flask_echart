from flask_cors import *
from flask import Flask, render_template, request, Response, redirect, url_for
import json
app = Flask(__name__)

# 进入页面


@app.route('/pie-nest')
def index():
    return render_template('pie-nest.html')


@app.route('/pie_nest_data')
def pie_nest_data():
    data_list = {}
    data1 = ['公众号：Python研究者', '直达', '营销广告', '搜索引擎',
             '邮件营销', '联盟广告', '视频广告', '百度', '谷歌', '必应', '其他']
    data_list['data1'] = data1
    data2 = [
        {'value': 2000, 'name': 'Python研究者', 'selected': True},
        {'value': 1548, 'name': '搜索引擎'},
        {'value': 775, 'name': '直达'},
        {'value': 679, 'name': '营销广告'}
    ]
    data_list['data2'] = data2
    data3 = [
        {'value': 1048, 'name': '百度'},
        {'value': 335, 'name': '直达'},
        {'value': 310, 'name': '邮件营销'},
        {'value': 251, 'name': '谷歌'},
        {'value': 234, 'name': '联盟广告'},
        {'value': 147, 'name': '必应'},
        {'value': 135, 'name': '视频广告'},
        {'value': 102, 'name': '其他'}
    ]
    data_list['data3'] = data3
    return Response(json.dumps(data_list), mimetype='application/json')


# if __name__ == '__main__':
#     """初始化，debug=True开启调试模式"""
#     app.run(host='127.0.0.1', port=5000, debug=True)
