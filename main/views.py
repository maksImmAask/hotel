from datetime import date

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

from .forms import RoomForm
from .forms import RegisterForm, BookingForm
from .models import Room, Booking
from .models import RoomImage
from django.contrib.auth.forms import UserCreationForm


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
    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = AuthenticationForm(data=request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')

    return render(request, 'login.html', {'form': form})


@login_required
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

@staff_member_required
def admin_dashboard(request):

    rooms_count = Room.objects.count()
    bookings_count = Booking.objects.count()
    users_count = User.objects.count()

    context = {
        'rooms_count': rooms_count,
        'bookings_count': bookings_count,
        'users_count': users_count,
    }

    return render(request, 'admin/dashboard.html', context)


@staff_member_required
def admin_rooms(request):

    rooms = Room.objects.all()

    return render(request, 'admin/rooms.html', {
        'rooms': rooms
    })

@staff_member_required
def admin_create_room(request):

    form = RoomForm()

    if request.method == 'POST':

        form = RoomForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            room = form.save()

            image = request.FILES.get('image')

            if image:
                RoomImage.objects.create(
                    room=room,
                    image=image
                )

            return redirect('admin_rooms')

    return render(request, 'admin/create_room.html', {
        'form': form
    })


@staff_member_required
def admin_edit_room(request, pk):

    room = get_object_or_404(Room, id=pk)

    form = RoomForm(instance=room)

    if request.method == 'POST':

        form = RoomForm(
            request.POST,
            request.FILES,
            instance=room
        )

        if form.is_valid():

            room = form.save()

            image = request.FILES.get('image')

            if image:

                RoomImage.objects.create(
                    room=room,
                    image=image
                )

            return redirect('admin_rooms')

    return render(request, 'admin/edit_room.html', {
        'form': form,
        'room': room
    })

@staff_member_required
def admin_delete_room(request, pk):

    room = get_object_or_404(Room, id=pk)

    room.delete()

    return redirect('admin_rooms')


@staff_member_required
def admin_bookings(request):

    bookings = Booking.objects.all()

    return render(request, 'admin/bookings.html', {
        'bookings': bookings
    })
@staff_member_required
def admin_confirm_booking(request, pk):

    booking = get_object_or_404(Booking, id=pk)

    if booking.status == 'confirmed':
        return redirect('admin_bookings')

    conflict = Booking.objects.filter(
        room=booking.room,
        status='confirmed',
        check_in__lt=booking.check_out,
        check_out__gt=booking.check_in
    ).exclude(id=booking.id).exists()

    if conflict:
        return redirect('admin_bookings')

    booking.status = 'confirmed'
    booking.save()

    return redirect('admin_bookings')
@staff_member_required
def admin_cancel_booking_panel(request, pk):

    booking = get_object_or_404(Booking, id=pk)

    booking.status = 'cancelled'
    booking.save()

    return redirect('admin_bookings')
@staff_member_required
def admin_users(request):

    users = User.objects.all()

    return render(request, 'admin/users.html', {
        'users': users
    })
@staff_member_required
def admin_create_user(request):

    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('admin_users')

    return render(request, 'admin/create_user.html', {
        'form': form
    })
@staff_member_required
def admin_edit_user(request, pk):

    user_item = get_object_or_404(User, id=pk)

    if request.method == 'POST':

        user_item.username = request.POST.get('username')

        user_item.email = request.POST.get('email')

        user_item.is_staff = bool(
            request.POST.get('is_staff')
        )

        user_item.save()

        return redirect('admin_users')

    return render(request, 'admin/edit_user.html', {
        'user_item': user_item
    })
@staff_member_required
def admin_delete_user(request, pk):

    user_item = get_object_or_404(User, id=pk)

    user_item.delete()

    return redirect('admin_users')