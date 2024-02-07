from django.shortcuts import render

def Home(request):
    return render(request,'Main\Home.html')

def Single_course(request):
    return render(request,'Main\Single_course.html')

def About(request):
    return render(request,'Main\About.html')

def become_instructor(request):
    return render(request,'Main\\become-instructor.html')

def contact_us(request):
    return render(request,'Main\contact-us.html')

def login(request):
    return render(request,'registration\login.html')

def coming_soon(request):
    return render(request,'Main\coming-soon.html')

def error(request):
    return render(request,'Main\\404.html')

def gallery(request):
    return render(request,'Main\gallery.html')

def index(request):
    return render(request,'Main\index.html')

def terms_of_service(request):
    return render(request,'Main\\terms-of-service.html')

def pricing(request):
    return render(request,'Main\pricing.html')

def recover(request):
    return render(request,'Main\\recover.html')

def register(request):
    return render(request,'registration\\register.html')

def faq(request):
    return render(request,'Main\\faq.html')

def shop_cart(request):
    return render(request,'Main\shop-cart.html')

def shop_checkout(request):
    return render(request,'Main\shop-checkout.html')

def shop_list(request):
    return render(request,'Main\shop-list.html')

def shop_order_completed(request):
    return render(request,'Main\shop-order-completed.html')

def shop_single(request):
    return render(request,'Main\shop-single.html')

def lesson_single(request):
    return render(request,'Main\lesson-single.html')

def instructors_list(request):
    return render(request,'Main\instructors-list.html')

def instructors_single(request):
    return render(request,'Main\instructors-single.html')

def blog_grid_v1(request):
    return render(request,'blog-grid-v1.html')

def blog_grid_v2(request):
    return render(request,'blog-grid-v2.html')

def blog_list_v1(request):
    return render(request,'blog-list-v1.html')

def blog_single(request):
    return render(request,'blog-single.html')

def course_list_v1(request):
    return render(request,'course-list-v1.html')

def course_list_v2(request):
    return render(request,'course-list-v2.html')

def course_list_v3(request):
    return render(request,'course-list-v3.html')

def course_list_v4(request):
    return render(request,'course-list-v4.html')

def course_list_v5(request):
    return render(request,'course-list-v5.html')

def course_list_v6(request):
    return render(request,'course-list-v6.html')

def event_list(request):
    return render(request,'event-list.html')

def event_single(request):
    return render(request,'event-single.html')
