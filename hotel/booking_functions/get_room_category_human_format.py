from hotel.models import Room

def get_room_category_human_format(category):
    room=Room.objects.all()[0]
    room_category=dict(room.ROOM_CATEGORIES).get(category,None)
    return room_category