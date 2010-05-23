#coding:utf-8
'''
2. Implementar uma função que formate uma lista de tuplas como tabela
HTML.
'''

import unittest

#olhar depois, porque os caras já fizeram isso!
#http://www.decalage.info/python/html

class Table(object):

    def __init__(self, lines, columns, border):
        self.lines = lines
        self.columns = columns
        self.border = str(border)
        self._table = [['empty' for j in xrange(columns)] for i in xrange(lines)]

    def set_value_at_line_column(self, value, line, column):
        try:
            self._table[line][column] = value
        except IndexError:
            print 'Ops! Out of bounder!'

    def parte_html(self):
        html_table = '<table border="%s">' % self.border
        for line in xrange(self.lines):
            html_table += '<tr>'
            for column in xrange(self.columns):
                html_table += '<td>%s</td>' % str(self._table[line][column])
            html_table += '</tr>'
        html_table += '</table>'
        return html_table

class TestTable(unittest.TestCase):

    def test_table_with_2_lines_and_2_columns_and_border_1(self):
        table = Table(2, 2, 1)
        table.set_value_at_line_column('row 1 - cell 1', 0, 0)
        table.set_value_at_line_column('row 1 - cell 2', 0, 1)
        table.set_value_at_line_column('row 2 - cell 1', 1, 0)
        table.set_value_at_line_column('row 2 - cell 2', 1, 1)
        html_table = table.parte_html()
        expected_html = '<table border="1"><tr><td>row 1 - cell 1</td><td>row 1 - cell 2</td></tr>'
        expected_html += '<tr><td>row 2 - cell 1</td><td>row 2 - cell 2</td></tr></table>'
        self.assertEquals(html_table, expected_html)

if __name__ == '__main__':
    unittest.main()
