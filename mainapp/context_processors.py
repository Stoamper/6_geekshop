from basketapp.models import Basket


def basket(request):
    # print("context processor basket works") убрали на 6 уроке оптимизация работы с БД
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return {
        "basket": basket,
    }
