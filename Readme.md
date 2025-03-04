# Open Edu Hub Search ETL

This repository is forked from openeduhub. Only a few spiders are directly in use
with oeh_spider being the main one. Others are mediothek_pixiothek, merlin, sodix.
Notable differences to the original repository are schulcloud/ and run.py.

The terms "spider" and "crawler" may be used interchangeable.

## Step 1: Project Setup — Python 3.13 (manual approach)

- make sure you have python3 installed (<https://docs.python-guide.org/starting/installation/>)
  - (Python 3.13 is required)
- go to project root
- Run the following commands:

```
sudo apt install python3-dev python3-pip python3-venv libpq-dev -y
python3 -m venv .venv
source .venv/bin/activate
pip3 install poetry
poetry install
cp .env.example .env
# adjust .env according to your use case
```

For windows, go to python.org to download and install the proper python version. After that:
```commandline
python3 -m venv .venv
.venv\Scripts\activate.bat
pip3 install poetry
poetry install
copy .env.example .env
REM adjust .env according to your use case
```

Run splash service:
```commandline
docker-compose up -d
```
Splash creates screenshots from web pages when thumbnails are not available.

`pip3 install poetry`

`poetry install`

## Step 1 (alternative): Project Setup - Python (automated, via `poetry`)

- Step 1: Make sure that you have [Poetry](https://python-poetry.org) [v1.8.4](https://github.com/python-poetry/poetry/releases/tag/1.8.4)+ installed
  - for detailed instructions, please consult the [Poetry Installation Guide](https://python-poetry.org/docs/#installation)
- Step 2: Open your terminal **in the project root directory**:
  - Step 2.1: If you want to have your `.venv` to be created inside the project root directory: 
    - `poetry config virtualenvs.in-project true`
      - *(this is an optional, strictly personal preference)* 
- Step 3: **Install dependencies** (according to `pyproject.toml`) by running: `poetry install`

## Step 2: Project Setup - required Docker Containers

If you have Docker installed, use `docker-compose up` to start up the multi-container for `Splash` and `Playwright`-integration.

## Run a crawler
(Activate your virtual environment as in requirements above, if not already done.)
```commandline
scrapy crawl oeh_spider
```

If a crawler has [Scrapy Spider Contracts](https://docs.scrapy.org/en/latest/topics/contracts.html#spiders-contracts) implemented, you can test those by running `scrapy check <spider-name>`

Or using the docker image:
```bash
docker build --tag oeh-search-etl .
./docker_run.sh oeh_spider
```
From the docker image respectively run.py, there are also other options one can execute like H5P upload or sodix permission script.

## Writing a spider/crawler

- We use scrapy, a framework for crawling metadata from the web
- To create a new spider, inside `converter/spiders/`, copy `sample_spider.py` to `<yourname>_spider.py`
- Inherit `LomBase` class in order to get out-of-the-box support for oeh's metadata model
- You may also inherit a base class for crawling data, e.g.
  - `LrmiBase` for crawling LRMI metadata
  - `OAIBase` for OAI interfaces
- Please take a look at the `sample_spider.py` for a template
# Running crawlers

- A crawler can be run with `scrapy crawl <spider-name>`. 
  - (It assumes that you have an edu-sharing v8.1+ instance in your `.env` settings configured which can accept the data.)
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

- We use Scrapy as a framework. Please check out the guides for Scrapy spider (https://docs.scrapy.org/en/latest/intro/tutorial.html)
- To create a new spider, create a file inside `converter/spiders/<myname>_spider.py`
- We recommend inheriting the `LomBase` class to get out-of-the-box support for our metadata model
- You may also inherit a base class (see: `converter/spiders/base_classes/`) for crawling data. 
  - If your site provides LRMI metadata, the `LrmiBase` is a good start. 
  - If your system provides an OAI interface, you may use the `OAIBase`
- As a sample/template, please take a look at the `sample_spider.py` or `sample_spider_alternative.py`
- To learn more about the LOM standard we're using, you'll find useful information at https://en.wikipedia.org/wiki/Learning_object_metadata
- For more information, have a look into Confluence ("Using OpenEduHub (OEH) spiders")

# Still have questions? Check out our GitHub-Wiki!
If you need help getting started or setting up your work environment, please don't hesitate to visit our GitHub Wiki at https://github.com/openeduhub/oeh-search-etl/wiki
