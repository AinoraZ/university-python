from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from forms.forms import MaterialActForm, MaterialsForm
from forms.generate_pdf import render_to_pdf
from forms.models import MaterialAct
from django.db.models import Q


def authorize(current_user, material_act):
    responsible = [u.id for u in material_act.commissioners.all()] + [material_act.responsible_worker.id]
    if current_user.id not in responsible:
        return False

    return True


@login_required()
def index(request):
    material_acts = MaterialAct.objects\
        .filter(Q(commissioners__id=request.user.id) | Q(responsible_worker__id=request.user.id))\
        .order_by('-date_created')\
        .distinct()

    return render(request, 'forms/index.html', {'material_acts': material_acts})


@login_required()
def material_act_form(request):
    if request.method == 'POST':
        form = MaterialActForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forms:index')
    else:
        form = MaterialActForm()

    return render(request, 'forms/materialActForm.html', {'form': form})


@login_required()
def material_act_form_details(request, act_id):
    material_act = get_object_or_404(MaterialAct, pk=act_id)
    if not authorize(request.user, material_act):
        return redirect('%s?next=%s' % ("/users/login/", request.path))

    total = 0
    for material in material_act.materials.all():
        total += material.sum

    return render(request, 'forms/materialActDetails.html', {'material_act': material_act, 'material_total': total})


@login_required()
def material_act_form_details_pdf(request, act_id):
    material_act = get_object_or_404(MaterialAct, pk=act_id)
    if not authorize(request.user, material_act):
        return redirect('%s?next=%s' % ("/users/login/", request.path))

    total = 0
    for material in material_act.materials.all():
        total += material.sum

    return render_to_pdf('forms/materialActDetailsPdf.html', {
        'material_act': material_act,
        'material_total': total,
        'pagesize': 'A4'
    })


@login_required()
def material_form(request, act_id):
    material_act = get_object_or_404(MaterialAct, pk=act_id)
    if not authorize(request.user, material_act):
        return redirect('%s?next=%s' % ("/users/login/", request.path))

    if request.method == 'POST':
        form = MaterialsForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.material_act = material_act

            temp_form.save()

            return redirect('forms:material_act_form_details', act_id=act_id)
    else:
        form = MaterialsForm()

    return render(request, 'forms/materialForm.html', {'form': form, 'material_act': material_act})
