import argparse
import PyPDF2
import re

parser = argparse.ArgumentParser(description='Reorganize PDFs By DOI')
parser.add_argument('pdf_file')
args = parser.parse_args()

print(args)
print(args.pdf_file)
with open(args.pdf_file, "rb") as my_file:
	try:
	    #PyPDF2.PdfFileReader(open(args.pdf_file, "rb"))
	    pdfReader =PyPDF2.PdfFileReader(my_file)
	except PyPDF2.utils.PdfReadError:
	    print("Invalid PDF file")
	else:
	    pass


	# PDF Metadata and Summary Stats
	print(pdfReader.numPages)
	docInfo = pdfReader.getDocumentInfo()
	print(docInfo.subject)
#	xmpInfo = pdfReader.getXmpMetadata()
#	print("xmp:")
#	print(type(xmpInfo))
#	print(xmpInfo.custom_properties)
#	print("done")

	pageObj = pdfReader.getPage(0)
	pdf_text = pageObj.extractText()
	pdf_text_lines = pdf_text.splitlines()

	# regex from pyRenamePdf
	regex_dict = {
		'key1': re.compile(r'(?<=doi)/?:?\s?\d{2}\.\d{4}/\S*[0-9]'), 
		'key2': re.compile(r'(?<=http://dx.doi.org/)\d{2}\.\d{4}/\S*[0-9]'),
		'key3': re.compile(r'(?<=doi).?10.1073/pnas\.\d+'), # PNAS fix
		'key4': re.compile(r'10\.1083/jcb\.\d{9}') # JCB fix

	}



	for line in pdf_text_lines:
		for key, pattern in regex_dict.items():
			s = pattern.search(line)
			if s:
				print(s.re)
				print(s.string)
				print(s.group(0))





