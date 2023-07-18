import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('prodlog_xml_db.sqlite')
cur = conn.cursor()
# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Record_id;

CREATE TABLE Record_id (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    record_id INTEGER,
    reshoot_idx INTEGER,
    data_type TEXT,
    state TEXT,
    Date TEXT
);
''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Production-Log-23-03-2016-23.58.20.xml'

stuff = ET.parse(fname)
all = stuff.findall('acquisitionRecord')
corr=[]
for item in all:
    if item.find('seismic-data-type').text == 'VIB_SS_CORR_REFERENCE':
        corr.append(item.find('seismic-data-type').text)
#print('CORR FILES:', len(corr) )

for item in all:
    if item.find('seismic-data-type').text:
        data_type = item.find('seismic-data-type').text
    if item.find('state').text:
        state = item.find('state').text
    if item.find('reshoot-index').text:
        reshoot_idx = item.find('reshoot-index').text
    if item.find('record-id').text:
        record_id = item.find('record-id').text
    if item.find('acquisitionTime').text:
        date = item.find('acquisitionTime').text   

    if data_type is None or state is None or reshoot_idx is None or record_id is None or date is None:
        continue

    cur.execute('''INSERT OR REPLACE INTO Record_id
        (record_id, state, data_type, reshoot_idx, Date)
        VALUES ( ?, ?, ?, ?, ?)''',
        ( record_id, state, data_type, reshoot_idx, date) )

    conn.commit()
