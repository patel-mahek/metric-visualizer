# -*- coding: utf-8 -*-
# file: example.py
# time: 05/02/2022
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.
import os
import random
from metric_visualizer.core import MetricVisualizer
import numpy as np

MV = MetricVisualizer(name="example", trial_tag="Model")

repeat = 100  # number of repeats
metric_num = 2  # number of metrics

#  利用metric_visualizer监听实验吧并保存实验结果，随时重新绘制图像
# trial_names = ["LSTM", "CNN", "BERT"]  # fake trial names
trial_names = ['NSGA-II', 'NSGA-III', 'MOEA/D']  # fake trial names
# trial_names = ['Hyperparameter Setting 1', 'Hyperparameter Setting 2', 'Hyperparameter Setting 3']  # fake trial names
for r in range(repeat):  # repeat the experiments to plot violin or box figure
    metrics = [
        (np.random.random() + n + (1 if random.random() > 0.5 else -1))
        for n in range(metric_num)
    ]  # n is metric scale factor
    for n_trial in range(len(trial_names)):

        for i, m in enumerate(metrics):
            MV.log_metric(
                trial_name="Trial-{}".format(n_trial),
                metric_name="metric{}".format(i + 1),
                value=m + random.random(),
            )  # add metric by custom name and value

MV.remove_outliers()  # remove outliers

MV.summary()
tikz_file_path = MV.box_plot(
    by="trial",
    engine="tikz",
    show=True,
    save_path=os.getcwd() + "/box_plot_by_trial.tex",
)

from metric_visualizer.colalab import reformat_tikz_format_for_colalab

style_settings = {
    'xtick': {0, 1, 2}
}
reformat_tikz_format_for_colalab(
    template='delta_hv.tex',
    tex_src_to_format=tikz_file_path,
    output_path=tikz_file_path,
    style_settings=style_settings,
)

# MV.compile_tikz(crop=True, clean=True)
