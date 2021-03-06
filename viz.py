import numpy as np

from lsdo_viz.api import BaseViz, Frame

import seaborn as sns


sns.set()


mode = 'last'


class Viz(BaseViz):

    def setup(self):
        # self.use_latex_fonts()

        self.frame_name_format = 'output_{}'

        self.add_frame(Frame(
            height_in=8., width_in=12.,
            nrows=2, ncols=2,
            wspace=0.4, hspace=0.4,
        ), 1)

    def plot(self, data_dict_list, ind, video=False):
        if ind < 0:
            ind += len(data_dict_list)

        data_dict_list[ind]['alpha']
        data_dict_list[ind]['CL']
        data_dict_list[ind]['CD']

        self.get_frame(1).clear_all_axes()

        with self.get_frame(1)[0, 0] as ax:
            x = np.arange(ind)
            y = [
                data_dict_list[k]['CL'][0]
                for k in range(ind)
            ]
            ax.plot(x, y)
            if video:
                ax.set_xlim([0, len(data_dict_list)])
                ax.set_ylim(self.get_limits(
                    'CL', lower_margin=0.1, upper_margin=0.1, mode=mode,
                ))
            ax.set_xlabel('Iteration')
            ax.set_ylabel('CL')

        with self.get_frame(1)[0, 1] as ax:
            x = np.arange(ind)
            y = [
                data_dict_list[k]['CD'][0]
                for k in range(ind)
            ]
            ax.plot(x, y)
            if video:
                ax.set_xlim([0, len(data_dict_list)])
                ax.set_ylim(self.get_limits(
                    'CD', lower_margin=0.1, upper_margin=0.1, mode=mode,
                ))
            ax.set_xlabel('Iteration')
            ax.set_ylabel('CD')

        with self.get_frame(1)[1, 0] as ax:
            x = np.arange(ind)
            y = [
                data_dict_list[k]['alpha'][0]
                for k in range(ind)
            ]
            ax.plot(x, y)
            if video:
                ax.set_xlim([0, len(data_dict_list)])
                ax.set_ylim(self.get_limits(
                    'alpha', lower_margin=0.1, upper_margin=0.1, mode=mode,
                ))
            ax.set_xlabel('Iteration')
            ax.set_ylabel('alpha')

        with self.get_frame(1)[1, 1] as ax:
            x = [
                data_dict_list[ind]['CD'][0]
            ]
            y = [
                data_dict_list[ind]['CL'][0]
            ]
            ax.plot(x, y, 'o')
            if video:
                ax.set_xlim(self.get_limits(
                    'CD', lower_margin=0.1, upper_margin=0.1, mode=mode,
                ))
                ax.set_ylim(self.get_limits(
                    'CL', lower_margin=0.1, upper_margin=0.1, mode=mode,
                ))
            ax.set_xlabel('CD')
            ax.set_ylabel('CL')

        self.get_frame(1).write()