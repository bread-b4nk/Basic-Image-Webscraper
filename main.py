''' 
   Python Web Scraper, still in early stages, started: August 2020
    Only limited to images and links from google searches
   
'''

#ALSO : pip install -r requirements.txt to download requirements

import sys, getopt

from functions import *

def main():
    # testing get_links() function
    # user_input = input("What do you want to search? ")
    
    # print(links)
    
    # testing get_pics() function

    print("\nHello! Here are our options:\n\t1. Download images from imgur.com\n\t2. Download images from google (small version)\n\t3. Download images from google(big version)")
    user_input = input("Please input 1,2, or 3: ")
    if int(user_input) == 1:
        user_input = (input("Please enter your search query: "))
        imgur_save_pics(user_input)
    elif int(user_input) == 2:
        user_input = (input("Please enter your search query: "))
        google_save_pics_small(user_input)
    elif int(user_input) == 3:
        user_input = (input("Please enter your search query: "))
        google_save_pics_big(user_input)
    # elif int(user_input) == 4:
    #     user_input = (input("Please enter your search query: "))
    #     search_query = user_input
    #     titles, links, descriptions = get_links(user_input)
    #     save_links(titles,links,descriptions,search_query)
    else:
        print("Please input 1,2, or 3")

        
        # pick between save or  output, but im going to do a command line interface instead

main()