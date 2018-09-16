from beautifultable import BeautifulTable


def build_tables_from_json(columns, data):
    """
    Builds a table string for given header and contents
    :param columns: The table header as a list
    :param data: The contents as a list of dicts
    :return: The string representation of a table
    """
    table = BeautifulTable()
    table.column_headers = columns

    for entry in data:
        row = []
        for column in columns:
            value = entry[column]
            row.append(value)
        table.append_row(row)

    return table

