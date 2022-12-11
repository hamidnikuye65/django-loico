from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import (HomePageView,
                    Home2PageView,
                    AboutUsPageView,
                    NotFondPageView,
                    ContactPageView,
                    ConsentPageView,
                    NewsSinglePageView,
                    CatalogPageView,
                    ProjectsPageView,
                    ProjectsSinglePageView,
                    ServicesPageView,
                    ServicesSinglePageView,
                    TeamPageView,
                    CertificatesPageView,
                    MoviesGalleryPageView, )

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('درباره ما', AboutUsPageView.as_view(), name='about'),
    path('صفحه مورد نظر پیدانشد', views.NotFondPageView.as_view(), name='404'),
    path('ارتباط با ما', views.ContactPageView.as_view(), name='contact'),
    path('رضایتنامه ها', views.ConsentPageView.as_view(), name='faq'),
    path('خانه دوم', views.Home2PageView.as_view(), name='index-2'),
    path('اخبار ما', views.NewsSinglePageView.as_view(), name='news-single'),
    path('دریافت کاتالوگ', views.CatalogPageView.as_view(), name='pricing'),
    path('پروژه ها', views.ProjectsPageView.as_view(), name='projects'),
    path('پروژه های بزرگ', views.ProjectsSinglePageView.as_view(), name='projects-single'),
    path('خدمات', views.ServicesPageView.as_view(), name='services'),
    path('خدمات ویژه', views.ServicesSinglePageView.as_view(), name='services-single'),
    path('چارت سازمانی', views.TeamPageView.as_view(), name='team'),
    path('گواهینامه ها', views.CertificatesPageView.as_view(), name='testimonials'),
    path('فیلم ها', views.MoviesGalleryPageView.as_view(), name='typography'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
