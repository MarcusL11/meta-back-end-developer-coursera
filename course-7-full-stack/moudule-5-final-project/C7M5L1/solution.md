# Solution: Little Lemon booking system
## Part 1:  Connect the Little Lemon back-end to MySQL
### Step 1:

```bash
mysql -u root -p  OR

sudo mysql -u root -p 
```
### Step 2:

```sql 
CREATE DATABASE reservations;
```
### Step 3:

```sql 
SHOW DATABASES;
```
### Step 7:

```sql
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!' ;
```
### Step 8:

```sql 
GRANT ALL ON *.* TO 'admindjango'@'localhost';
```
### Step 9:

```sql 
FLUSH PRIVILEGES;
```
### Step 10:

```sql 
exit;
```
### Step 11:

### settings.py
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reservations',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : 'admindjango', # based on your setup
        'PASSWORD' : 'employee@123!', # based on your setup
    }
}
```

### Part 2: Exercise: Set up a Little Lemon booking API

### forms.py

```py
from django.forms import ModelForm
from .models import Booking

# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
```
### views.py
```py
def bookings(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})
```
### booking.html
```html
// Step 10
<h1>Make a reservation</h1>

// Step 11
<script>
  console.log("Hello");
  document.getElementById("id_reservation_date").type="date"
</script>
```
### bookings.html

```html
// Step 12
<h1>All Reservations</h1>

// Step 13
<script>
  // Note that the |safe filter is used in the template to mark the bookings variable as safe, indicating that it should not be escaped or sanitized. This is necessary when rendering JSON data within a template. // 
  const bookings = JSON.parse('{{ bookings|safe }}') 
  console.log(bookings);
  const pretty_json = JSON.stringify(bookings,null,2)
  document.getElementById('bookings').innerHTML = pretty_json
</script>
```

### index.html
```html
<a href="{% url 'book' %}">Book your table now</a>
```

### _header.html
```html
<li><a href="{% url 'book' %}">Book</a></li>
<li><a href="{% url 'bookings' %}">Reservations</a></li>
```

## Part 3 Exercise: Display the Little Lemon available booking times
### views.py

```py 
@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')
    
```
### templates/book.html - Part 1
```html
    <label for="reservation_date">Reservation date:</label>
    <input type="date" id="reservation_date">
```
### templates/book.html - Part 2
```js
  document.getElementById('reservation_date').addEventListener('change', function () {
    getBookings()
  })
```

### templates/book.html - Part 3
```js
for (item of data) {
          console.log(item.fields)
          reserved_slots.push(item.fields.reservation_slot)
          bookings += `<p>${item.fields.first_name} - ${formatTime(item.fields.reservation_slot)}</p>`
        }
```

### templates/book.html - Part 4
```js
slot_options = '<option value="0" disabled>Select time</option>'
        for (i = 10; i <= 20; i++) {
          const label = formatTime(i)
          if (reserved_slots.includes(i)) {
            slot_options += `<option value=${i} disabled>${label}</option>`
          } else {
            slot_options += `<option value=${i}>${label}</option>`
          }

        }
```

## Complete templates/book.html file for cross-reference
```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
<section>
  <article>
    <h1>Make a reservation</h1>
    <!--Begin row-->
    <div class="row">
      <!--Begin col-->
      <div class="column">
          {% csrf_token %}
          <form method="POST" id="form">
            <!-- {% csrf_token %} -->
            <p>
              <label for="first_name">Name:</label>
              <input type="text" placeholder="Your Name" maxlength="200" required="" id="first_name">
            </p>
            <p>
              <label for="reservation_date">Reservation date:</label>
              <input type="date" id="reservation_date">
            </p>
      
            <p>
              <label for="reservation_slot">Reservation time:</label>
              <select id="reservation_slot">
                <option value="0" disabled>Select time</option>
              </select>
            </p>
            <button type="button" id="button">Reserve</button>
          </form>
      </div>
      <!--End col-->

      <!--Begin col-->
      <div class="column">
        <h2>Bookings For <span id="today"></span></h2>
        <div id="bookings">
        </div>
      </div>
      <!--End col-->
    </div>
    <!--End row-->




  </article>
</section>
<script>

  const date = new Date()
  document.getElementById('reservation_date').value = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, "0")}-${date.getDate().toString().padStart(2, "0")}`

  console.log(document.getElementById('reservation_date').value)
  getBookings()


  document.getElementById('reservation_date').addEventListener('change', function () {
    getBookings()
  })


  function getBookings() {
    let reserved_slots = []
    const date = document.getElementById('reservation_date').value
    document.getElementById('today').innerHTML = date
    
    fetch("{% url 'bookings' %}" + '?date=' + date)
      .then(r => r.json())
      .then(data => {
        reserved_slots = []
        bookings = ''
        for (item of data) {
          console.log(item.fields)
          reserved_slots.push(item.fields.reservation_slot)
          bookings += `<p>${item.fields.first_name} - ${formatTime(item.fields.reservation_slot)}</p>`
        }

        slot_options = '<option value="0" disabled>Select time</option>'
        for (i = 10; i <= 20; i++) {
          const label = formatTime(i)
          if (reserved_slots.includes(i)) {
            slot_options += `<option value=${i} disabled>${label}</option>`
          } else {
            slot_options += `<option value=${i}>${label}</option>`
          }

        }
        
        document.getElementById('reservation_slot').innerHTML = slot_options
        if(bookings==''){
          bookings = "No bookings"
        }
        document.getElementById('bookings').innerHTML = bookings
      })
  }

  function formatTime(time) {
    const ampm = time < 12 ? 'AM' : 'PM'
    const t = time < 12 ? time : time > 12 ? time - 12 : time
    const label = `${t} ${ampm}`
    return label
  }


  document.getElementById('button').addEventListener('click', function (e) {
    const formdata = {
      first_name: document.getElementById('first_name').value,
      reservation_date: document.getElementById('reservation_date').value,
      reservation_slot: document.getElementById('reservation_slot').value,
    }

    fetch("{% url 'bookings' %}", { method: 'post', body: JSON.stringify(formdata) })
      .then(r => r.text())
      .then(data => {
        getBookings()
      })
  })
</script>
{% endblock %}


```