# Hindenberg Scrape
<p style="font-size: 16px;"> The goal of this script is to capitalize on the periodic research releases by Hindenburg Research and their associates. In virtually all publications on their website, http://www.hindenburgresearch.com/, the associated stock value mentioned drops a  significant amount.

Within the script there are a few different components. After running, the script will loop continuously until it notice a new publication on Hindenburg's website - the script will proceed to search for mention of the stock's ticker as well as an indication that Hindenburg Research themselves took a short position. Once these components are found and it is confirmed that the ticker in the new publication does not match the ticker from the previous publication**(haven't incorporated this yet), the script will proceed to enter into our short position using Alpaca API.

Steps should be taken to incorporate the user's (you) risk tolerance into the position taken to ensure and this can be done by altering the code in the script.

I am not a licensed financial advisor - none of this information should be taken as financial advice. The script provided is for educational purposes and should be used for paper trading, not on a live trading platform.</p>

Converting to C++ to improve latency
