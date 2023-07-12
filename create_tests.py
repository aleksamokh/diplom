# Александра Мохаткина, 6-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_requests



def test_getting_info_about_order_by_track():
    new_orders_response = sender_stand_requests.post_create_new_order(data.new_order)
    track_number = new_orders_response.json()["track"]
    info_order_response = sender_stand_requests.getting_info_about_order_by_track(track_number)
    assert info_order_response.status_code == 200


