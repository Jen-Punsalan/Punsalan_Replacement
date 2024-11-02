from django.shortcuts import render, redirect, get_object_or_404
from .models import Material, Element, Quotation, Project
from django.contrib.auth.decorators import login_required


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Use the related name defined in the ForeignKey
    materials = project.materials.all()  # Change this line if you defined a different related_name

    return render(request, 'quotes/project_detail.html', {
        'project': project,
        'materials': materials,
    })
@login_required
def request_quote(request):
    if request.method == 'POST':
        # Handle form submission for requesting a quote
        area_size = request.POST.get('area_size')
        description = request.POST.get('description')
        location = request.POST.get('location')

        project = Project.objects.create(
            user=request.user,
            area_size=area_size,
            description=description,
            location=location,
        )

        return redirect('quote_detail', project_id=project.id)

    elements = Element.objects.all()
    return render(request, 'request_quote.html', {'elements': elements})


def home(request):
    return render(request, 'home.html')
@login_required
def material_list(request):
    materials = Material.objects.all()
    return render(request, 'material_list.html', {'materials': materials})


@login_required
def add_material(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        unit = request.POST.get('unit')
        unit_price = request.POST.get('unit_price')
        markup_percentage = request.POST.get('markup_percentage')
        element_id = request.POST.get('element')

        # Create a new Material instance
        material = Material(
            name=name,
            description=description,
            unit=unit,
            unit_price=unit_price,
            markup_percentage=markup_percentage,
            element_id=element_id  # Set the foreign key
        )
        material.save()

        return redirect('material_list')  # Redirect after successful addition

    elements = Element.objects.all()  # Get all elements for the dropdown
    return render(request, 'quotes/add_material.html', {'elements': elements})
@login_required
def edit_material(request, material_id):
    material = Material.objects.get(id=material_id)

    if request.method == 'POST':
        material.name = request.POST.get('name')
        material.description = request.POST.get('description')
        material.unit = request.POST.get('unit')
        material.unit_price = request.POST.get('unit_price')
        material.markup_percentage = request.POST.get('markup_percentage')
        material.save()
        return redirect('material_list')

    return render(request, 'edit_material.html', {'material': material})

