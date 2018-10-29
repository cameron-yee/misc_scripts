from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

def concat(pdfs, num):
    base = '/Users/cyee/Documents/pdf_concat/lesson_{}/'.format(num)
    merger = PdfFileMerger(strict=False)
    for pdf in pdfs:
        merger.append(base + pdf)

    title = 'et_lesson_{}.pdf'.format(num)

    merger.write(title)


def removeEmpty(pdf):
    pages_to_keep = [0]

    infile = PdfFileReader(pdf, 'rb')
    output = PdfFileWriter()

    for i in range(infile.getNumPages()):
        if i in pages_to_keep:
            p = infile.getPage(i)
            output.addPage(p)

    with open(pdf, 'wb') as f:
        output.write(f)

    f.close()


if __name__ == '__main__':
    l1 = ['l1_1.pdf','l1_2.pdf','l1_3.pdf','l1_4.pdf']
    l2 = ['l2_1.pdf','l2_2.pdf','l2_3.pdf']
    l3 = ['l3_1.pdf','l3_2.pdf','l3_3.pdf','l3_4.pdf','l3_5.pdf','l3_6.pdf','l3_7.pdf']
    l4 = ['l4_1.pdf','l4_2.pdf','l4_3.pdf']
    l5 = ['l5_1.pdf','l5_2.pdf','l5_3.pdf','l5_4.pdf','l5_5.pdf','l5_6.pdf']
    all_pdfs = [l2] #[l1,l2,l3,l4,l5]

    count = 1
    for pdfs in all_pdfs:
        concat(pdfs, count)
        count += 1

    #removeEmpty('/Users/cyee/Desktop/vatl_session_7_cr_and_models_lap.pdf')

