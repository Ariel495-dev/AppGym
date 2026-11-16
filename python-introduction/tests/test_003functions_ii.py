import context
import io
import unittest
from contextlib import redirect_stdout
from intro import functions


class MoreFunctionsTestCase(unittest.TestCase):

    def test_more_functions(self):
        with redirect_stdout(io.StringIO()) as f:
            functions.short_print()
        console_output = f.getvalue()

        self.assertTrue(console_output.__contains__("La primera guerra mundial tuvo lugar de 1914 a 1918"))
        self.assertEqual(functions.lucky_number(), 79)


if __name__ == '__main__':
    unittest.main()
