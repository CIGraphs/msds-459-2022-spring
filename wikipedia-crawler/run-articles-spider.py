# This is a program for running the quotes spider
# Run from the WebFocusedCrawlWork directory with this command:
# python run-quotes-spider-scraped.py

import os  # operating system commands

# make directory for storing complete html code for web page
page_dirname = 'wikipages'
if not os.path.exists(page_dirname):
	os.makedirs(page_dirname)

# function for walking and printing directory structure
def list_all(current_directory):
    for root, dirs, files in os.walk(current_directory):
        level = root.replace(current_directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

# initial directory should have this form (except for items beginning with .):
#    TOP-LEVEL-DIRECTORY-FOR-SCRAPY-WORK
#        RUN-SCAPY-JOB-NAME.py
#        scrapy.cfg
#        DIRECTORY-FOR-SCRAPY
#            __init__.py
#            items.py
#            pipelines.py
#            settings.py
#            spiders
#                __init__.py
#                FIRST-SCRAPY-SPIDER.py
#                SECOND-SCRAPY-SPIDER.py

# examine the directory structure
current_directory = os.getcwd()
list_all(current_directory)

# list the avaliable spiders
print('\nScrapy spider names:\n')
os.system('scrapy list')

# decide upon the desired format for exporting output: 
# such as csv, JSON, XML, or jl for JSON lines

# run the scraper exporting results as a comma-delimited text file items.csv
# os.system('scrapy crawl quotes -o items.csv')

# run the scraper exporting results as a JSON text file items.json
# this gives a JSON array 
# os.system('scrapy crawl quotes -o items.json')

# for JSON lines we use this command
os.system('scrapy crawl articles-spider -o items.jl')
print('\nJSON lines written to items.jl\n')

# run the scraper exporting results as a dictionary XML text file items.xml
# os.system('scrapy crawl quotes -o items.xml')