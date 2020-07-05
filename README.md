PythonScripts
=============


## General Python Recipes

- [parallelism_process.py](parallelism_process.py) - Python parallel processing code using multiple processes.

- [parallelism_thread.py](parallelism_thread.py) - Python parallel processing code using multiple threads.

- [parallelism_pool.py](parallelism_pool.py) - Python parallel processing code using multiple processes but with simpler syntax.

- [split_iter.py](split_iter.py) - Generator version of split.


## CSV/Excel/SQL data

- [edd.py](edd.py) - Generates an EDD (Extended Data Dictionary) of a file. Requires ```pandas``` module.

- [split_csv.py](split_csv.py) - Splits a CSV into multiple CSVs.

- [combine_csv_0.py](combine_csv_0.py) - Combines a list of csv files into a single csv. Header needs to be same. Requires ```pandas``` module.

- [combine_csv_1.py](combine_csv_1.py) - Combines a list of csv files into a single csv. Header needs to be same. Handles UnicodeDecodeErrors, to some extent. Requires ```pandas``` module.

- [csv2excel_adj_widths.py](csv2excel_adj_widths.py) - Converts CSV into Excel with the column with adjusted to the max length in the column.

- [csv2SQL.py](csv2SQL.py) - Reads a CSV and uploads it to a SQL Database. Requires ```pandas``` and ```sqlalchemy``` modules.

- [sql2formatted_excel.py](sql2formatted_excel.py) - Extracts table from MS SQL DB and saves it into CSV and Column adjusted Excel.

- [sql_select_into.py](sql_select_into.py) - Creates new tables in SQL DB using SELECT INTO using Python.


## Text

- [correct_encoding.py](correct_encoding.py) - Converts a mixed encoding CSV file into a utf-8 compliant CSV.

- [word_freq.py](word_freq.py) - Word frequency.

- [wiki.py](wiki.py) - Fetches the page contents in plain text. Depends on ```wikipedia``` module. (```pip install wikipedia```)

- [gtransliterate.py](gtransliterate.py) - Gets a transliteration of a word from hindi to english (and vice-versa).

- [gen_wordcloud.py](gen_wordcloud.py) - Generates a wordcloud from a given text and writes it to a PNG file. Depends on - ```wordcloud``` and ```matplotlib```.

- [sentence_boundary.py](sentence_boundary.py) - Determines sentence boundaries.

- [state_from_address.py](state_from_address.py) - Extracts State and City from an address column.

- [address_similarity.py](address_similarity.py) - Gives a similarity between 2 addresses.

- [lat_long2addr.py](lat_long2addr.py) - Gets address from lat-long using Google Maps API. This is an old code so I am not sure if it'll work now.


## PDFs

- [pdf2csv_0.py](pdf2csv_0.py) - Extracts simple table from a PDF document. Requires the installation of ```Java``` based ```Tabula``` and ```tabula``` python module.

- [pdf2csv_1.py](pdf2csv_1.py) - Extracts tables from a PDF document, page by page. Requires the installation of ```Java``` based ```Tabula``` and ```tabula``` python module.

- [pdf2csv_2.py](pdf2csv_2.py) - Extracts tables from a PDF document. First tries to convert it as a whole, if it fails, converts it page by page. Requires the installation of ```Java``` based ```Tabula``` and ```tabula``` python module.


## Videos

- [vid2frames.py](vid2frames.py) - Extract frames from a video using opencv (both versions - parallel and non-parallel).


## GUI

- [move_cursor.py](move_cursor.py) - Moves the cursor to the lower right corner and keeps clicking there after every 5 seconds. Prevents the screen from sleeping.


## Random Stuff

- [prime_gen.py](prime_gen.py) - An iterator that generates primes.

- [greads.py](greads.py) - Scrapes all the pages of the user's liked quates list on Goodreads by using HTML scraper and add them to a file.

- [greads_rss.py](greads_rss.py) - Scrapes the RSS feed of the user's liked quotes on Goodreads and then randomly displays one random quote from all the quotes.

- [img_download.py](img_download.py) - Downloads an image from a given link.
