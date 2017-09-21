def authenticatedUsersOnly(fn, info, request, **kwargs):
  if not request.user:
    return None

  def wrapper():
    
  return wrapper