import configuration
import data
import requests


def post_create_new_order(new_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=new_order,
                         headers=data.headers)


"""
response = post_create_new_order(data.new_order)
print(response.status_code)
print(response.json())
"""


def getting_info_about_order_by_track(number_track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK + str(number_track),
                        headers=data.headers)


"""
response = getting_info_about_order_by_track()
print(response.status_code)
"""
