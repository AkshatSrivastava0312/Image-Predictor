from django.shortcuts import render
from .forms import ImageUploadForm
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Create your views here.
def handle_uploaded_file(f):
    with open('images/img.jpg', 'wb+')as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home(request):
    return render(request, 'home.html')

def post(request):
    form = ImageUploadForm(request.POST, request.FILES)

    if form.is_valid():
        handle_uploaded_file(request.FILES['image'])

        model = ResNet50(weights='imagenet')
        img_path = 'images/img.jpg'
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = model.predict(x)        

        predictions = decode_predictions(preds, top=3)[0]

        res = [] 

        for e in predictions:
            res.append((e[1], np.round(e[2]*100, 2)))
        
        return render(request,'home.html', {'res': res})

    return render(request, 'home.html')