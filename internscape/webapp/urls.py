from django.urls import path

from . import views

urlpatterns = [


    path('',views.home, name=""),
    path('register', views.candidate_register, name="register"),
    path('my-login', views.candidate_login, name="my-login"),
    path('company-register', views.company_register, name='company-register'),
    path('company-login', views.company_login, name='company-login'),
    path('company-dashboard', views.company_dashboard, name='company-dashboard'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user-logout',views.user_logout, name = "user-logout" ),

    path('superadmin-dashboard/', views.superadmin_dashboard, name='superadmin-dashboard'),

    path('post-job', views.post_job, name='post-job'),
    path('view-jobs', views.view_jobs, name='view-jobs'),
    path('apply-for-job/<int:job_id>/', views.apply_for_job, name='apply-for-job'),
    path('job-postings/', views.job_postings_list, name='job-postings'),
    path('job-postings/<int:job_id>/applications/', views.job_applications_detail, name='job_applications_detail'),
    path('job-postings/<int:job_id>/export-applications/', views.export_applications, name='export-applications'),

    path('blogs/', views.view_blogs, name='view-blogs'),
    path('create-blog/', views.create_blog, name='create-blog'),
    path('approve-blog/<int:blog_id>/', views.approve_blog, name='approve-blog'),
    path('reject-blog/<int:blog_id>/', views.reject_blog, name='reject-blog'),
    path('delete-blog/<int:blog_id>/', views.delete_blog, name='delete-blog'),

]


