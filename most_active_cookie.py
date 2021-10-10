import argparse

"""
Sets up argparse to parse command line flags
@return the data and file name
"""
def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, help='Required date argument')
    parser.add_argument('-f', type=str, help='Required file argument')
    args = parser.parse_args()
    return args.d, args.f

"""
Finds the most frequent cookie(s)
@param cookieDates: the dictionary of cookie dates and cookies w/ the number of occurances
@param date: the date to find the most frequent cookie for
@return the list of most frequent cookie(s)
"""
def findMostFrequentCookie(cookieDates, date):
    mostFreqOcur = max(cookieDates[date].values())
    cookies = []
    for cookie, ocur in cookieDates[date].items():
        if ocur == mostFreqOcur:
            cookies.append(cookie)
    return cookies

"""
Parses the file of cookies and timestamp pairs
@param the opened file descriptor
@return the dictionary containing the cookie dates and cookies w/ the number of occurances
"""
def parseFile(f):
    cookieDates = {}
    for line in f:
        cookie, UTCDate = line.split(',')
        cookieDate = UTCDate.replace('\n', '').split('T')[0]
        if cookieDate not in cookieDates:
            cookieDates[cookieDate] = {}
        if cookie not in cookieDates[cookieDate]:
            cookieDates[cookieDate][cookie] = 0
        cookieDates[cookieDate][cookie] += 1
    return cookieDates

"""
The main entry point for the program. It setups the parser, opens the file, parses the file, and then
finds the most frequent cookie. Lastly, it prints the most frequent cookies and closes the file.
"""
def main():
    date, file = init_parser()
    f = open(file)
    cookieDates = parseFile(f)
    res = findMostFrequentCookie(cookieDates, date)
    for i in res:
        print(i)
    f.close()

main() # Start the program

