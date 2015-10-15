#!/usr/bin/env python

#Command line scipt to convert a single number to and from several units

import argparse, webbrowser

from src.convert import kilometers_to_miles, miles_to_kilometers,\
        years_to_minutes, minutes_to_years, thousand_to_xkcd_thousand

#Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('value', type=float, help="The number to be converted")
args = parser.parse_args()

#Perform conversions
#km to miles
to_miles = kilometers_to_miles(args.value)
print("{0} kilometers is {1} miles".format(args.value, to_miles))

# miles to km
to_km = miles_to_kilometers(args.value)
print("{0} miles is {1} kilometers".format(args.value, to_km))

# years to minutes
to_minutes = years_to_minutes(args.value)
print("{0} years is {1} minutes".format(args.value, to_minutes))

# minutes to years
to_years = minutes_to_years(args.value)
print("{0} minutes is {1} years".format(args.value, to_years))

# thousand to xkcd-thousand
# easter egg
if args.value == 1000:
    to_xkcd_thousand = thousand_to_xkcd_thousand(args.value)
    print("{0} in our world is equal to {1} in xkcd-land".format(to_xkcd_thousand, args.value))
    webbrowser.open("http://xkcd.com/1000/")
