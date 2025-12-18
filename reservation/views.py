from django.shortcuts import render, redirect
from reservation.models import Room, Booking, Profile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


@login_required
def index(request):
   
    num_rooms = Room.objects.count()
    num_booking = Booking.objects.count()


    context = {
        "num_rooms": num_rooms,
        "num_booking": num_booking,
        "num_of_free_room": num_rooms - num_booking,
    }

    return render (request, template_name="booking/index.html", context=context)
    

def room_list(request):
    now = timezone.now()

    occupied_room_ids = Booking.objects.filter(
        start_time__lte=now,
        end_time__gte=now,
    ).values_list('room_id', flat=True)
    rooms = Room.objects.exclude(id__in=occupied_room_ids)
    
    context = {'rooms': rooms}
    return render(request, 
              "booking/rooms_list.html", 
              context)

@login_required
def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room_number")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        try:
            room = Room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse(
                "Wrong value for room number",
                status=400
            )
        except Room.DoesNotExist:
            return HttpResponse(
                "This room number doesn't exist",
                status=404
            )
        
        overlapping = Booking.objects.filter(
            room=room,
            start_time__lte=end_time,
            end_time__gte=start_time,
            ).exists()
        
        if overlapping:
            messages.error(request, "This room already occupation at this time")
            return redirect("book_room")

        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time,

        )
        return redirect("booking_details", pk=booking.id)
    

    


    else:
        return render(request, template_name="booking/booking_form.html")


def booking_details(request, pk):
    try: 
        booking = Booking.objects.get(id=pk)
        context = {
            "booking": booking
        }
        return render(request, template_name="booking/booking_details.html", context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            "This boooking doesn't exist",
            status=404
        )
    

@login_required
def profile_details(request):
    user = request.user
    
    context = {
        'user': user,
    }

    return render(
            request,
            template_name='booking/profile.html',
            context=context)
