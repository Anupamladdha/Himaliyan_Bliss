from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView,FormView,View,DeleteView
from django.urls import reverse,reverse_lazy
from .models import Room, Booking,Contact,Event
from .forms import AvailabilityForm
from hotel.booking_functions.availability import check_availability
from hotel.booking_functions.get_room_cat_url_list import get_room_cat_url_list
from hotel.booking_functions.get_room_category_human_format import get_room_category_human_format
from hotel.booking_functions.get_available_rooms import get_available_rooms
from hotel.booking_functions.book_room import book_room
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from datetime import datetime
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def RoomListView(request):
    get_room_category_url_list=get_room_cat_url_list()
    context={
        "room_list":get_room_category_url_list,
    }
    # print(context["room_list"])
    return render(request,'room_list_view.html',context)

def EventBookView(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone') 
        eventtype=request.POST.get('eventtype') 
        eventdate=request.POST.get('eventdate') 
        desc=request.POST.get('desc') 
        event=Event(name=name,email=email,phone=phone,eventtype=eventtype,eventdate=eventdate,desc=desc,date=datetime.today())
        event.save()
        messages.success(request, 'Your message has been sent')
    return render(request,'event_book_view.html')

def base(request):
    return render(request,'base.html')

def SpaView(request):
    return render(request,'spa_view.html')

def GalleryView(request):
    return render(request,'gallery_view.html')

def ThingsView(request):
    return render(request,'things2do.html')

def RoomFullView(request):
    return render(request,'room_full_view.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone') 
        desc=request.POST.get('desc') 
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request,'contactus_view.html')

class BookingListView(ListView):
    model=Booking
    # template_name = 'booking_list_view.html'
    def get(self,request,*args,**kwargs):
        if self.request.user.is_staff:
            booking_list=Booking.objects.all()
            # return booking_list
            context={
                'booking_list':booking_list,
            }
            return render(request,'booking_list_view.html',context)
        else:
            if self.request.user.is_anonymous:
                return redirect('/accounts/login')
            booking_list=Booking.objects.filter(user=self.request.user)
            # return booking_list
            context={
                'booking_list':booking_list,
            }
            return render(request,'booking_list_view.html',context)

class RoomDetailView(View):
    def get(self,request,*args,**kwargs):
        if self.request.user.is_anonymous:
            return redirect('/accounts/login')
        
        category = self.kwargs.get('category', None)
        human_format_room_category=get_room_category_human_format(category)
        form=AvailabilityForm()
        if human_format_room_category is not None:
            room_rate=Room.objects.filter(category=category)[0].rate
            room_descs=dict(Room.ROOM_DESCS)
            room_desc=room_descs.get(category)
            room_details=dict(Room.ROOM_DETAILS)
            room_detail=room_details.get(category)
            context={
                'room_category':human_format_room_category,
                'category':category,
                'form':form,
                'room_rate':room_rate,
                'room_desc':room_desc,
                'room_detail':room_detail

            }
            return render(request,'room_detail_view.html',context)
        else:
            return  HttpResponse("Category does not exists")


    def post(self,request,*args,**kwargs):
        category = self.kwargs.get('category',None)
        
        form=AvailabilityForm(request.POST)

        if form.is_valid():
            data=form.cleaned_data

        client = razorpay.Client(auth=("rzp_test_v9Yll7cN20PlKo", "in8gnde7EZEQaGZ55Cp8mBCG"))
        callback_url = 'http://127.0.0.1:8000/success/'
        email = self.request.user.email

        date_format = "%Y-%m-%d"
        a = datetime.strptime(str(data['check_in']), date_format)
        b = datetime.strptime(str(data['check_out']), date_format)
        delta = b - a
        print(delta.days)
        # print(data['check_in'])
        available_rooms=get_available_rooms(category,data['check_in'],data['check_out'])
        print(available_rooms)

        
        if available_rooms is not None:
            print(f'------{available_rooms[0].rate}-----')
            rate = available_rooms[0].rate
            room_categories=dict(available_rooms[0].ROOM_CATEGORIES)
            room_category=room_categories.get(available_rooms[0].category)
            order = client.order.create(dict(amount = rate*100*delta.days, currency = 'INR', payment_capture = '0' ))
            print(f'------{order}-----')
            book_room(request,available_rooms[0],data['check_in'],data['check_out'], order['id'], rate*delta.days)

            return render(self.request, 'payment_summary.html', {'order' : order,'check_in' : data['check_in'],'check_out' : data['check_out'], 'room' : room_category,'amount' : rate*delta.days, 'id' : order['id'], 'email' : email, 'callback_url' : callback_url})
        else:
            return redirect('hotel:RoomFullView')
        


@csrf_exempt
def success(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    # client instance
    client = razorpay.Client(auth=("rzp_test_v9Yll7cN20PlKo", "in8gnde7EZEQaGZ55Cp8mBCG"))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        room_book = Booking.objects.get(order_id=response['razorpay_order_id'])
        room_book.payment_id = response['razorpay_payment_id']
        room_book.paid = True
        room_book.save()
        return redirect('hotel:BookingListView')
    except:
        return render(request, "success.html")
    return render(request, "success.html")

def payment(request):
    return render(request, "payment_summary.html")


class CancelBookingView(DeleteView):
    model=Booking
    template_name='booking_cancel_view.html'
    success_url=reverse_lazy('hotel:BookingListView')

def booking_render_pdf_view(self,*args, **kwargs):
    pk=kwargs.get('pk')
    booking=get_object_or_404(Booking,pk=pk)
    room_categories=dict(booking.room.ROOM_CATEGORIES)
    room_category=room_categories.get(booking.room.category)
    template_path = 'booking_print_view.html'
    context = {'booking': booking,'room_category':room_category}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = '; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'booking_print_view.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = '; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
