from django import forms
from .models import UserProfile, Order, UserCreation, Authentication
from .models import Department

from django import forms
from .models import Department

class StudentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    dob = forms.DateField(label='DOB', widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone_number = forms.CharField(label='Phone Number', max_length=10)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    department = forms.ModelChoiceField(label='Department', queryset=Department.objects.all())


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['department'] = forms.ChoiceField(label='department', choices=[ ('select your department', 'Select your department'),
        (1, 'Civil'),
        (2,'Computer Science'),
        (3,'Commerce'),])
        self.fields['course'] = forms.ChoiceField(label='Course', choices=[('select your course','select your course'),('B.Com','B.Com'),('M.COM','M.COM'),('Computer Application','Computer Application'),('Maths','Maths'),])
        self.fields['purpose'] = forms.ChoiceField(label='Purpose', choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
        self.fields['materials_provided'] = forms.MultipleChoiceField(label='Materials Provided',
        choices=[
        ('question_paper', 'Question Paper'),
        ('notebook', 'Notebook'),
        ('pen', 'Pen'),
        ('exam_paper', 'Exam Papers')], widget=forms.CheckboxSelectMultiple)


        if 'department' in self.data:
            department_id = int(self.data.get('department', 0))
            department = Department.objects.filter(pk=department_id).first()

            if department:
                courses = department.course_set.all().values_list('id', 'name')
                self.fields['course'].choices = courses

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['user']

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = UserCreation
        exclude = ['user']
class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = Authentication
        exclude = ['user']

    def get_user(self):
        pass