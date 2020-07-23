from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Patient
from .forms import PatientForm


def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})


def create_patient(request):
    form = PatientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_patients')

    return render(request, 'patient-form.html', {'form': form})


def update_patient(request, id):
    # busca o paciente no banco, pelo id passado
    patient = get_object_or_404(Patient, id=id)
    # cria o form instanciando o paciente recuperado do banco
    form = PatientForm(request.POST or None, instance=patient)

    if form.is_valid():
        form.save()
        return redirect('list_patients')

    return render(request, 'patient-form.html', {'form': form, 'patient': patient})


def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        patient.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_patient.html", {'patient': patient})
