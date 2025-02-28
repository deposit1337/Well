"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys

sys.path.append('D:/Well-ecommerce-api/main/')

from basket import views
from catalog import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap



from catalog.sitemaps import StaticViewSitemap, ProductSitemap


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}


# from main.catalog import views

# handler404 = 'catalog.views.page_not_found_view'


handler404 = 'catalog.views.custom_404_view'
handler500 = 'catalog.views.custom_500_view'

router = DefaultRouter()
router.register(r'item', views.ItemView)
router.register(r'category', views.CategoryView)

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('', include('catalog.urls', namespace='catalog')),
    path('', views.home_page, name='home_page'),
    path('catalog/<slug:category_slug>/', views.catalog, name='category_catalog'),
    path('catalog/<slug:category_slug>/<int:item_id>/', views.item_detail, name='item_detail'),
    path('basket/', include('basket.urls', namespace='basket')),
    path('search/', views.search, name='search'),
    # path('test_404', views.test_404, name='test_404'),


]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
