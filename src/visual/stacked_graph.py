import math
from typing import List, Type


class StackedGraph:

    TICK = '▇'
    SEPARATOR = '-'

    def __init__(self, record_labels: List, record_values: List, graph_title: str):
        self._record_labels = record_labels
        self._record_values = record_values
        self._scaled_values = [int(value*100) for value in record_values]
        self._graph_title = graph_title
        self._scale = self._get_scale()
        self._width = self._get_width()

    def _get_scale(self):
        """
        Identifies the scale of the graph
        Meaning, how much is the value of one block, self.TICK
        """
        non_zero_records = [record for record in self._scaled_values if record > 0]
        min_value = min(non_zero_records)
        # Get the floor value of the nearest power of 10
        scale = math.pow(10, math.floor(math.log10(min_value)))
        return scale

    def _get_width(self):
        """
        Sets the approximate width of the graph
        """
        return len(self._graph_title)

    def _get_num_units(self, value):
        """
        Returns the number of units of self.TICK needed for a given value
        :param value:
        :return: the number of units
        """
        large_units = value/self._scale
        return int(large_units)

    def _get_horizontal_line(self):
        """
        Horizontal line as per the width of the graph
        :return: String representation of a horizontal line
        """
        line = [self.SEPARATOR] * self._width
        return ''.join(line)

    def _get_single_horizontal_line_graph(self, label: str, value: float, scaled_value: int):
        """
        Build a string representation of a row
        :return:
        :param scaled_value: the value on which the scale is built
        :param label: label of the row
        :param value: value of the row
        :return: String representation of a row
        """
        line = list()
        # the label
        line.append(str(label))

        # the blocks in the line
        large_units = self._get_num_units(scaled_value)
        line_graph_elements = [self.TICK] * large_units
        line_graph = ''.join(line_graph_elements)
        line.append(line_graph)

        # the value at the end of the line
        line.append(str(value))

        return ' '.join(line)

    def __str__(self):
        """
        Creates a string representation of the data in this object. It follows the structure
        - horizontal line
        - title of the graph
        - horizontal line
        - for each value
            - record label, blocks for the value, value
        ex:
        ----------
        title
        ----------
        2017-18 ▇▇▇▇▇▇ 6.7
        2018-19 ▇▇▇▇▇▇▇▇ 8.6
        2019-20 ▇▇▇▇▇▇▇▇▇ 9.9
        2020-21 ▇▇▇▇▇▇▇▇▇▇ 10
        :return: The string representation of a graph
        """
        graph = list()
        # Start with a line on top
        graph.append(self._get_horizontal_line())

        # Title of the graph if it exists
        if self._graph_title:
            graph.append(self._graph_title)
            graph.append(self._get_horizontal_line())

        # A row for each value
        for label, value, scaled_value in zip(self._record_labels, self._record_values, self._scaled_values):
            single_line = self._get_single_horizontal_line_graph(label, value, scaled_value)
            graph.append(single_line)

        # Bring everything together
        return '\n'.join(graph)


def build_stacked_graph(labels: List, values: List, title: str) -> Type[StackedGraph]:
    """
    Returns an instance of stacked graph
    :param labels: labels for each row
    :param values: values for each row
    :param title: the tile of the graph
    :return: StackedGraph
    """
    return StackedGraph(labels, values, title)
