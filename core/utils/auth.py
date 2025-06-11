# auth/middleware.py
import jwt
from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from user_auth.models import Session, User
from decouple import config

SECRET_KEY = config('JWT-SECRET')

def authenticate(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check Authorization header
        token = request.headers.get('Authorization', '').replace('Bearer ', '')

        # If not in header, check cookies
        if not token:
            token = request.COOKIES.get('token', '')

        if not token:
            return Response({"message": "No Auth token provided."}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token expired."}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({"error": "Invalid token."}, status=status.HTTP_401_UNAUTHORIZED)

        session = Session.objects(token=token).first()
        if not session:
            return Response({"error": "Session invalid or expired."}, status=status.HTTP_401_UNAUTHORIZED)

        # Fetch user and attach to request
        user = User.objects(id=payload['user_id']).first()
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_401_UNAUTHORIZED)

        request.user = user  # 🔐 Attach user object to request
        request.token = token
        return view_func(request, *args, **kwargs)
    
    return wrapper
