from hotel.models import Room
from django.urls import reverse

def get_room_cat_url_list():
    room=Room.objects.all()[0]
    # print(room)
    room_cat_url_list=[]
    room_categories=dict(room.ROOM_CATEGORIES)
    room_descs=dict(room.ROOM_DESCS)
    for category in room_categories:
        room_category=room_categories.get(category)
        room_img_url=f'hotel/images/{category}.jpg'
        room_rate=Room.objects.filter(category=category)[0].rate
        room_desc=room_descs.get(category)
        room_url=reverse('hotel:RoomDetailView', kwargs={'category':category})
        room_cat_url_list.append((room_category,room_img_url,room_rate,room_desc,room_url))
        # print(type(room_img_url)
    # print(room_cat_url_list)
    return room_cat_url_list