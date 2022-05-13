from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import qr
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
import webbrowser,os
content = 'https: // wangxiao20485.github.io/Untitled-1.html'
def createQRCode():
    Qr_code = qr.QrCodeWidget(content,barBorder=2,barWidth=113,barHeight=113)
    drawing=Drawing(50,50)
    drawing.add(Qr_code)
    renderPDF.draw(drawing, c, 51,28)


c = canvas.Canvas("stud_card.pdf")
c.drawImage("1.png",0,0,width=372,height=665)
c.drawImage("2.png",150,420,width=87,height=95,mask="auto")
c.roundRect(145,415,95,105,6,stroke=1,fill=0)
createQRCode()
c.showPage()
c.save()
webbrowser.open("file://" + os.path.realpath("stud_card.pdf"))
