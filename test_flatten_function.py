import unittest
import json
import os
from util_flatten_function import flatten

class TestFlattenFunction(unittest.TestCase):

    def test_flatten_success(self):
        # Define sample input and expected output
        keys = [
            "attributes.primaryAttributes.skuName",
            "attributes.feedSkuBaseAttributeSet.skuCode",
            "attributes.primaryAttributes.productName",
            "attributes.feedProductBaseAttributeSet.productCode",
            "attributes.primaryAttributes.supplier",
            "attributes.productDescriptiveAttributes.Brand",
            "attributes.primaryAttributes.ean",
            "attributes.FormattedDimensions.BoxDimensions.height",
            "attributes.FormattedDimensions.BoxDimensions.length",
            "attributes.FormattedDimensions.BoxDimensions.quantity",
            "attributes.FormattedDimensions.BoxDimensions.weight",
            "attributes.FormattedDimensions.BoxDimensions.width",
            "attributes.FormattedDimensions.NumberOfBoxes",
            "hierarchicalCategories.lvl0",
            "hierarchicalCategories.lvl1",
            "hierarchicalCategories.lvl2",
            "hierarchicalCategories.lvl3"
        ]
        expected_output = {
            "attributes.primaryAttributes.skuName": "Topaz Cushion Cover 43x43cm Biscuit",
            "attributes.feedSkuBaseAttributeSet.skuCode": "78012363",
            "attributes.primaryAttributes.productName": "Topaz Cushion Cover",
            "attributes.feedProductBaseAttributeSet.productCode": "90033573",
            "attributes.primaryAttributes.supplier": "Fullshire Ltd",
            "attributes.productDescriptiveAttributes.Brand": "Newmaster",
            "attributes.primaryAttributes.ean": "5054077847315",
            "attributes.FormattedDimensions.BoxDimensions.height": 74,
            "attributes.FormattedDimensions.BoxDimensions.length": 224,
            "attributes.FormattedDimensions.BoxDimensions.quantity": 1,
            "attributes.FormattedDimensions.BoxDimensions.weight": 40,
            "attributes.FormattedDimensions.BoxDimensions.width": 192,
            "attributes.FormattedDimensions.NumberOfBoxes": 1,
            "hierarchicalCategories.lvl0": [
                "Home"
            ],
            "hierarchicalCategories.lvl1": [
                "Home "
            ],
            "hierarchicalCategories.lvl2": [
                "Home > All Cushions and Throws",
                "Home > Cushions"
            ],
            "hierarchicalCategories.lvl3": [
                "Home > Cushions > Cushion Covers",
                "Home > Cushions > Cushions Covers Throws Sale"
            ]
        }

        # Define output file path
        self.output_filepath = 'products_flatten.json'

        # Call the flatten function
        success = flatten('products.json', keys, self.output_filepath)

        # Read the output data from the temporary output file
        with open(self.output_filepath, 'r') as f:
            actual_output = json.load(f)

        # Check if the function call was successful
        self.assertTrue(success)

        # Check if the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()