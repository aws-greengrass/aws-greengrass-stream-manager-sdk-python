## AWS Greengrass Stream Manager SDK for Python

The **AWS Greengrass Stream Manager SDK for Python** enables Python developers to manage data streams using [Stream
Manager](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-data-streams.html) on AWS IoT Greengrass core.

## Overview

This document provides instructions for preparing your Python code to manage Streams in Stream Manager using the Python
SDK.

## Using Stream Manager Client to work with Streams

Follow the guide [here](https://docs.aws.amazon.com/greengrass/v2/developerguide/work-with-streams.html) to work
with Streams using the Stream Manager Client from the Stream Manager SDK.

View Python SDK documentation [here](https://aws-greengrass.github.io/aws-greengrass-stream-manager-sdk-python/).

## Compatibility

Stream Manager SDK provided by this repo is compatible with Stream Manager running on Greengrass Core 1.11 and above.

## Requirements

This SDK has additional requirements. Specifically, Stream Manager SDK requires Python version 3.6 or above. It also
 has package requirements listed in the requirements.txt file. Please install these requirements.

To install the requirements you can use pip such as :code:`pip install --user -r requirements.txt`. This will install
the requirements to your Python path on the device. However if you are deploying the code to a device, you can bundle
the requirements with your code. With the pip command above, the dependencies will be installed to the user
site-packages directory. To find its location, use :code:`python -m site --user-site`. You can then simply copy the
entire user site package directory contents into the final artifact before deploying which will ensure that the Stream
Manager dependencies are present.

## Installation

One way to install both stream-manager and its dependencies (i.e. cbor) is to run the following command:
```console
pip3 install stream_manager
```

## Getting Help

*   [Ask on AWS re:Post](https://repost.aws/)

## License

Apache 2.0
