default_settings={"theme":"light","language":"english","notification":True}


user_setting={
    "theme":"dark","notification":True
}
final_settings=default_settings.copy()
final_settings.update(user_setting)

print(final_settings)