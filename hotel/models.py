from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES=(
        ('PR','PREMIUM ROOM'),
        ('SU','SUPERIOR ROOM'),
        ('SR','SUITE ROOM'),
        ('HS','HILL VIEW SUITE'),
        ('PS','PRESIDENTIAL SUITE'),
    )
    ROOM_DESCS=(
        ('PR','Ideal for a family of 2-3, these rooms are approximately 200 to 300 sq. ft. in size and have mini refrigerator, hair dryer, complimentary tea/coffee maker, heating system, hot & cold water facility.'),
        ('SU','Approximately 200 to 300 sq. ft. in size, surrounded by a spectacular mountain & garden view, each of these rooms has a mini refrigerator, hair dryer, tea/coffee maker, centralised heating system and hot & cold water facility.'),
        ('SR','About 300 to 350 sq. ft. in size, with 2 rooms – one master bed room and one sitting room – along with a sofa cum bed, these rooms have a mini refrigerator, hair dryer, tea/coffee maker, Heating system, Hot & Cold water facility and 2 TVs.'),
        ('HS','Approximately 300 to 350 sq. ft. in size, with 2 rooms and surrounding view of mountains, these rooms have mini refrigerator, hair dryer, tea and coffee maker, centralised Heating system, hot & cold water facility and 2 TVs.'),
        ('PS','Spread over 600 sq. ft., this suite is the best in Nainital that offers an array of facilities including a valet for the entire stay. It can accommodate a family of up to 4 people and comes equipped with a built-in bar and sitting area.'),
    )
    ROOM_DETAILS=(
            ('PR',['Centrally Hot and Cold Water','TV with Cable connection','Direct dailing','Writing Desk','Wardrobe','Tea and coffee-maker','Sitting out area and face the lawns','New and better quality mattress','Room linen']),
            ('SU',['Room facilities are furnished with aesthetic luxury','Centrally Hot & Cold Water','TV with cable connection','Direct dialing','Writing Desk','Wardrobe','Tea and coffee-maker']),
            ('SR',['Centrally Hot & Cold Water','2 Flat screen TV','Direct dialing','Writing Desk','Wardrobe','Tea and coffee-maker','Mini refrigerator']),
            ('HS',['Aesthetic luxury','Centrally Hot & Cold Water','TV with cable connection','Direct dialing','Writing Desk','Wardrobe','Tea and coffee-maker','Mini bar']),
            ('PS',['Aesthetic luxury','Centrally Hot & Cold Water','TV with cable connection','Direct dailing','Writing Desk','Wardrobe','Tea and coffee-maker']),
        )
    number = models.IntegerField()
    category=models.CharField(max_length=3,choices=ROOM_CATEGORIES)
    beds=models.IntegerField()
    capacity=models.IntegerField()
    rate=models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'
    
    

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    amount= models.CharField(max_length=100, default=0)
    paid=models.BooleanField(default= False)
    order_id=models.CharField(max_length=100, default='a')
    payment_id=models.CharField(max_length=100, default='a')
    

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
    
    def get_room_category(self):
        room_categories=dict(self.room.ROOM_CATEGORIES)
        room_category=room_categories.get(self.room.category)
        return room_category
    
    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBookingView',args=[self.pk, ])
    
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    eventtype=models.CharField(max_length=122)
    eventdate=models.DateField()
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
    