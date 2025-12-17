from django.db import models
from django.conf import settings
from django.utils import timezone

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    locations = models.TextField()
    type = models.CharField(max_length=222, null=True, blank=True)

    def __str__(self):
        return f"Номер приміщення #{self.number} - {self.capacity}, тип приміщення#{self.type}"
    
    def get_status(self):
        now = timezone.now()
        currunt_booking = Booking.objects.filter(
            room=self,
            start_time__lte=now,
            end_time__gte=now,
            ).first()
        if currunt_booking:
            return f"Occupate to {currunt_booking.end_time}"
        
        return "Free for reservation"
        
    class Meta:
        verbose_name = "Приміщення"
        verbose_name_plural = "Приміщення"
        ordering = ["number"]

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    all_rooms = models.ForeignKey(Room, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(blank=True)  
    username = models.CharField(max_length=256, default='user', blank=True)

    def __str__(self):
        return f"{self.user} {self.phone_number}"
    
    class Meta:
        verbose_name = "Користувач/ка"
        verbose_name_plural = "Користувачі"
        ordering = ["user"]

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user}# Booking, {self.room}"
    
    
    @property
    def user_email(self):
        return self.user.email
    
    @property
    def user_name(self):
        return self.user.username

    class Meta:
        verbose_name = "Резервування"
        verbose_name_plural = "Резервування"
        ordering = ["start_time"]