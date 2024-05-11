from django.shortcuts import render
from .models import Coffee
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount_str = request.POST.get('amount')
        print(name, '--------', amount_str)
        amount = int(float(amount_str) * 100)
        client = razorpay.Client(auth=('rzp_test_MNYcVHDelhc8O9', 'aBpNNAPNuhDe35HyfgKsL5vi'))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        coffee = Coffee(name=name, amount=amount, payment_id=payment['id'])
        coffee.save()
        return render(request, 'app1/home.html', {'payment': payment})
    return render(request, 'app1/home.html')

@csrf_exempt
def success(request):
    if request.method == 'POST':
        a = request.POST
        order_id =''
        for key, value in a.items():
            if key == 'razorpay_order_id':
                order_id = value
                break
        print(order_id)
        user = Coffee.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
    return render(request, 'app1/success.html')