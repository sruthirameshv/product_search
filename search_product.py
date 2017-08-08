from amazon.api import AmazonAPI

# Amazon Credentials
AMAZON_ACCESS_KEY = "AKIAJHD6XRGK5NFMCPNA"
AMAZON_SECRET_KEY = "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"
AMAZON_ASSOC_TAG= "srvani92-20"

amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
products = amazon.search(Keywords='Room Essentials Magazine File Holder', SearchIndex='All')
for i, product in enumerate(products):
    print ("{0}. '{1}'".format(i, product.price_and_currency),product.title)
