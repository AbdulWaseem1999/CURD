from django.shortcuts import render
from .forms import ContactForm
from .models import contact
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    form =ContactForm()
    # contacts=contact.objects.all()
    return render(request,'home.html',{'form':form})


def data(request):
    contacts=contact.objects.values()
    contact_list=list(contacts)
    # print(contact_list)
    return JsonResponse(contact_list,safe=False)



def save_contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contacts_id=request.POST.get('contact_id')
            # print(contacts_id,"hii")
            name=request.POST['name']
            email=request.POST['email']
            mobile=request.POST['mobile']

            if(contacts_id==''):
                cont=contact(name=name,email=email,mobile=mobile)
                cont.save()
                cont_list=contact.objects.values()
                contact_list=list(cont_list)
                contaxt={
                "id":cont.id,
                "name":cont.name,
                 "email":cont.email,
                  "mobile":cont.mobile,} 
                return JsonResponse({'status':'save','contact_list':contaxt})
            else:
                cont=contact(id=contacts_id,name=name,email=email,mobile=mobile)
                cont.save()
           
                contaxt={
                "id":cont.id,
                "name":cont.name,
                 "email":cont.email,
                  "mobile":cont.mobile,}   
                return JsonResponse({'status':'edit','contact_list':contaxt})
        else:
            return JsonResponse({'status':0})
        


@csrf_exempt
def delete_contact(request):
    if request.method=="POST":
        id=request.POST.get('contact_id')
        # print(id)
        contact_row=contact.objects.get(pk=id)
        contact_row.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    


def edit_contact(request):
     if request.method=="POST":
        id=request.POST.get('contact_id')
        # print(id)
        contacts=contact.objects.get(pk=id)
        contact_list={"id":contacts.id,"name":contacts.name,"email":contacts.email,"mobile":contacts.mobile}
        # print(contacts.id)
        return JsonResponse(contact_list)



