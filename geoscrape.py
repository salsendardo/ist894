import dpkt
import socket
import pygeoip
import optparse

geo = pygeoip.GeoIP('/home/student/scripts/venv/dbip4.dat')
def retGeoStr(ip):
    try:
        rec = geo.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
            geoLoc = city + ', ' + country
        else:
            geroLoc = country
        return geoLoc
    except Exception, e:
        return 'N/A'
def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip  = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[*] Src:: ' + src + ' ---> Dst: ' + dst
            print '[*] Src: ' + retGeoStr(src) + ' ---> Dst: ' + retGeoStr(dst)
        except:
            pass
def main():
    parser = optparse.OptionParser('usage%prog -p <pcap_file>')
    parser.add_option('-p' , dest='pcapFile', type='string' , help='expect pcap file name')
    (options, args) = parser.parse_args()
    if options.pcapFile == None:
        print parser.usage
        exit(0)
    pcapFile = options.pcapFile
    f = open(pcapFile)
    pcap = dpkt.pcap.Reader(f)
    printPcap(pcap)
if __name__ == '__main__':
    main()
