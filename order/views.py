from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from order.forms import OrderCreateForm
from order.models import Order, OrderItem
from cart.helpers import Cart
from django.contrib.admin.views.decorators import staff_member_required


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
        return render(self.request, 'created.html', {'order': order})

def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'history.html', {'orders': orders})

def order_history_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    order_items = order.items.all()
    return render(request, 'history_detail.html', locals())
