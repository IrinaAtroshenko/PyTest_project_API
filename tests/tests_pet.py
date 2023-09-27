from api import Pets

pt = Pets()


def test_get_registration():
    status = pt.get_registration()[0]
    assert status == 200


def test_get_token():
    status = pt.get_token()[1]
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_post_pet():
    status = pt.post_pet()[1]
    pet_id = pt.post_pet()[0]
    assert status == 200
    assert pet_id


def test_post_pet_photo():
    status = pt.post_pet_photo()[0]
    link = pt.post_pet_photo()[1]
    assert status == 200
    assert link


def test_put_pet_like():
    status = pt.put_pet_like()
    assert status == 200


def test_put_pet_comment():
    status = pt.put_pet_comment()
    assert status == 200


def test_get_pet_info():
    status = pt.get_pet_info()[0]
    pet_id = pt.get_pet_info()[1]
    assert status == 200
    assert pet_id


def test_update_pet_type():
    status = pt.update_pet_type()
    assert status == 200


def test_post_pet_list():
    status = pt.post_pet_list()[0]
    assert status == 200


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200


def test_delete_all_pets():
    status = pt.delete_all_pets()
    assert status == 200


def test_delete_user():
    status = pt.delete_user()[0]
    assert status == 200
