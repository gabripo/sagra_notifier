from sagra_downloader.page_scraper import SagraPageContent

if __name__ == "__main__":
    url = "https://www.sagreinemilia.it/sagre_per_provincia/8/ferrara"
    sagra_content = SagraPageContent(
        url=url
    )

    sagra_content.print_sagra_content()