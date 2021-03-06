import os

def scrap():
    try: 
        os.remove("data_s/race_result.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/qualif.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/tyres.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/fastest_b.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/fastest_a.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/pit_stop.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/qualif_2021_no_sprint.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/qualif_2021_sprint.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/standings_driver.json")
    except Exception as e:
        print(e)
    try:
        os.remove("data_s/standings_team.json")
    except Exception as e:
        print(e)

    os.system("scrapy crawl f1_parse2 -o data_s/race_result.json")
    os.system("scrapy crawl qualif -o data_s/qualif.json")
    os.system("scrapy crawl f1fca -o data_s/tyres.json")
    os.system("scrapy crawl fastest_before -o data_s/fastest_b.json")
    os.system("scrapy crawl fastest_after -o data_s/fastest_a.json")
    os.system("scrapy crawl pit_stop -o data_s/pit_stop.json")
    os.system("scrapy crawl qualif_2021_sprint -o data_s/qualif_2021_sprint.json")
    os.system("scrapy crawl qualif_2021_no_sprint -o data_s/qualif_2021_no_sprint.json")
    os.system("scrapy crawl standings_driver -o data_s/standings_driver.json")
    os.system("scrapy crawl standings_team -o data_s/standings_team.json")