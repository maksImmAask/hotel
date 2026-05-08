from datetime import date

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, BookingForm
from .models import Room, Booking



def home(request):

    rooms = Room.objects.all()

    room_type = request.GET.get('type')
    capacity = request.GET.get('capacity')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if room_type:
        rooms = rooms.filter(room_type=room_type)

    if capacity:
        rooms = rooms.filter(capacity=capacity)

    if min_price:
        rooms = rooms.filter(price__gte=min_price)

    if max_price:
        rooms = rooms.filter(price__lte=max_price)

    context = {
        'rooms': rooms
    }

    return render(request, 'home.html', context)



def room_detail(request, pk):

    room = get_object_or_404(Room, id=pk)

    form = BookingForm()

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return redirect('login')

        form = BookingForm(request.POST)

        if form.is_valid():

            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            if check_in < date.today():
                form.add_error('check_in', 'Past date is not allowed')

            elif check_out <= check_in:
                form.add_error('check_out', 'Check-out must be after check-in')

            else:

                conflict = Booking.objects.filter(
                    room=room,
                    status='confirmed',
                    check_in__lt=check_out,
                    check_out__gt=check_in
                ).exists()

                if conflict:
                    form.add_error(None, 'Room already booked for these dates')

                else:
                    booking = form.save(commit=False)
                    booking.user = request.user
                    booking.room = room
                    booking.save()

                    return redirect('profile')

    context = {
        'room': room,
        'form': form
    }

    return render(request, 'room_detail.html', context)



def register_view(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'register.html', {'form': form})



def login_view(request):

    form = AuthenticationForm(data=request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')

    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')



@login_required
def profile(request):

    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'profile.html', {
        'bookings': bookings
    })



@login_required
def cancel_booking(request, pk):

    booking = get_object_or_404(
        Booking,
        id=pk,
        user=request.user
    )

    booking.status = 'cancelled'
    booking.save()

    return redirect('profile')