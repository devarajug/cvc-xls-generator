# cvc-xls-generator
It takes json file which is generad by dependency check tool as input and conver it into xlsx file, while converting to xls it mark false positives by using user defined comments.json file.

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
    #comments_file=comments_file #optional if you have comments json file uncomment it.
)

gx.makeXL()

```
# Comments File
The template of comments json file should be like below and it is optional
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
Download sample of comments file [here](https://raw.githubusercontent.com/devarajug/cvc-xls-generator/master/sample_comments.json)

## License

Copyright (c) 2021 Devaraju Garigapati

This repository is licensed under the MIT license.
See LICENSE for details.