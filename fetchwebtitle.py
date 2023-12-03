# fetchwebtitle.py -  Module that tries to fetch a html page and parse title

import sys
import requests

def fetchtitle(url) -> str:
    title = ""
    try:
        res = requests.get(url)
        page = res.text
        titlestart = page.lower().find("<title>")
        titleend = page.lower().find("</title>")
        title = page[titlestart+7:titleend]
    except:
        title = "Title fetching failed."
    
    return title

# main function
def main() -> int:
    print(fetchtitle(input("Web page: ")))
    return 0

# main function entry point
if __name__ == '__main__':
    sys.exit(main())