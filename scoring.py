def IsGuessed(user_text, need_next):
  user_text = user_text.replace(' ', '')
  user_text = user_text.lower()
  need_next = need_next.replace(' ', '')
  need_next = need_next.lower()
  if user_text == need_next:
    return 1
  return 0
