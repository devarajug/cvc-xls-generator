# cvc-xls-generator
It takes json file which is generad by dependency check tool as input and conver it into xlsx file.

## Installation
```pip install cvc-xls-generator```

## How to use it
```
from cvc_xls_generator.xls_creator import GenerateXls

json_file="path to Json File" #eg D:\\dir\\dependency-check.json
output_file="Path to output file" #eg D:\\dir\\dependency-check-report-project-version.xlsx
comments_file = "Path to comments file" #eg D:\\dir\\sample_comments.json

gx = GenerateXls(
    json_file=json_file,
    output_file=output_file,
    comments_file=comments_file
)

gx.makeXL()

```
# Template of comments file
```
{
    "dependency name or jar name with version" : {
        "cve id" : {
            "Status" : "Status of the issue",
            "Comment: "Comment of he issue, which is need to be updated in generated xls file"
        }
    }
}
```
Download sample of comments file [here](./sample_comments.json)

## License

Copyright (c) 2021 Devaraju Garigapati

This repository is licensed under the MIT license.
See LICENSE for details.