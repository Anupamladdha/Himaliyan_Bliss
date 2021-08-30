from hotel.models import Booking,Room

def book_room(request,room,check_in,check_out,order_id, amount):
    booking=Booking.objects.create(
    user=request.user,
    room=room,
    check_in=check_in,
    check_out=check_out,
    amount=amount,
    order_id=order_id
    )
    booking.save()