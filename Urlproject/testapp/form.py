from django.forms import froms 

class EmployeeForm(forms.Form):
    eno=forms.IntegerFields()
    ename=forms.charFields()
    esal=forms.IntegerFields()

    
