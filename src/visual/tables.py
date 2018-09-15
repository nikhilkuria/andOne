from beautifultable import BeautifulTable


def build_tables_from_json(columns, data):
    table = BeautifulTable()
    table.column_headers = columns
    for entry in data:
        row = []
        for column in columns:
            value = entry[column]
            row.append(value)
        table.append_row(row)
    return table

