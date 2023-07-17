# Processing production logs using Python and SQL

In a seismic acquisition survey all of the field and processed seismic data are held digitally on removable or external hard drives. Back to the base camp this data and ancillary field data will be analysed and QCed properly.
One of the most important ancillary field data that we receive is called “Oberver Log”, it contains all the necessary information we need about the records (SEG-D files). All the details are specified in this report, such as missed shots, bad traces, noisy files…etc.
Now days the production logs are generated automatically from the recording unit. Some systems supplied the logs in [XML](https://docs.python.org/3/library/xml.etree.elementtree.html) (Extensible Markup Language) format which makes the QC task difficult.<br>
<br>
For this reason, I generated a python code using ElementTree Python module and SQL to parse the information, process it and then output it in an excel file from the SQLite database file.

## **1. What is XML format?**
The [Extensible Markup Language](https://en.wikipedia.org/wiki/XML#:~:text=Extensible%20Markup%20Language%20(XML)%20is,%2Dreadable%20and%20machine%2Dreadable) (XML) is a markup language and file format for storing, transmitting, and reconstructing arbitrary data. It defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.

## **2. Parsing XML**
The xml.etree.ElementTree Python module implements a simple and efficient API for parsing and creating XML data. You can download




