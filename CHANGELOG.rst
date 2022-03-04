=========
CHANGELOG
=========

1.1.1
=====
- Stream manager client is now a context manager, enabling it to be used with the Python `with` statement.
- Bump cbor2 dependency version to support Python 3.10.
- Update usage of asyncio to support Python 3.10.

1.1.0
=====
Stream manager supports automatic data export to AWS S3 and AWS IoT SiteWise, provides new API method to update existing streams, and pause or resume exporting.
