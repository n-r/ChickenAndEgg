#!/usr/bin/env python3

import sys

def chickenAndEgg(n, ordered, quoteStr):
    def quote(s):
        if n == 1:
            return s
        return quoteStr + s + quoteStr

    if n == 0:
        return "the chicken" if ordered else "the egg"

    newQuoteStr = '"' if quoteStr == "'" else "'"
    punct = "?" if n == 1 else ""

    return "".join([
        "Which came first, ",
        quote(chickenAndEgg(n - 1, ordered, newQuoteStr)),
        " or ",
        quote(chickenAndEgg(n - 1, not ordered, newQuoteStr) + punct)
    ])

try:
    print(chickenAndEgg(int(sys.argv[1]), True, '"'))
except IndexError:
    print("""\nUsage:
./chickenAndEgg <number>
""")
