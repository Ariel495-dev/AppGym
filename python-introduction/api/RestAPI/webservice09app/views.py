from django.http import HttpResponse

def my_first_view(request):
    return HttpResponse("Hola, mundo, esta vez usando un HttpResponse")

def my_second_view(request):
    return HttpResponse("""<html>
  <body>
    <h1>1, 2, probando...</h1>
    <p>Ahí van tres emperadores romanos</p>
    <ul>
      <li>Tiberio</li>
      <li>Claudio</li>
      <li>Trajano</li>
    <ul>
  </body>
</html>""")
