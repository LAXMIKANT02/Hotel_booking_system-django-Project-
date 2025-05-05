from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Room, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'booking/home.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    rooms = hotel.room_set.all()
    return render(request, 'booking/hotel_detail.html', {'hotel': hotel, 'rooms': rooms})

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            return render(request, 'booking/booking_success.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'booking/book_room.html', {'form': form, 'room': room})
