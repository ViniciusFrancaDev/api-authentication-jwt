from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


def create_authentication_token(user_id, secret='access_secret', duration_in_minutes=60):
    """Generates a JWT token
    :param user_id: id of the user that will have the generated token
    :type user_id: int
    :param secret: secret used to generate the token during encode process
    :type secret: str
    :param duration_in_minutes: time in minutes that the generated token will be valid
    :type duration_in_minutes: int
    :return: encoded JWT
    :rtype: str
    """
    return jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=duration_in_minutes),
        'iat': datetime.datetime.utcnow()
    }, secret, algorithm='HS256')


def decode_authentication_token(access_token, secret='access_secret'):
    """Decodes a JWT token
    :param access_token: authorization access token
    :type access_token: str
    :param secret: secret used to generate the token during encode process
    :type secret: str
    :return: user id from the token
    :rtype: int
    """
    try:
        payload = jwt.decode(access_token, secret, algorithms='HS256')

        return payload['user_id']
    except:
        raise AuthenticationFailed('Unauthenticated')
