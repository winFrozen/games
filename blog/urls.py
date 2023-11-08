from django.urls import path
from .views import index, about, contact, product, remot, video, productdetailview, videodetailview, contactdetailview, remotdetailview
urlpatterns = [
    path('', index, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("product/", product, name='product'),
    path("remot/", remot, name='remot'),
    path("video/", video, name='video'),
    path("product/<int:id>", productdetailview, name='product_list_view'),
    path("video/<int:id>", videodetailview, name='video_detail_view'),
    path("contact/<int:id>", contactdetailview, name='contact_detail_view'),
    path("remot/<int:id>", remotdetailview, name='remot_detail_view')
]










