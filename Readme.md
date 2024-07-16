# Open Edu Hub Search ETL

## Step 1: Project Setup - Python (manual approach)

- make sure you have python3 installed (<https://docs.python-guide.org/starting/installation/>)
  - (Python 3.10 or newer is required)
- go to project root
- Run the following commands:

```
sudo apt install python3-dev python3-pip python3-venv libpq-dev -y
python3 -m venv .venv
```

For windows, go to python.org to download and install the proper python version. After that:
```commandline
python3.9 -m venv .venv
.venv\Scripts\activate.bat
pip3 install -r requirements.txt
copy .env.example .env
REM adjust .env according to your use case
```

Run splash service:
```commandline
docker-compose up -d
```
Splash creates screenshots from web pages when thumbnails are not available.

There is another service for use at crawl time called "pyppeteer" which is currently not in use by our crawlers.

## Step 1 (alternative): Project Setup - Python (automated, via `poetry`)

- Step 1: Make sure that you have [Poetry](https://python-poetry.org) v1.5.0+ installed
- Step 2: Open your terminal in the project root directory:
  - Step 2.1: (this is an optional, strictly personal preference) If you want to have your `.venv` to be created in the project root directory: 
    - `poetry config virtualenvs.in-project true`
- Step 3: Install dependencies (according to `pyproject.toml`) by running: `poetry install`

## Step 2: Project Setup - required Docker Containers
If you have Docker installed, use `docker-compose up` to start up the multi-container for `Splash` and `Playwright`-integration.

## Run a crawler
(Activate your virtual environment as in requirements above, if not already done.)
```commandline
scrapy crawl oeh_spider
```

If a crawler has [Scrapy Spider Contracts](https://docs.scrapy.org/en/latest/topics/contracts.html#spiders-contracts) implemented, you can test those by running `scrapy check <spider-name>`

# Running crawlers

- A crawler can be run with `scrapy crawl <spider-name>`. 
  - (It assumes that you have an edu-sharing v6.0+ instance in your `.env` settings configured which can accept the data.)
- If a crawler has [Scrapy Spider Contracts](https://docs.scrapy.org/en/latest/topics/contracts.html#spiders-contracts) implemented, you can test those by running `scrapy check <spider-name>`


## Running crawlers via Docker

```bash
git clone https://github.com/openeduhub/oeh-search-etl
cd oeh-search-etl
cp converter/.env.example .env
# modify .env with your edu sharing instance
export CRAWLER=your_crawler_id_spider # i.e. wirlernenonline_spider
docker compose build scrapy
docker compose up
```

# Building a Crawler

- We use scrapy, a framework for crawling metadata from the web
- To create a new spider, inside `converter/spiders/`, copy `sample_spider.py` to `<yourname>_spider.py`
- Inherit `LomBase` class in order to get out-of-the-box support for oeh's metadata model
- You may also inherit a base class for crawling data, e.g.
  - `LrmiBase` for crawling LRMI metadata
  - `OAIBase` for OAI interfaces
- Please take a look at the `sample_spider.py` for a template
- To learn more about the LOM standard we're using, you'll find useful information at https://en.wikipedia.org/wiki/Learning_object_metadata
- For more information, have a look into Confluence ("Using OpenEduHub (OEH) spiders")

# Still have questions? Check out our GitHub-Wiki!
If you need help getting started or setting up your work environment, please don't hesitate to visit our GitHub Wiki at https://github.com/openeduhub/oeh-search-etl/wiki
