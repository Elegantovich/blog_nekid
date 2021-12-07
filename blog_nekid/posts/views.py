from django.shortcuts import render, get_object_or_404
from .models import Post, Follow, User, Viewed
from django.core.paginator import Paginator
from .forms import PostForm
from django.shortcuts import redirect
from .sent_mail import send_message_to_mail


def index(request):
    """Главная страница отображения блогов."""
    temp = 'posts/index.html'
    blogs = User.objects.all()
    paginator = Paginator(blogs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, temp, context)


def post_create(request):
    """Создаем пост получаем уведомление на почту."""
    form = PostForm(request.POST or None)
    if form.is_valid():
        post_object = form.save(commit=False)
        post_object.author = request.user
        result = user_filter(request)
        print(result)
        post = Post.objects.latest('id')
        post_id = post.id
        if result:
            for i in result:
                follower = get_object_or_404(User, username=i)
                author = request.user
                username = follower.username
                email = follower.email
                send_message_to_mail(username, author, email, post_id)
        post_object.save()
        return redirect('posts:blog', post_object.author)
    return render(request, 'posts/create_post.html', {'form': form})


def user_filter(request):
    """Обратотка Queryset подписчиков."""
    followers = request.user.following.all()
    followers_count = followers.count()
    list_follower = []
    for m in followers:
        str(m.user)
        list_follower.append(str(m.user))
        if len(list_follower) == followers_count:
            return list_follower


def post_edit(request, post_id):
    """Редактирование поста."""
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id)
    form = PostForm(request.POST or None,
                    files=request.FILES or None,
                    instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id)
    return render(request, 'posts/create_post.html',
                  {'form': form,
                   'post': post,
                   'post_id': post_id,
                   'is_edit': True})


def post_detail(request, post_id):
    """Информация о посте + отметка прочтения."""
    userman = request.user.is_authenticated
    post = get_object_or_404(Post, id=post_id)
    if userman:
        vieved_post = post.read_post.filter(user=request.user).exists()
    context = {
        'post': post,
        'vieved_post': vieved_post
        }
    return render(request, 'posts/post_detail.html', context)


def blog(request, username):
    """Информация о блоге + подписка."""
    blog = get_object_or_404(User, username=username)
    all_posts = blog.posts.all()
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    following = request.user.is_authenticated
    if following:
        following = blog.following.filter(user=request.user).exists()
    context = {
        'page_obj': page_obj,
        'blog': blog,
        'all_posts': all_posts,
        'following': following,
    }
    return render(request, 'posts/blog.html', context)


def follow_index(request):
    """Вывод постов избранных блогеров."""
    all_posts = Post.objects.filter(author__following__user=request.user)
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/follow.html', context)


def blog_follow(request, username):
    """Подписка."""
    author = get_object_or_404(User, username=username)
    if author != request.user:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('posts:blog', author)


def blog_unfollow(request, username):
    """Отписка."""
    author = get_object_or_404(User, username=username)
    follower = get_object_or_404(Follow, user=request.user, author=author)
    follower.delete()
    return redirect('posts:blog', follower.author)


def post_viewed(request, post_id):
    """Отметка о прочтении."""
    post = get_object_or_404(Post, id=post_id)
    Viewed.objects.get_or_create(user=request.user, post=post)
    return redirect('posts:post_detail', post_id)


def post_unviewed(request, post_id):
    """Отметка о прочтении."""
    post = get_object_or_404(Post, id=post_id)
    post_view = get_object_or_404(Viewed, user=request.user, post=post)
    post_view.delete()
    return redirect('posts:post_detail', post_id)
