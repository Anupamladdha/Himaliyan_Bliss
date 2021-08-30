from django.urls import path
from .views import RoomListView,BookingListView,RoomDetailView,CancelBookingView,render_pdf_view,booking_render_pdf_view,SpaView,GalleryView,contact,base,RoomFullView, success, payment,EventBookView, ThingsView

app_name='hotel'

urlpatterns = [
    path('', RoomListView,name='RoomListView'),
    path('room_list/', RoomListView,name='RoomListView'),
    path('booking_list/', BookingListView.as_view(),name='BookingListView'),
    path('room/<category>', RoomDetailView.as_view(),name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),name='CancelBookingView'),
    path('booking/print/<pk>', booking_render_pdf_view,name='booking_render_pdf_view'),
    path('spa/', SpaView,name='SpaView'),
    path('gallery/', GalleryView,name='GalleryView'),
    path('contact/', contact,name='contact'),
    path('base/', base,name='base'),
    path('room_full/', RoomFullView,name='RoomFullView'),
    path('success/', success, name='success'),
    path('payment/', payment, name='payment'),
    path('eventbook/', EventBookView, name='EventBookView'),
    path('things2do/', ThingsView, name='ThingsView')
]
