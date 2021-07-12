# cvc-xls-generator
It takes json file which is generad by dependency check tool as input and conver it into xlsx file.

## Installation
```pip install cvc-xls-generator```

## How to use it
```
from cvc-xls-generator import GenerateXls
json_report="path to Json File" #eg D:\\dir\\dependency-check.json
output_report="Path to output file" #eg D:\\dir\\dependency-check-report-project-version.xlsx

gx = GenerateXls(
    json_report=json_report,
    output_report=output_report
)

gx.makeXL()

```

## License

Copyright (c) 2021 Devaraju Garigapati

This repository is licensed under the MIT license.
See LICENSE for details.