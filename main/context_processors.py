from main.forms import SignUpModelForm

def signup_form(request):
    return {"signup_form": SignUpModelForm()}