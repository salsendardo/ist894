import pygeoip

gi = pygeoip.GeoIP('/home/student/scripts/venv/dbip4.dat')
def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    region = rec['region']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt + ' Geo-located. '
    print '[*] '+str(city)+', '+str(region)+', '+str(country)
    print '[+] Latittude: '+str(lat)+ ', Longitude: '+ str(long)
tgt = '173.255.226.98'
printRecord(tgt)
