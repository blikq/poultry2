from django.urls import path
from .views import *

urlpatterns = [
    path('', index_render, name="home"),

    path('about', about_render, name="about-us"),

    path('blog/<int:id>', news_sin_render, name="blog-single"),
    path('vlog/<int:id>', blogs_sin_render, name="vlogs-single"),

    path('blog/<int:id>/edit', edit_news_render, name="news-edit"),
    path('vlog/<int:id>/edit', edit_blog_render, name="blogs-edit"),


    path('blogs', blogs_render, name="vlogs"),
    path('news', news_render, name="news"),

    path('contact', contact_render, name="contact-us"),

    path('master/dashboard', dashboard_render, name="master-dashboard"),
    path('master/login', login_render, name="login"),
    path('master/logout', logout_, name="logout"),

    path('api/delete', delete_api, name="delete-api"),
] 


#ignore for media routing
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)