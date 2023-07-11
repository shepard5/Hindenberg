# This function begins the looping of the program and will end under
# the circumstance that HindenBurg Research publishes a new report on their
# website, the program may or may not enter a position depending on a few
# variables
from Page_Benchmark import initial_benchmark
from Page_Refresh import Hindenburg_Refresh
from Ticker_Search import tickersearch
from Position_Search import Hindenburg_Position
from Enter_Short import Hindenburg_Enter_Position


initial_benchmark()
Hindenburg_Refresh()
ticker_search(body_text)
Hindenberg_Position_Search(body_text)
Hindenburg_Enter_position(position, ticker)
