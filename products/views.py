from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Review
from profiles.models import UserProfile
from .forms import PhotoForm

# Create your views here.


def upload(request):
    """
    Connecting to cloudinary to allow file upload
    """
    context = dict(backend_form=PhotoForm())

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)


def products(request):
    """
    A view to display all products, including sorting and search queries.
    """

    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)

            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request,
                                   "Ups, you didn't enter\
                                   any search criteria!")
                    return redirect(reverse('products'))

                queries = (
                           Q(name__icontains=query) |
                           Q(description__icontains=query)
                )
                products = products.filter(queries)
            # add sorting products ascending
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'category':
                    sortkey = 'category__name'
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    products = products.annotate(lower_name=Lower('name'))
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

    sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_phrase': query,
        'selected_category': category,
        'sorting': sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """
    A view to show single product details
    """

    product = get_object_or_404(Product, pk=product_id)
    # get reviews for that product
    reviews = Review.objects.filter

    # add review to the product when user is logged in
    if request.method == 'POST' and request.user.is_authenticated:
        rate = request.POST.get('rate', 5)
        comment = request.POST.get('comment', '')
        user = get_object_or_404(UserProfile,
                                 user=request.user)
        review = Review.objects.create(product=product,
                                       user=user, rate=rate,
                                       comment=comment)

    context = {
        'product': product,

    }

    return render(request, 'products/product_details.html', context)
