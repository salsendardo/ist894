import pyPdf
import optparse
from pyPdf import PdfFileReader

def metaPrint(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    documentInfo = pdfFile.getDocumentInfo()
    print '[*] PDF Metadata report for: ' + str(fileName)
    for metaItem in documentInfo:
        print '[+] ' + metaItem + ':' + documentInfo[metaItem]
def main():
    parser = optparse.OptionParser('usage %prog "+" -F <PDF_File_Name>')
    parser.add_option('-F', dest='fileName', type='string', help='<PDF file name expected>')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print parser.usage
        exit(0)
    else:
        metaPrint(fileName)
if __name__ == '__main__':
    main()
