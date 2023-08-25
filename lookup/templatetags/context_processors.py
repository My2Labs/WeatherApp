def form_name(request):
    form_name = request.session.get('myname', None)
    return {'form_name': form_name}
