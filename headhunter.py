import os
import sys
import json
import time
import shutil
import signal
import random
import traceback
import datetime
from datetime import datetime, timedelta
from tqdm import tqdm
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ensure you pass the right arguments (email, password, delay, depth)
if len(sys.argv) != 5:
    print("Usage: ~$ python3 ./headhunter.py <linkedin_email> <linkedin_password> <delay_in_seconds> <max_page_depth>")
    exit(0)
else:
    u = list(sys.argv)[1]
    p = list(sys.argv)[2]
    delay = int(list(sys.argv)[3])
    depth = int(list(sys.argv)[4])

def keyboardInterruptHandler(signal, frame):
    save()
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

def save():
    print("*********** ERR - ENDING GRACEFULLY ************************")
    end_time = int(round(time.time() * 1000))
    log['runtime'] = log['runtime'] + (end_time - start_time)
    log['last_updated'] = str(datetime.now())

    date = datetime.now().strftime("%d-%m-%Y")
    todays_log = "./logs/log-" + date + ".json"

    with open(todays_log, 'w') as fp:
        json.dump(log, fp)

    with open("./logs/master_user_log.txt", 'w') as fp:
        for user in master_users:
            fp.write('%s\n' % user)

    with open("./logs/master_query_log.txt", 'w') as fp:
        for query in master_queries:
            fp.write('%s\n' % query)

    browser.quit()

def check_log():
    print("- Log_Name: " + log['log_name'])
    current_log = "log-" + datetime.now().strftime("%d-%m-%Y") + ".json"
    if current_log == log['log_name']:
        print("Current log is Correct.")
    else:
        print("Current log is Wrong.")

# Loading necessary files
print("=========== Linkedin Social Engineering Script ============")
print("       -------'IF YOU VIEW IT THEY WILL COME'-------        ")

print("=---- Checking for ./chromedriver")
if os.path.isfile("./chromedriver") is False:
    print("- CHROMEDRIVER IS NOT INSTALLED! Get it here: https://chromedriver.chromium.org/downloads")
    exit(0)
else:
    print("- Chromedriver is installed.")

print("=---- Loading Keywords")
keywords = open("./keywords.txt", "r").read().splitlines()
print("- " + str(len(keywords)) + " Keywords Loaded.")

print("=---- Loading User List")
master_users = open("./logs/master_user_log.txt", "r").read().splitlines()
print("- " + str(len(master_users)) + " Users Loaded.")

print("=---- Loading Query List")
master_queries = open("./logs/master_query_log.txt", "r").read().splitlines()
print("- " + str(len(master_queries)) + " Queries Already Completed.")

print("=---- Loading Log")
date = datetime.now().strftime("%d-%m-%Y")
print("- Today's Date: " + date)
todays_log = "log-" + date + ".json"
if not os.path.isfile("./logs/" + todays_log):
    print("- Creating A New Log For Today.")
    shutil.copy("./template.json", "./logs/" + todays_log)
else:
    print("- Log Exists, Loading it")
with open("./logs/" + todays_log) as json_file:
    log = json.load(json_file)
log["log_name"] = todays_log

# Load cities
print("=---- Loading Cities")
cities = open("./cities.txt", "r").read().splitlines()
print("- " + str(len(cities)) + " Cities Loaded.")
for city in cities:
    try:
        if log['cities'][city.split("#")[1].replace(" ", "")] == 0:
            log['cities'][city.split("#")[1].replace(" ", "")] = 0
    except KeyError:
        log['cities'][city.split("#")[1].replace(" ", "")] = 0

profile_languages = '["en","fr"]'
connection_degree = '["O"]'
search_slug = 'https://www.linkedin.com/search/results/people/?origin=GLOBAL_SEARCH_HEADER&facetNetwork=' + connection_degree + '&facetProfileLanguage=' + profile_languages + '&'

def hol_up(x):
    time.sleep(x)

def links_2_users(links):
    usernames = []
    for link in links:
        href = link.get_attribute("href")
        if href and "https://www.linkedin.com/in/" in href:
            username = href.replace("https://www.linkedin.com/in/", "").replace("/", "")
            if username not in usernames:
                usernames.append(username)
    return usernames

def check_query(city_id, keyword):
    query = city_id + "-" + keyword
    if query not in log['queries'] and query not in master_queries:
        log['queries'].append(query)

def add_query(city_id, keyword):
    query = city_id + "-" + keyword
    master_queries.append(query)
    save()

# Updated login function to wait until login is confirmed
def login():
    browser.get("https://www.linkedin.com/login")
    
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
    
    in_user = browser.find_element(By.ID, "username")
    in_user.send_keys(u)
    
    in_pass = browser.find_element(By.ID, "password")
    in_pass.send_keys(p)
    
    time.sleep(2)
    in_pass.send_keys(Keys.RETURN)
    print(">> Please complete 2FA if prompted (you have 60 seconds)...")

    # Wait until we see an element that indicates the user is logged in
    try:
        # Wait for a known element that only appears when logged in
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'feed/')]")))  # LinkedIn feed URL pattern
        print("Logged in successfully.")
    except:
        print("Failed to log in within the timeout period.")
        exit(1)  # Exit if login is unsuccessful

def check_sec(html, url):
    if "Let's Do A Quick Security Check" in html:
        alert = "RED ALERT"
        try:
            os.system('spd-say ' + alert)
        except:
            os.system('say ' + alert)

def heck():
    session_view_count = 0
    for city in cities:
        city_id = city.split("#")[1].replace(" ", "")
        city_slug = search_slug + '&facetGeoUrn=%5b"' + city_id + '"%5D'

        for keyword in keywords:
            check_log()
            check_query(city_id, keyword)

            browser.get(city_slug)
            check_sec(browser.page_source, city_slug)
            hol_up(delay)

            try:
                browser.execute_script("""
                var overlay = document.getElementById('msg-overlay');
                if (overlay) {
                    overlay.style.display = 'none';
                }
                """)
            except Exception as e:
                print("Overlay removal failed:", e)

            try:
                search_input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
                search_input.clear()
                search_input.send_keys(keyword)
                search_input.send_keys(Keys.RETURN)
            except Exception as e:
                print("Search bar not found or error occurred:", e)
                continue

            hol_up(delay)

            try:
                res_count = browser.find_element(By.CLASS_NAME, 'search-results__total').text.split(" ")[1]
            except:
                res_count = "0"
            page_count = 100
            if int(res_count.replace(",", "")) < 100:
                page_count = int(res_count.replace(",", "")) / 10
            if int(res_count.replace(",", "")) > depth:
                page_count = depth

            print(f"- {res_count} Results For '{keyword}' in '{city.split('#')[0].replace(' ', '')}'.")
            print(f"- {page_count} Pages of Results")

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            hol_up(delay)

            query_url = browser.current_url
            batch = []

            links = browser.find_elements(By.XPATH, "//a[@href]")
            users = links_2_users(links)
            batch.extend(users)

            for page in tqdm(range(2, int(page_count))):
                page_url = query_url + "&page=" + str(page)
                browser.get(page_url)
                check_sec(browser.page_source, page_url)
                hol_up(delay)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                links = browser.find_elements(By.XPATH, "//a[@href]")
                users = links_2_users(links)
                batch.extend(users)
                hol_up(delay)

            for c in tqdm(range(0, len(batch))):
                usr = batch[c]
                if usr not in log['users'] and usr not in master_users:
                    hol_up(delay)
                    browser.get("https://www.linkedin.com/in/" + usr + "/")
                    check_sec(browser.page_source, "https://www.linkedin.com/in/" + usr + "/")
                    log['users'].append(usr)
                    master_users.append(usr)
                    log['cities'][city.split("#")[1].replace(" ", "")] += 1
                    hol_up(delay)
                    session_view_count += 1

            add_query(city_id, keyword)

print('=========== STARTING HECK =================================')
start_time = int(round(time.time() * 1000))

try:
    browser = webdriver.Chrome(service=Service("./chromedriver"))
except Exception as e:
    print("Failed to start browser session.")
    traceback.print_exc()
    exit(1)

login()
try:
    heck()
except Exception as e:
    print("Error during execution:")
    traceback.print_exc()
    save()