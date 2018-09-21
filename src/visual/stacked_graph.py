import math


class StackedGraph:

    TICK = '▇'
    SEPARATOR = '-'

    def __init__(self, record_labels, record_values, graph_title):
        self._record_labels = record_labels
        self._record_values = record_values
        self._scaled_values = [value*100 for value in record_values]
        self._graph_title = graph_title
        self._set_scale()
        self._set_width()

    def _set_scale(self):
        """
        Identifies the scale of the graph
        Meaning, how much is the value of one block, self.TICK
        """
        min_value = int(min(self._record_values))
        # Get the floor value of the nearest power of 10
        scale = math.pow(10, math.floor(math.log10(min_value)))
        self._scale = scale

    def _set_width(self):
        """
        Sets the approximate width of the graph
        """
        if self._record_values is None or len(self._record_values) == 0:
            self._width = 0
        else:
            max_value = max(self._record_values)
            len_graph = self._get_num_units(max_value)
            self._width = len_graph

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

    def _get_single_horizontal_line_graph(self, label, value):
        """
        Build a string representation of a row
        :param label: label of the row
        :param value: value of the row
        :return: String representation of a row
        """
        line = list()
        # the label
        line.append(str(label))

        # the blocks in the line
        large_units = self._get_num_units(value)
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
        for label, value in zip(self._record_labels, self._record_values):
            single_line = self._get_single_horizontal_line_graph(label, value)
            graph.append(single_line)

        # Bring everything together
        return '\n'.join(graph)
