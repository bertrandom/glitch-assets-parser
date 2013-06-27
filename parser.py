#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import os, os.path
import json
import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Parses Glitch assets (food and drink) metadata into a JSON format')
parser.add_argument('-f', '--filename', type=argparse.FileType('w'), help='file to output to')

args = parser.parse_args()

script_path = os.path.dirname(os.path.realpath(__file__))

output = {}

categories = ["food", "drinks"]

for category in categories:

	txt = open(script_path + '/html/items_' + category + '.html')
	html = txt.read()

	soup = BeautifulSoup(html)

	el_items_list = soup.find("ul", {"class": "items-list"})
	el_items = el_items_list.findAll("li")

	items = {}

	for el_item in el_items:

		item = {}

		link = el_item.find('a')

		match = re.search('/items/(.*)/(.*)/', link['href'])
		item_id = match.group(2)

		item['name'] = el_item.find('span', {"class" : "item-name"}).string
		item['description'] = el_item['title']

		item_html = open(script_path + '/html/items_' + category + '_' + item_id + '.html').read()
		item_soup = BeautifulSoup(item_html)
		el_asset_list = item_soup.find('table', {"class" : "asset_list"})
		el_asset_links = el_asset_list.findAll('a')
		el_asset_link = el_asset_links[0]

		item_match = re.search('/2012-12-06/(.*)__', el_asset_link['href'])
		directory_name = item_match.group(1)

		for dirname, dirnames, filenames in os.walk(script_path + '/glitch-assets/' + directory_name + '/'):
		    for filename in filenames:
		    	if "iconic" in filename:
		    		item['asset_path'] = 'glitch-assets/' + directory_name + '/' + filename

		im = Image.open(item['asset_path'])
		item['width'] = im.size[0]
		item['height'] = im.size[1]

		items[item_id] = item

	output[category] = items

json_output = json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))

if args.filename != None:
	args.filename.write(json_output)
	args.filename.close()
else:
	print json_output