from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import UserModel, Products, Post, CatProduct
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'zoz/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/login.html', {'error_message': 'Invalid login'})
    return render(request, 'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_delete(request, user_id):
    try:
        user = UserModel.objects.get(id=user_id)
        user.delete()
        return True, "Пользователь успешно удален."
    except UserModel.DoesNotExist:
        return False, "Пользователь с указанным ID не найден."


@login_required  # Декоратор проверки авторизации
def add_product(request):
    user = UserModel.objects.all()
    if request.user.сustomer:  # Проверка статуса продавца у пользователя
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.seller = request.user.username  # Привязываем продавца к товару
                product.save()
                return redirect('product_detail', product_id=product.id)
        else:
            form = ProductForm()
            context = {'form': form}
        return render(request, 'add_product.html', context)
    else:
        return redirect('home')

def products(request):
    products = Products.objects.all()
    return render(request,'products.html', products)

def product_detail(request, product_id):
    product = get_object_or_404(Products, id = product_id)
    if request.method == 'POST':
        context = {'product': product}
        return render(request, 'product_detail.html', context)
    else:
        redirect('products.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts.html')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def detail_posts(request, id):
    post = get_object_or_404(Post, id=product_id)
    if request.method == 'POST':
        context = {'post': post}
        return render(request, 'post_detail.html', context)
    else:
        redirect('posts.html')

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list') # Здесь 'posts:list' - это имя URL-пути, на который нужно перенаправить после успешного обновления поста
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:list') # Здесь 'posts:list' - это имя URL-пути, на который нужно перенаправить после успешного удаления поста
    return render(request, 'post_delete.html', {'post': post})


def posts_user(request, name):
    user = User.objects.get(username=name)
    posts = Post.objects.filter(author=user)
    context = {'user': user, 'posts': posts}
    return render(request, 'post_user.html', context)


