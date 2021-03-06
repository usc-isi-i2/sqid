MOCK_HEADERS = [('Date', 'Wed, 13 May 2020 17:27:28 GMT'), ('Server', 'mw1363.eqiad.wmnet'), ('X-Content-Type-Options', 'nosniff'), ('P3p', 'CP="See https://www.wikidata.org/wiki/Special:CentralAutoLogin/P3P for more info."'), ('Mediawiki-Login-Suppressed', 'true'), ('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Credentials', 'false'), ('Access-Control-Expose-Headers', 'MediaWiki-API-Error, Retry-After, X-Database-Lag, MediaWiki-Login-Suppressed'), ('X-Frame-Options', 'DENY'), ('Content-Disposition', 'inline; filename=api-result.json'), ('Vary', 'Accept-Encoding,Treat-as-Untrusted,X-Forwarded-Proto,Cookie,Authorization'), ('Cache-Control', 'private, must-revalidate, max-age=0'),
                ('Content-Type', 'application/json; charset=utf-8'), ('Age', '0'), ('X-Cache', 'cp4027 miss, cp4032 pass'), ('X-Cache-Status', 'pass'), ('Server-Timing', 'cache;desc="pass"'), ('Strict-Transport-Security', 'max-age=106384710; includeSubDomains; preload'), ('Set-Cookie', 'WMF-Last-Access=13-May-2020;Path=/;HttpOnly;secure;Expires=Sun, 14 Jun 2020 12:00:00 GMT'), ('Set-Cookie', 'WMF-Last-Access-Global=13-May-2020;Path=/;Domain=.wikidata.org;HttpOnly;secure;Expires=Sun, 14 Jun 2020 12:00:00 GMT'), ('Set-Cookie', 'GeoIP=US:CA:Los_Angeles:34.00:-118.43:v4; Path=/; secure; Domain=.wikidata.org'), ('X-Client-IP', '76.94.202.193'), ('Accept-Ranges', 'bytes')]

ELASTICSEARCH_HOST = "localhost"

MOCK_CLASSIFICATION = {}

PROPERTY_FILES = [
    "flask_data/macroscore_0827_properties.tsv",
    "flask_data/wikidata_properties.tsv"
]

ES_INDEX = "macroscore"
SPARQL_ENDPOINT = 'http://localhost:14000/bigdata/namespace/wdq/sparql'

#Flask Port
PORT = 5556
HOST = "0.0.0.0"

# SQID domain
DOMAIN = "http://sitaware.isi.edu:8051/"
