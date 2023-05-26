import argparse
import datetime
import csv
import pandas as pd

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--csv', type=str, help='input csv file', default='/Users/johnoleary/Downloads/Lesson_Record2023-05-25_17_29_50.csv')
	args = parser.parse_args()

	csv_in = args.csv

	# Extract raw data
	csv = pd.read_csv(csv_in)
	csv = csv.fillna('')

	section_cols = sorted([col for col in csv.columns if col.startswith("Section ")])
	section_cols = ['Section 3A']

	print(section_cols)

	relevant_cols = [
		"Submission Date",
		"Student"
	] + section_cols

	csv[section_cols] = csv[section_cols].applymap(lambda c: c.split("\n") if c else c)
	print(csv[relevant_cols])
	# with open(csv_in) as f:
	# 	csvreader = csv.reader(f, delimiter=',', quotechar='"')
	# 	# for row in csvreader:
	# 	# 	print(', '.join(row))
		
	# Transform for report printing

	# Generate report
