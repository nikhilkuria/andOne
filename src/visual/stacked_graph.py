import math


class StackedGraph:

    TICK = '▇'
    SM_TICK = '▏'
    SEPARATOR = '-'

    def __init__(self, record_labels, record_values, graph_title):
        self._record_labels = record_labels
        self._record_values = record_values
        self._graph_title = graph_title

    def _get_num_units(self, value):
        integer_value = int(value)
        unit_value = math.pow(10, math.floor(math.log10(integer_value)))
        large_units = integer_value/unit_value
        return int(large_units)

    def _get_width(self):
        if self._record_values is None or len(self._record_values) == 0:
            return 0
        max_value = max(self._record_values)
        len_graph = self._get_num_units(max_value)
        return len_graph

    def _get_horizontal_line(self):
        line = [self.SEPARATOR for i in range(self._get_width())]
        return ''.join(line)

    def _get_single_horizontal_line_graph(self, label, value):
        line = list()
        line.append(str(label))

        graph_units = self._get_num_units(value)
        line_graph = ''.join([self.TICK for i in range(graph_units)])

        line.append(line_graph)

        line.append(str(value))

        return ' '.join(line)

    def __str__(self):
        graph = list()
        # Start with a line on top
        graph.append(self._get_horizontal_line())
        for label, value in zip(self._record_labels, self._record_values):
            single_line = self._get_single_horizontal_line_graph(label, value)
            graph.append(single_line)
        return '\n'.join(graph)
