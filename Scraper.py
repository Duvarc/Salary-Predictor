from lxml import html
import requests

page = requests.get("https://www.justice.gov/ust/eo/bapcpa/20140401/bci_data/median_income_table.htm")
tree = html.fromstring(page.content)

states = tree.xpath('//tr[@class="state-title"]/text()')
print(states)