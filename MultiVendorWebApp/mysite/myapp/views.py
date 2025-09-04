from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,OrderDetail
from django.conf import settings
from instamojo_wrapper import Instamojo
import uuid
from .forms import ProductForm,UserRegistrationForm
from django.db.models import Sum
import datetime
# Create your views here.

def index(request):
    products=Product.objects.all()

    return render(request,'myapp/index.html',{'products':products})

def detail(request, id):
    product = Product.objects.get(id=id)
    # Razorpay ka code hata diya
    return render(request, 'myapp/detail.html', {'product': product})

# Initialize Instamojo client
mojo = Instamojo(api_key=settings.INSTAMOJO_API_KEY,
                 auth_token=settings.INSTAMOJO_AUTH_TOKEN,
                 endpoint=settings.INSTAMOJO_ENDPOINT)


def instamojo_checkout(request, id):
    product = get_object_or_404(Product, id=id)
    try:
        response = mojo.payment_request_create(
            amount=str(product.price),
            purpose=product.name,
            buyer_name=request.user.username,
            email=request.user.email,
            redirect_url=settings.INSTAMOJO_REDIRECT_URL,
            send_email=False
        )
        print("DEBUG RESPONSE:" , response)  # DEBUG
        # Create OrderDetail in DB
        order = OrderDetail.objects.create(
            product=product,
            customer_email=request.user.email,
            instamojo_payment_request_id=response['id'],
            amount=product.price,
            currency='INR',
            payment_status='created'
        )
        # Redirect to Instamojo payment page
        return redirect(response['longurl'])
    except Exception as e:
        return render(request, 'myapp/failure.html', {'error': str(e)})


def instamojo_success(request):
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    payment_status = request.GET.get('payment_status')

    order = get_object_or_404(OrderDetail, instamojo_payment_request_id=payment_request_id)

    if payment_status == 'Credit':
        order.payment_status = 'paid'
        order.instamojo_payment_id = payment_id
        order.save()
        return render(request, 'myapp/success.html', {'order': order})
    else:
        order.payment_status = 'failed'
        order.save()
        return render(request, 'myapp/failure.html', {'order': order})






def create_product(request):
    if request.method=="POST":
        product_form=ProductForm(data=request.POST,files=request.FILES)
        if product_form.is_valid():
            new_product=product_form.save(commit=False)
            new_product.seller=request.user
            new_product.save()
            return redirect('index')
        
    product_form=ProductForm()    
    return render(request,'myapp/create_product.html',{'product_form':product_form})

def edit_product(request,id):
        product=Product.objects.get(id=id)
        if product.seller!=request.user:
            return redirect('invalid')
        product_form=ProductForm(data=request.POST or None,files=request.FILES or None,instance=product)
        if request.method=="POST":
            if product_form.is_valid():
                product_form.save()
                return redirect('index')
          
        return render(request,'myapp/edit_product.html',{'product_form':product_form,'product':product})


def delete(request,id):
    product=Product.objects.get(id=id)
    if product.seller!=request.user:
        return redirect('invalid')
    if request.method=="POST":
        product.delete()
        return redirect('index')
    return render(request,'myapp/delete.html',{'product':product})

def dashboard(request):
    products= Product.objects.filter(seller=request.user)
    return render(request,'myapp/dashboard.html',{'products':products}) 

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])  # use 'password'
            new_user.save()
            return redirect('index')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'myapp/register.html', {'user_form': user_form})


def invalid(request):
    return render(request,'myapp/invalid.html')

def my_purchases(request):
    orders=OrderDetail.objects.all()
    return render(request,'myapp/purchase.html',{'orders':orders})

def sales(request):
    orders=OrderDetail.objects.filter(product__seller=request.user)
    total_sales=orders.aggregate(Sum('amount'))
    # 365 days sales sum
    last_year=datetime.date.today()-datetime.timedelta(days=365)
    data=OrderDetail.objects.filter(product__seller=request.user,created_at__gt=last_year)
    yearly_sales=data.aggregate(Sum('amount'))
    
    # 30 days sales sum
    last_month=datetime.date.today()-datetime.timedelta(days=30)
    data=OrderDetail.objects.filter(product__seller=request.user,created_at__gt=last_month)
    monthly_sales=data.aggregate(Sum('amount'))

    # 7 days sales sum
    last_week=datetime.date.today()-datetime.timedelta(days=7)
    data=OrderDetail.objects.filter(product__seller=request.user,created_at__gt=last_week)
    weekly_sales=data.aggregate(Sum('amount'))

    # work on this
    daily_sums=OrderDetail.objects.filter(product__seller=request.user).values('created_at__date').order_by('created_at__date').annotate(sum=Sum('amount'))

    product_sales_sums=OrderDetail.objects.filter(product__seller=request.user).values('product__name').order_by('product__name').annotate(sum=Sum('amount'))
    print(product_sales_sums)

    return render(request,'myapp/sales.html',{'total_sales':total_sales,'yearly_sales':yearly_sales,'monthly_sales':monthly_sales,'weekly_sales': weekly_sales,'product_sales_sums':product_sales_sums,'daily_sums':daily_sums})














