from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm


# ── List / Dashboard ──────────────────────────────────────────────────────────
def student_list(request):
    """Display all students with optional search & course filter."""
    students = Student.objects.all()

    search_query  = request.GET.get('search', '').strip()
    course_filter = request.GET.get('course', '').strip()

    if search_query:
        students = students.filter(name__icontains=search_query)

    if course_filter:
        students = students.filter(course_interest__icontains=course_filter)

    # Build a unique list of courses for the filter dropdown
    all_courses = Student.objects.values_list('course_interest', flat=True).distinct()

    context = {
        'students':     students,
        'all_courses':  all_courses,
        'search_query': search_query,
        'course_filter': course_filter,
        'total':        Student.objects.count(),
        'new_count':    Student.objects.filter(status='New').count(),
        'enrolled':     Student.objects.filter(status='Enrolled').count(),
        'rejected':     Student.objects.filter(status='Rejected').count(),
    }
    return render(request, 'student_list.html', context)


# ── Add Student ───────────────────────────────────────────────────────────────
def add_student(request):
    """Render and handle the Add Student form."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form, 'title': 'Add New Student'})


# ── Edit Student ──────────────────────────────────────────────────────────────
def edit_student(request, pk):
    """Edit an existing student."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {'form': form, 'title': 'Edit Student'})


# ── Delete Student ────────────────────────────────────────────────────────────
def delete_student(request, pk):
    """Delete a student record."""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student removed successfully!')
    return redirect('student_list')
