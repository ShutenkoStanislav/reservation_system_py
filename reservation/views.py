from django.shortcuts import render, redirect, get_object_or_404
from reservation.models import Room, Booking, Profile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone



@login_required
def index(request):
   
    num_rooms = Room.objects.count()
    num_booking = Booking.objects.count()
    num_types = Room.objects.values('type').distinct().count()


    context = {
        "num_rooms": num_rooms,
        "num_booking": num_types,
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

def room_details(request, room_id):
    room_infa = get_object_or_404(Room, id=room_id)
    context = {'room_infa': room_infa}
    return render(request,
                  "booking/room_detail.html",
                  context)

@login_required
def book_room(request, room_id):
    if request.method == "POST":
       
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        
        room = get_object_or_404(Room, id=room_id)
       
        
        overlapping = Booking.objects.filter(
            room=room,
            start_time__lte=end_time,
            end_time__gte=start_time,
            ).exists()
        
        if overlapping:
            messages.error(request, "This room already occupation at this time")
            return redirect("book_room", room_id=room_id)

        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time,

        )
        return redirect("booking_details", pk=booking.id)
    

    


    else:
        room = get_object_or_404(Room, id=room_id)
        return render(request, "booking/booking_form.html", {'room': room})


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


def booking_types(request):
    room_types = Room.objects.values_list('type', flat=True).distinct()
    
    rooms_by_type = {}
    for room_type in room_types:
        rooms_by_type[room_type] = Room.objects.filter(type=room_type)
    
    context = {'rooms_by_type': rooms_by_type}
    return render(request, 'booking/booking_type.html', context)
