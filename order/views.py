import braintree
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from order.forms import OrderCreateForm
from order.models import Order, OrderItem
from cart.helpers import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required



class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'order_create.html'
    success_url = reverse_lazy('products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form(self.get_form_class())
        return context

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()
        order_items = [OrderItem(order=order,
        product=obj['product'],
        quantity=obj['quantity'],
        )
        for obj in cart]
        OrderItem.objects.bulk_create(order_items)
        cart.clear()
        return render(self.request, 'success_delivery.html', {'order': order})

def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'history.html', {'orders': orders})

def order_history_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    order_items = order.items.all()
    return render(request, 'history_detail.html', locals())


@login_required
def checkout_page(request):
    #generate all other required data that you may need on the #checkout page and add them to context.
    if settings.BRAINTREE_PRODUCTION:
        braintree_env = braintree.Environment.Production
    else:
        braintree_env = braintree.Environment.Sandbox

    # Configure Braintree
    braintree.Configuration.configure(
        braintree_env,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY,
    )
 
    try:
        braintree_client_token = braintree.ClientToken.generate({ "customer_id": user.id })
    except:
        braintree_client_token = braintree.ClientToken.generate({})

    context = {'braintree_client_token': braintree_client_token}
    return render(request, 'checkout.html', context)

@login_required
def payment(request):
    pay_id = 6
    session = request.session.get('cart')
    print(session)
    cart = session.get(str(pay_id))
    price = cart.get('price')
    quantity = cart.get('quantity')
    total = float(price) * float(quantity)
    nonce_from_the_client = request.POST['paymentMethodNonce']
    customer_kwargs = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
    }
    customer_create = braintree.Customer.create(customer_kwargs)
    customer_id = customer_create.customer.id
    result = braintree.Transaction.sale({
        "amount": int(total),
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    
    return HttpResponse('Ok')