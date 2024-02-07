from django.urls import path,include
from. import views,user_login

urlpatterns = [
    path('',views.Home,name='Home'),  
    path('Home',views.Home,name='Home'), 
    path('Single_course',views.Single_course,name='Single_course'),
    path('About',views.About,name='About'),
    path('become_instructor',views.become_instructor,name='become_instructor'),
    path('contact_us',views.contact_us,name='contact_us'),
    
    path('accounts/register', user_login.REGISTER , name='register'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login',views.login,name='login'),
    
    path('error',views.error,name='error'),
    path('coming_soon',views.coming_soon,name='coming_soon'),
    path('gallery',views.gallery,name='gallery'),
    path('index',views.index,name='index'),
    path('terms_of_service',views.terms_of_service,name='terms_of_service'),
    path('recover',views.recover,name='recover'),
    path('faq',views.faq,name='faq'),
    path('pricing',views.pricing,name='pricing'),
    path('shop_cart',views.shop_cart,name='shop_cart'),
    path('shop_checkout',views.shop_checkout,name='shop_checkout'),
    path('shop_list',views.shop_list,name='shop_list'),
    path('shop_order_completed',views.shop_order_completed,name='shop_order_completed'),
    path('shop_single',views.shop_single,name='shop_single'),
    path('lesson_single',views.lesson_single,name='lesson_single'),
    path('instructors_list',views.instructors_list,name='instructors_list'),
    path('instructors_single',views.instructors_single,name='instructors_single'),
    path('blog_grid_v1',views.blog_grid_v1,name='blog_grid_v1'),
    path('blog_grid_v2',views.blog_grid_v2,name='blog_grid_v2'),
    path('blog_list_v1',views.blog_list_v1,name='blog_list_v1'),
    path('blog_single',views.blog_single,name='blog_single'),
    path('course_list_v1',views.course_list_v1,name='course_list_v1'),
    path('course_list_v2',views.course_list_v2,name='course_list_v2'),
    path('course_list_v3',views.course_list_v3,name='course_list_v3'),
    path('course_list_v4',views.course_list_v4,name='course_list_v4'),
    path('course_list_v5',views.course_list_v5,name='course_list_v5'),
    path('course_list_v6',views.course_list_v6,name='course_list_v6'),
    path('event_list',views.event_list,name='event_list'),
    path('event_single',views.event_single,name='event_single'),
    
    
]
