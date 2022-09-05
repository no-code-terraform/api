from django.http import JsonResponse


def response_json_200(
  data: dict = None,
  message: str = 'OK',
) -> JsonResponse:
	return JsonResponse(
		{
			'status': 'success',
			'message': message,
			'data': data,
		},
		status=200
	)

def response_json_201(
  message: str = 'Created',
) -> JsonResponse:
	return JsonResponse(
		{
			'status': 'success',
			'message': message,
		},
		status=201
	)


def response_json_400(
  error: dict,
  message: str = 'Bad Request',
) -> JsonResponse:
	return JsonResponse(
		{
			'status': 'failure',
			'message': message,
			'errors': error,
		},
		status=400
	)


def response_json_405(
  message: str = 'Method Not Allowed',
) -> JsonResponse:
	return JsonResponse(
		{
			'status': 'failure',
			'message': message,
		},
		status=405
	)
