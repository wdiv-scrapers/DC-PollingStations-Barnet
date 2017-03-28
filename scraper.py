from dc_base_scrapers.ckan_scraper import CkanScraper

base_url = 'http://open.barnet.gov.uk/api/3/action/package_show?id='

stations_info = {
    'dataset': 'polling-stations-in-barnet',
    'extra_fields': [],
    'return_format': 'CSV',
}

council_id = 'E09000003'


stations_meta_scraper = CkanScraper(
    base_url,
    stations_info['dataset'],
    stations_info['return_format'],
    stations_info['extra_fields'],
    'utf-8')
stations_url = stations_meta_scraper.scrape()
