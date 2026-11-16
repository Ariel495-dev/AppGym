import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def login_endpoint(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON inválido"}, status=400)

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return JsonResponse({"error": "username y password son obligatorios"}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"error": "Credenciales inválidas"}, status=401)

    login(request, user)
    return JsonResponse({
        "everything_ok": True,
        "message": "Login correcto",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        },
    })


def logout_endpoint(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    logout(request)
    return JsonResponse({"everything_ok": True, "message": "Sesión cerrada"})


def profile_endpoint(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "No autenticado"}, status=401)

    return JsonResponse({
        "everything_ok": True,
        "user": {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "is_staff": request.user.is_staff,
        },
    })