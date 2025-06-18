from django.shortcuts import render
from .models import Tickets
from lookups.models import Department, Category
from .forms import CreateTicketForm

def home(request):
    return render(request, "home.html")

def index(request):

    tickets = Tickets.objects.filter(user=request.user).order_by("-created_at")  # ← pastikan ada model Tickets dan filter mengikut pengguna
   # breakpoint() 
    context = {
        "tickets": tickets,
    }
    return render(request, "tickets/index.html", context)  # ← pastikan ada template untuk index
    pass  # ← pastikan ada fungsi index walaupun kosong

def create(request):
    form = CreateTicketForm()  # ← pastikan form wujud untuk GET dan fallback

    if request.method == "POST":
        print("Form submitted")
        print("Form data", request.POST)

        form = CreateTicketForm(request.POST)  # ← inisialisasi form dengan data POST

        if form.is_valid():
            pass

            # Ambil data dari borang
            title = request.POST.get("title", "")
            description = request.POST.get("description", "")
            category_id = request.POST.get("category_id", "")
            department_id = request.POST.get("department_id", "")

            user = request.user

            # Semak jika semua maklumat diisi
            if title and category_id and department_id:
                try:
                    department = Department.objects.get(id=int(department_id))
                    category = Category.objects.get(id=int(category_id))

                    Tickets.objects.create(
                        title=title,
                        description=description,
                        user=user,
                        department=department,
                        category=category,
                    )
                    print("Tiket berjaya dihantar.")

                except Exception as e:
                    print("Ralat semasa cipta tiket:", e)
        else:
            print("Sila lengkapkan semua maklumat yang diperlukan.")

    departments = Department.objects.all()
    categories = Category.objects.all()

    context = {
        "departments": departments,
        "categories": categories,
        "form": form,
    }

    return render(request, "tickets/create.html", context)
