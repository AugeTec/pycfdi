import os
import unittest

from simple_cfdi import utils as cfdi_utils
from tests.utils import assert_equal_xml


class TestUtils(unittest.TestCase):
    def test_import_export_util(self):
        current_module_path = os.path.dirname(__file__)
        with open(current_module_path + "/fixtures/cfdi_4_0_invoice.xml", "rb") as f:
            fixture = f.read()

        doc = cfdi_utils.import_xml(fixture)
        self.assertTrue(doc)

        xml_data = cfdi_utils.export_xml(doc)
        self.assertTrue(xml_data)

        assert_equal_xml(self, fixture, xml_data.encode('utf-8'))


if __name__ == '__main__':
    unittest.main()
