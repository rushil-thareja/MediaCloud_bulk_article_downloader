# MediaCloud bulk article downloader
 Given news headlines with links from mediacloud extracts all text of those articles, multithreading enabled !
 
# Installing
* download zip
* pip install -r /path/to/requirements.txt


## Features
* get article text
* set the number of threads i.e the number of parallel processors
* checkpoints enabled, set after how many downloads checkpoints must be created

### How to set the number of threads
* threads will decide how many agents will execute this code parallely,
* therefore, this feature reduces execution time by a factor of number of threads
* you can use the default number of threads i.e 10, but to get least execution time
without puting too much stress on your machine choose number of threads lesser than
the logical processors in your machine
* in windows the logical processors can be checked by task manager:
 * Open Task Manager
 * Select Performance tab
 * Look for Cores and Logical Processors (Threads)
![logical processors](https://github.com/rushil-thareja/MediaCloud_bulk_article_downloader/blob/main/screenshots/checking_threads.JPG)

## Process
* go to mediacloud
![go to mediacloud](https://github.com/rushil-thareja/MediaCloud_bulk_article_downloader/blob/main/screenshots/s1.JPG)
* choose explorer
![choose explorer](https://github.com/rushil-thareja/MediaCloud_bulk_article_downloader/blob/main/screenshots/s2.JPG)
* go to explorer view and choose source
![go to explorer view and choose source](https://github.com/rushil-thareja/MediaCloud_bulk_article_downloader/blob/main/screenshots/s3.JPG)
* enter search terms or querry
![enter search terms or querry](https://github.com/rushil-thareja/MediaCloud_bulk_article_downloader/blob/main/screenshots/s4.JPG)
* click on Download all story URLs for employment
![click on Download all story URLs for employment](https://github.com/rushil-thareja/MediaCloud_bulk_article_downloader/blob/main/screenshots/s5.JPG)
* Download and save file in running directory, can rename as news.csv
![Download and save file in running directory, can rename as news.csv](https://github.com/rushil-thareja/MediaCloud_bulk_article_downloader/blob/main/screenshots/s6.JPG)
* set params in main.py file 
![set params in main.py file ](https://github.com/rushil-thareja/MediaCloud_bulk_article_downloader/blob/main/screenshots/s7.JPG)
* finnaly run the file by typing in CMD : python main.py
