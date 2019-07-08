1. Filter source BFMF spreadsheet to display multipage records (FILE column --> fiter by condition --> text contains --> "_p")
2. Remove page suffix in RECORD column (everything after and including "_p")
3. Copy into new spreadsheet
4. Download as .csv
5. Rename .csv "multi.csv"
6. Move .csv to same directory as python script
7. Run
8. In original Google Sheets spreadsheet, select all (should still only be displaying multipage records)
9. Go to Data --> Remove Duplicates
10. Check "Data has header row", click the box for "Select all" to deselect all check boxes, and then select only "Column A - record"
11. Make sure the remaining number of rows matches the output number of rows in "condensed.csv"
12. Copy 'file' into file column in source spreadsheet, and copy 'meas' into physical_description_size
13. Double check to make sure filenames match those in the record column
14. Viola!

Note: Must have the physical_description_size column filled out or the program will throw an error.
