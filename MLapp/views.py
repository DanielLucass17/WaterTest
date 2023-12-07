from django.shortcuts import render
from joblib import load
model = load('./ModelosSalvos/modelo_arvore_decisao.joblib')

def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    ph = request.GET['ph']
    Hardness = request.GET['Hardness']
    Solids = request.GET['Solids']
    Chloramines = request.GET['Chloramines']
    Sulfate = request.GET['Sulfate']
    Conductivity = request.GET['Conductivity']
    Organic_carbon = request.GET['Organic_carbon']
    Trihalomethanes = request.GET['Trihalomethanes']
    Turbidity = request.GET['Turbidity']
    y_pred = model.predict([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    if y_pred[0] == 0:
        y_pred = 'Não Potável'
    else:
        y_pred = 'Potável'
    return render(request, 'resultado.html', {'resultado' : y_pred})