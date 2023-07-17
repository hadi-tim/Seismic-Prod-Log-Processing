# Production log processing using Python and SQL

In a seismic acquisition survey all of the field and processed seismic data are held digitally on removable or external hard drives. Back to the base camp this data and ancillary field data will be analysed and QCed properly.
One of the most important ancillary field data that we receive is called “Oberver Log”, it contains all the necessary information we need about the records (SEG-D files). All the details are specified in this report, such as missed shots, bad traces, noisy files…etc.
Now days the production logs are generated automatically from the recording unit. Some systems supplied the logs in XML (Extensible Markup Language) format which makes the QC task difficult.
I generated a python code using ElementTree Python module and SQL to parse the information, process it and then output it in an excel file from the SQLite database file.




