from dc_base_scrapers.datapress_scraper import DataPressScraper

base_url = 'http://open.barnet.gov.uk/api/dataset/'

stations_info = {
    'dataset': 'polling-stations-in-barnet',
    'extra_fields': [],
    'return_format': 'csv',
}

council_id = 'E09000003'


stations_meta_scraper = DataPressScraper(
    base_url,
    council_id,
    stations_info['dataset'],
    stations_info['return_format'],
    stations_info['extra_fields'],
    'utf-8')
stations_url = stations_meta_scraper.scrape()
