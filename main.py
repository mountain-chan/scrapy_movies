import json

from scrapy_movies.spiders.movies import process


def crawl_movie(keyword):
    parameters = {
        "keyword": str(keyword).strip().replace(" ", "%20")
    }

    with open("parameter.json", "w") as f:
        json.dump(parameters, f, indent=4)

    # run scraper
    process.start()

    # get data from movies file
    with open("movies.json") as f:
        movies = json.load(f)

    print("seasons: ", len(movies))
    for m in movies:
        print(m)


if __name__ == '__main__':
    """
    Start crawl movies with keyword
    """
    crawl_movie("diners")
