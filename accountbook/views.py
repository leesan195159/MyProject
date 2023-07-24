import json

from django.views import View
from django.http  import JsonResponse

from accountbook.models import AccountBook
from cores.decorator    import login_authorization


class PostAccountBook(View):
    @login_authorization
    def post(self, request):
        try:
            data          = json.loads(request.body)
            amount        = data['amount']
            amount_detail = data['amount_detail']
            note_content  = data['note_content']
            url           = data['url']
            user          = request.user

            AccountBook.objects.create(
                user_id       = user.id,
                amount        = amount,

                
                amount_detail = amount_detail,
                note_content  = note_content,
                url           = url
            )
            return JsonResponse({'message': 'Success'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'Key_Error'}, status=401)
        except ValueError:
            return JsonResponse({'message': 'Value_Error'}, status=408)


class GetAccountBook(View):
    @login_authorization
    def get(self, request, user_id):
        accountbooks = AccountBook.objects.filter(user_id=user_id)

        if not accountbooks.exists():
            return JsonResponse({'message': 'Invalid_User'}, status=410)

        result = [{
            'userId'       : user_id,
            'accountbookId': accountbook.id,
            'amount'       : accountbook.amount,
            'amount_detail': accountbook.amount_detail,
            'note_content' : accountbook.note_content
        }for accountbook in accountbooks]
        return JsonResponse({'message': result}, status=200)


class PatchAccountBook(View):
    @login_authorization
    def patch(self, request, accountbook_id):
        try:
            data          = json.loads(request.body)
            user          = request.user
            amount        = data['amount']
            amount_detail = data['amount_detail']
            note_content  = data['note_content']
            accountbook   = AccountBook.objects.get(id=accountbook_id, user_id=user.id)

            if AccountBook.objects.filter(id=accountbook_id).exists():
                accountbook.amount        = amount
                accountbook.amount_detail = amount_detail
                accountbook.note_content  = note_content
                accountbook.save()
                return JsonResponse({'message': 'Changed'}, status=200)
            return JsonResponse({'message': 'Does_Not_Exist'}, status=411)

        except KeyError:
            return JsonResponse({'message': 'Key_Error'}, status=401)


class DeleteAccountBook(View):
    @login_authorization
    def delete(self, request):
        try:
            accountbook_ids = request.GET.getlist('accountbook_id')
            user = request.user

            if not accountbook_ids:
                return JsonResponse({'message': 'List_Empty'}, status=412)

            AccountBook.objects.filter(id__in=accountbook_ids, user_id=user.id).delete()
            return JsonResponse({'message': 'Deleted'}, status=200)

        except ValueError:
            return JsonResponse({'message': 'Value_Error'}, status=408)


class AmountDetailUrl(View):
    @login_authorization
    def patch(self, request, accountbook_id):
        user = request.user
        accountbook = AccountBook.objects.get(id=accountbook_id, user_id=user.id)

        if AccountBook.objects.filter(id=accountbook_id).exists():
            accountbook.url = accountbook.amount_detail
            accountbook.save()
            return JsonResponse({'message'       : 'Changed',
                                 'accountbook_id': accountbook.id,
                                 'user_id'       : accountbook.user_id,
                                 'amount'        : accountbook.amount,
                                 'amount_detail' : accountbook.amount_detail,
                                 'note_content'  : accountbook.note_content
                                 }, status=200)
        return JsonResponse({'message': 'Does_Not_Exist'}, status=411)


