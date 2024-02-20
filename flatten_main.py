from util_flatten_function import flatten

# Parameters
json_filepath = 'products.json'

keys = ["attributes.primaryAttributes.skuName",
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
"hierarchicalCategories.lvl3"]

output_filepath = 'products_flatten.json'

if __name__ == '__main__':
    success = flatten(json_filepath, keys, output_filepath)
    if success:
        print("Flattening successful!")
    else:
        print("Flattening failed.")