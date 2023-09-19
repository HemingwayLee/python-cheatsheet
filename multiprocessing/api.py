import os
import requests
import time
from dotenv import load_dotenv
from multiprocessing import Pool


load_dotenv()
token = os.getenv('TOKEN')

def do_request(url):
    resp = requests.get(
        f"https://api.github.com/repos/HemingwayLee/{url}", 
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    )

    return resp.json()["stargazers_count"]

def run_in_parallel(urls, num_worker=4):
    with Pool(num_worker) as pool:
        result = pool.map(do_request, urls)

    pool.join()
    print(result)

def run_seq(urls):
    for url in urls:
        resp = requests.get(
            f"https://api.github.com/repos/HemingwayLee/{url}", 
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28"
            }
        )

        print(resp.json()["stargazers_count"])


def main():
    urls = [
        "docker-cheatsheet",
        "japan-map-js",
        "japanese-wordnet-visualization",
        "multichain-cheatsheet"
    ]

    start_time = time.time()
    run_seq(urls)
    print("--- %s seconds (run_seq) ---" % (time.time() - start_time))

    start_time = time.time()
    run_in_parallel(urls)
    print("--- %s seconds (run_par) ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
