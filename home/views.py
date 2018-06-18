from django.views import generic
from .models import MissingPerson, FoundPerson
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, MissingForm, FoundForm
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


# def home(request):
# return render(request, 'home/home.html')


def home(request):
    # template = loader.get_template('home/home.html')
    # return HttpResponse(template.render(request))
    return render(request, 'home/home.html')


def MissingProfiles(request):
    all_Mprofiles = MissingPerson.objects.all()
    # mtemplate = loader.get_template('home/MissingPerson.html')
    context = {'all_Mprofiles': all_Mprofiles}
    # mhtml = ''
    # for mprofile in all_Mprofiles:
    # url = '/home/MissingProfiles/' + str(mprofile.id) + '/'
    # mhtml += '<a href="' + url + '">' + mprofile.FirstNeme + '</a><br>'
    # return HttpResponse(mtemplate.render(context, request))
    return render(request, 'home/MissingPerson.html', context)


def FoundProfiles(request):
    all_Fprofiles = FoundPerson.objects.all()
    # ftemplate = loader.get_template('home/FoundPerson.html')
    context = {'all_Fprofiles': all_Fprofiles}
    # fhtml = ''
    # for fprofile in all_Fprofiles:
    # url = '/home/FoundProfiles/' + str(fprofile.id) + '/'
    # fhtml += '<a href="' + url + '">' + fprofile.id + '</a><br>'
    # return HttpResponse(ftemplate.render(context, request))
    return render(request, 'home/FoundPerson.html', context)


def missingDetails(request, MissingPerson_ID):
    # try:
    # mprofile = MissingPerson.objects.get(pk=MissingPerson_ID)
    # except MissingPerson.DoesNotExist:
    # raise Http404("Missing Profile Does Not Exist")
    mprofile = get_object_or_404(MissingPerson, pk=MissingPerson_ID)
    return render(request, 'home/missingDetails.html', {'mprofile': mprofile})
    # return HttpResponse("<h2>Details For MissingPerson_ID:" + str(MissingPerson_ID) + "</h2>")


def foundDetails(request, FoundPerson_ID):
    # try:
    # fprofile = MissingPerson.objects.get(pk=FoundPerson_ID)
    # except MissingPerson.DoesNotExist:
    # raise Http404("Missing Profile Does Not Exist")
    fprofile = get_object_or_404(FoundPerson, pk=FoundPerson_ID)
    return render(request, 'home/foundDetails.html', {'fprofile': fprofile})
    # return HttpResponse("<h2>Details For FoundPerson_ID:" + str(FoundPerson_ID) + "</h2>")


def logedin(request):
    return render(request, 'home/logedin.html')


# class MissingProfilesView(generic.ListView):
# template_name = 'home/MissingPerson.html'

# def get_queryset(self):
# return MissingPerson.objects.all()


# class FoundProfilesView(generic.ListView):
# template_name = 'home/FoundPerson.html'

# def get_queryset(self):
# return FoundPerson.objects.all()


# class missingDetailsView(generic.DetailView):
# model = MissingPerson
# template_name = 'home/missingDetails.html'


# class foundDetailsView(generic.DetailView):
# model = FoundPerson
# template_name = 'home/foundDetails.html'


# class mprofilecreate(CreateView):
# model = MissingPerson
# fields = {'FirstName', 'SecondName', 'Sex', 'AgeBeforeMissing', 'DateOfBirth', 'HairColour', 'EyesColour', 'Weight',
# 'Height', 'MissingFrom', 'MissingDate', 'RelativeID', 'RelativeRelation', 'Details', 'MissingPersonImage'}


def mprofilecreate(request):
    if not request.user.is_authenticated():
        return render(request, 'home/LogIn_form.html')
    else:
        form = MissingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            mprofile = form.save(commit=False)
            mprofile.user = request.user
            mprofile.MissingPersonImage = request.FILES['MissingPersonImage']
            file_type = mprofile.MissingPersonImage.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'mprofile': mprofile,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'home/mprofileform.html', context)
            mprofile.save()
            return render(request, 'home/logedin.html', {'mprofile': mprofile})
        context = {
            "form": form,
        }
        return render(request, 'home/mprofileform.html', context)


# class fprofilecreate(CreateView):
# model = FoundPerson
# fields = {'Sex', 'FoundIn', 'FoundDate', 'Location', 'Details', 'FoundPersonImage'}


def fprofilecreate(request):
    if not request.user.is_authenticated():
        return render(request, 'home/LogIn_form.html')
    else:
        form = FoundForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            fprofile = form.save(commit=False)
            fprofile.user = request.user
            fprofile.FoundPersonImage = request.FILES['FoundPersonImage']
            file_type = fprofile.FoundPersonImage.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'fprofile': fprofile,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'home/fprofileform.html', context)
            fprofile.save()
            return render(request, 'home/logedin.html', {'fprofile': fprofile})
        context = {
            "form": form,
        }
        return render(request, 'home/fprofileform.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registeration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                # if user.is_active:
                login(request, user)
                return redirect('home:logedin')

        return render(request, self.template_name, {'form': form})


class LogInFormView(View):
    form_class = UserForm
    template_name = 'home/LogIn_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:logedin')

        return render(request, self.template_name, {'form': form})
