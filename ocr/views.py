from django.shortcuts import render
import pytesseract
from PIL import Image

# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        pic = request.FILES.get("pic")
        nat = request.POST.get("nat")
        pytesseract.pytesseract.tesseract_cmd = 'tess/tesseract.exe'
        img = Image.open(pic)
        text = pytesseract.image_to_string(img, lang=nat)
        context.update({
            "con" : text,
            "nat" : nat
        })
    return render(request, "ocr/index.html", context)



