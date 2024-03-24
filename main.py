from scrap import extract_contents_for

ALLOW_SCRAPPING = False # Toggle to enable web scrapping. 


def main():
    urls = [
        "https://www.stir.ac.uk/study/fees-funding/",
        "https://www.stir.ac.uk/study/semester-dates/",
        "https://www.stir.ac.uk/about/contact-us/",
        "https://www.stir.ac.uk/study/fees-funding/how-to-pay-your-fees/",
        "https://www.stir.ac.uk/internal-students/fees-and-finance/online-payment-terms-and-conditions/",
    ]
    
    if ALLOW_SCRAPPING:
        bool_ = extract_contents_for(urls)
        print(bool_)
        

if __name__ == "__main__":
    main()