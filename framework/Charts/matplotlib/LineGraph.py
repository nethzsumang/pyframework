import matplotlib.pyplot as plt


class LineGraph:
    """
        (list) X Values for Chart
    """
    a_x_values = None

    """
        (list) Y Values for Chart
    """
    a_y_values = None

    """
        (string) Title for the Chart
    """
    s_title = ""

    """
        (string) Label for X axis
    """
    s_x_label = ""

    """
        (string) Label for Y axis
    """
    s_y_label = ""

    """
        Counter for graph
    """
    counter = 1

    """
        (dict) Properties for chart
    """
    props = {
        "linestyle": "--",
        "colors": ["b", "g", "r", "c", "m", "y"],
        "marker": "o",
        "legend_loc": "upper left",
        "pause_time": 0.01,
        "bbox_to_anchor": (0.5, -0.5),
        "fancybox": True,
        "shadow": True,
        "ncol": 5,
    }

    def __init__(self, title=""):
        """
            LineGraph constructor
            :param title:
        """
        self.s_title = title

    def set_props(self, a_props):
        """
            Sets properties
            :param a_props:
            :return:
        """
        for s_name, s_val in a_props.items():
            if s_name not in self.props:
                continue

            self.props[s_name] = s_val

    def set_values(self, a_x_values, a_y_values, s_x_label="", s_y_label=""):
        """
            Set chart's values
            :param a_x_values:
            :param a_y_values:
            :param s_x_label:
            :param s_y_label:
            :return:
        """
        self.a_x_values = a_x_values
        self.a_y_values = a_y_values
        self.s_x_label = s_x_label
        self.s_y_label = s_y_label

    def plot(self, a_legend=None, s_title="Untitled"):
        """
            Plots the value in the charts
            :param a_legend:
            :param s_title:
            :return:
        """
        i_counter = 0
        plt.subplot(1, 2, self.counter)
        self.counter += 1
        for y_values in self.a_y_values:
            plt.plot(
                self.a_x_values,
                y_values,
                color=self.props["colors"][i_counter],
                marker=self.props["marker"],
            )
            plt.title(s_title)
            i_counter += 1

        plt.xlabel(self.s_x_label)
        plt.ylabel(self.s_y_label)

        if a_legend is not None:
            plt.legend(
                a_legend,
                loc=self.props["legend_loc"],
                bbox_to_anchor=self.props["bbox_to_anchor"],
                fancybox=self.props["fancybox"],
                shadow=self.props["shadow"],
                ncol=self.props["ncol"],
            )

    def show(self):
        """
            Show the chart
            :return:
        """
        self.counter = 0
        plt.show()
