import xlrd
import pandas as pd
location = (r'data.xlsx')
workbook = xlrd.open_workbook(location)
sheet = workbook.sheet_by_index(0)
sheet.cell_value(0, 0)
sheet.cell_value(1, 0)
from rake_nltk import Rake
r = Rake()
r.extract_keywords_from_text("relates five adventure of an owl")
r.get_ranked_phrases()
fact = "he is bad."
r.extract_keywords_from_text(fact)
r.get_ranked_phrases()
for line in keywords:
    print(line)

keywords = []
for i in range(1, 213304):
    sheet = workbook.sheet_by_index(0)
    eachSentence = sheet.cell_value(i, 0)
    try:
        r.extract_keywords_from_text(eachSentence)
    except TypeError:
        continue
    temp = r.get_ranked_phrases()
    keywords.append(temp)

