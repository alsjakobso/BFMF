1. Filter source BFMF spreadsheet to display multipage records (record column --> fiter by condition --> text contains --> "_p")
2. Copy into new spreadsheet
3. Download as .csv
4. Rename .csv "multi.csv"
5. Move .csv to same directory as python script
6. Run
7. In source BFMF spreadsheet, delete text after "_p" in record column
8. Select all
9. Data --> Remove Duplicates
10. Check "Data has header row", click the box for "Select all" to deselect all check boxes, and then select only "Column A - record"
11. Make sure the remaining number of rows matches the output number of rows in "condensed.csv"
12. Copy file over file column in source spreadsheet, and copy meas into physical_description_size
13. Copy record over record column in source spreadsheet, or select source record column and remove trailing "_p"s
14. Viola!
