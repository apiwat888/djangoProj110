

from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def edu(request):
    return render(request, 'edu.html')


def interests(request):
    return render(request, 'interests.html')


def product(request):
    return render(request, 'product.html')


def rolemodel(request):
    return render(request, 'rolemodel.html')


def showdata(request):
    STDID = "65342310110-0"
    name = "นายอภิวัฒน์ มะลิวงศ์"
    address = "อ.กุดจับ ต.กุดจับ จ.อุดรธานี"
    Domicile = "อุดรธานี"
    gender = "ชาย"
    weight = "54 ก.ก"
    height = "167 ซ.ม"
    colors = "Navy Blue"
    food = "หมูกะทะ"
    work = "นักศึกษา"
    products = [
                ["ผ่าพิภพไททัน : Attack on Titan", " 81/เล่ม","images/ah.jpg"],
                ["DR.STONE Our Stone World", " 63/เล่ม","images/dr.png"],
                ["Chain saw man", " 63/เล่ม","images/ch.png"],
                ["ขังดวลแข้ง BLUELOCK", " 90/เล่ม","images/1000_.jpg"],
                ["วัน พีซ - One Piece", " 125/เล่ม","images/One_piece.jpg"],
                ["Jujutsu kaisen-มหาเวทย์ผนึกมาร", " 72/เล่ม","images/ju_.jpg"],
                ["SPYx FAMILY", " 99/เล่ม","images/spy.png"],
                ["ไฮคิว!! คู่ตบฟ้าประทาน", " 59/เล่ม","images/cover.png"],
                ["ดาบพิฆาตอสูร", " 65/เล่ม","images/ki.png"],
                ["Record of Ragnarok มหาศึกคนชนเทพ", " 115/เล่ม","images/XXL.jpg"]
                ]
    context = {'STDID': STDID, 'name': name, ' address': address,
               'Domicile': Domicile, 'gender': gender, 'weight': weight,
               'height': height, 'colors': colors, 'food': food, 'work': work,
               'products': products}
    return render(request, "showdata.html", context)
